from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TabbedContent, TabPane

from oterm.app.chat import ChatContainer
from oterm.app.model_selection import ModelSelection
from oterm.app.splash import SplashScreen
from oterm.store.store import Store


class OTerm(App):
    TITLE = "oTerm"
    SUB_TITLE = "A terminal-based Ollama client."
    CSS_PATH = "oterm.tcss"
    BINDINGS = [
        ("n", "new_chat", "new chat"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("x", "forget_chat", "forget chat"),
        ("q", "quit", "Quit"),
    ]
    SCREENS = {
        "splash": SplashScreen(),
        "model_selection": ModelSelection(),
    }

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        return self.exit()

    def action_new_chat(self) -> None:
        async def on_model_select(model: str) -> None:
            tabs = self.query_one(TabbedContent)
            tab_count = tabs.tab_count
            name = f"chat #{tab_count+1} - {model}"
            id = await self.store.save_chat(
                id=None,
                name=name,
                model=model,
                context="[]",
            )
            pane = TabPane(name, id=f"chat-{id}")
            pane.compose_add_child(ChatContainer(db_id=id, chat_name=name, model=model))
            tabs.add_pane(pane)
            tabs.active = f"chat-{id}"

        self.push_screen("model_selection", on_model_select)

    async def action_forget_chat(self) -> None:
        tabs = self.query_one(TabbedContent)
        active_pane_id = tabs.active

        if active_pane_id:
            await self.store.delete_chat(int(active_pane_id.split("-")[1]))
            tabs.remove_pane(active_pane_id)

    async def on_mount(self) -> None:
        self.store = await Store.create()
        saved_chats = await self.store.get_chats()  # type: ignore
        if not saved_chats:
            self.action_new_chat()
        else:
            tabs = self.query_one(TabbedContent)
            for id, name, model, context in saved_chats:
                messages = await self.store.get_messages(id)
                pane = TabPane(name, id=f"chat-{id}")
                pane.compose_add_child(
                    ChatContainer(
                        db_id=id,
                        chat_name=name,
                        model=model,
                        context=context,
                        messages=messages,  # type: ignore
                    )
                )
                tabs.add_pane(pane)
                tabs.active = f"chat-{id}"

        await self.push_screen("splash")

    def compose(self) -> ComposeResult:
        yield Header()
        yield TabbedContent(id="tabs")
        yield Footer()


app = OTerm()
