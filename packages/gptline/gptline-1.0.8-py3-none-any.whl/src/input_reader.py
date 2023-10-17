from dataclasses import dataclass
from prompt_toolkit import PromptSession, print_formatted_text, Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.formatted_text import HTML, FormattedText
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import BufferControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Frame
from src.formatting import formattedTime
from src.ui_utils import draw_horizontal_line
from typing import Optional
import html
import tiktoken

@dataclass
class UserInput:
    text: Optional[str] = None
    # -1 to create a new chat.
    chat_identifier: Optional[int] = None
    query: Optional[str] = None
    message_query: Optional[str] = None
    regenerate = False
    edit = False
    allow_execution = False
    settings = False

@dataclass
class Chat:
    chat_identifier: int
    name: str
    last_update: str
    num_messages: int

def usage(model, text):
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except Exception as e:
        return 0


# Returns UserInput
def read_input(chats, current_chat_name, have_any_messages, placeholder, allow_execution, used, max_tokens, model):
    result = UserInput()
    tokens_typed = [0]
    result.allow_execution = allow_execution

    session = PromptSession()

    def update_tokens_typed(_):
        buffer = session.default_buffer
        tokens_typed[0] = usage(model, buffer.text)
        session.app.invalidate()

    session.default_buffer.on_text_changed += update_tokens_typed
    kb = KeyBindings()

    # Add a binding for the 'Enter' key to insert a newline character
    @kb.add(Keys.Enter)
    def _(event):
        event.current_buffer.insert_text('\n')

    # Add a binding for ^D to accept the input.
    @kb.add(Keys.ControlD)
    def _(event):
        buffer = event.current_buffer
        if buffer.cursor_position < len(buffer.text):
            buffer.delete()
        else:
            buffer.validate_and_handle()

    SHOW_CHAT_LIST = "$$$SHOW_CHAT_LIST"
    NEW_CHAT = "$$$NEW_CHAT"
    SEARCH = "$$$SEARCH"
    SEARCH_THIS_CHAT = "$$$SEARCH_THIS_CHAT"
    REGENERATE = "$$$REGENERATE"
    EDIT = "$$$EDIT"
    TOGGLE_SETTING = "$$$TOGGLE_SETTING"
    SETTINGS = "$$$SETTINGS"

    @kb.add(Keys.F2)
    def _(event):
        app = get_app()
        app.exit(result=SHOW_CHAT_LIST)

    @kb.add(Keys.F3)
    def _(event):
        app = get_app()
        app.exit(result=NEW_CHAT)

    @kb.add(Keys.F4)
    def _(event):
        app = get_app()
        app.exit(result=SEARCH)

    if have_any_messages:
        @kb.add(Keys.F5)
        def _(event):
            app = get_app()
            app.exit(result=REGENERATE)
        @kb.add(Keys.F6)
        def _(event):
            app = get_app()
            app.exit(result=EDIT)

    @kb.add(Keys.F7)
    def _(event):
        result.allow_execution = not result.allow_execution
        if result.allow_execution:
            print("Command execution enabled.")
        else:
            print("Command execution disabled.")
        app = get_app()
        app.exit(result=TOGGLE_SETTING)

    @kb.add(Keys.F8)
    def _(event):
        app = get_app()
        app.exit(result=SEARCH_THIS_CHAT)

    @kb.add(Keys.F10)
    def _(event):
        app = get_app()
        app.exit(result=SETTINGS)

    def read_chat_search_query():
        search_session = PromptSession()
        return search_session.prompt(HTML("<b>Search this chat: </b>"))

    def read_search_query():
        search_session = PromptSession()
        return search_session.prompt(HTML("<b>Search: </b>"))

    def pick_chat():
        print_formatted_text(HTML(f'<b>Select a chat:</b>'))
        show_list = True
        base = 0
        PAGE_SIZE = Application().output.get_size().rows - 2
        while True:
            i = 0
            for chat in chats[base:]:
                i += 1
                if i == PAGE_SIZE + 1:
                    break
                if show_list:
                    time = formattedTime(chat.last_update)
                    n = chat.num_messages - 1
                    s = "s" if n > 1 else ""
                    print_formatted_text(HTML(f'{i}: <b>{html.escape(chat.name)}</b> ({time}, {n} message{s})'))
            show_list = True

            kb = KeyBindings()
            user_pressed_esc = [False]
            @kb.add(Keys.ControlD)
            def _(event):
                user_pressed_esc[0] = True
                event.app.exit()

            # Prompt the user for their selection
            picker_session = PromptSession(key_bindings=kb)
            selection = picker_session.prompt(HTML("<b>Enter chat number, press 'return' for more, + to create a new chat, or '^D' to cancel: </b>"))
            if user_pressed_esc[0]:
                return

            # Handle the user's selection
            if selection.isdigit():
                index = int(selection) + base - 1
                result.chat_identifier = chats[index].chat_identifier
                print_formatted_text(HTML(f'<b>Switched to: {html.escape(chats[index].name)}</b>'))
                return
            elif selection == '':
                if len(chats) > base + PAGE_SIZE:
                    base += PAGE_SIZE
                else:
                    print_formatted_text(HTML('<b>No more chats.</b>'))
                    show_list = False
            elif selection == '+':
                result.chat_identifier = -1
                return
            else:
                print_formatted_text(HTML('<b>Selection canceled or invalid choice.</b>'))


    # Create a frame around the default buffer
    frame = Frame(body=Window(content=BufferControl(buffer=session.default_buffer)))

    # Set the layout of the session to use the frame
    session.layout = Layout(container=frame)

    # Prompt the user for input
    draw_horizontal_line()
    try:
        while True:
            def bottom_toolbar():
                text = f'[{html.escape(current_chat_name)}] <b>M-⏎</b>: Send  <b>F2</b>: Switch chat  <b>F3</b>: New chat  <b>F4</b>: Search'
                if have_any_messages:
                    text += "  <b>F5</b>: Regenerate"
                    text += "  <b>F6</b>: Edit Last"
                if result.allow_execution:
                    text += "  <b>F7</b>: Disable Execution"
                else:
                    text += "  <b>F7</b>: Enable Execution"
                if have_any_messages:
                    text += "  <b>F8</b>: Search Current Chat"
                text += "  <b>F10</b>: Settings"
                text += "  "
                total_used = used + tokens_typed[0]
                if total_used >= max_tokens:
                  text += "<ansired>"
                text += f'{total_used}/{max_tokens} tokens'
                if total_used >= max_tokens:
                  text += "</ansired>"
                return HTML(text)
            value = session.prompt(
                    "",
                key_bindings=kb,
                multiline=True,
                bottom_toolbar=bottom_toolbar,
                default=placeholder
            )
            if value == SHOW_CHAT_LIST:
                pick_chat()
                if result.chat_identifier is not None:
                    return result
            elif value == NEW_CHAT:
                result.chat_identifier = -1
                return result
            elif value == REGENERATE:
                result.regenerate = True
                return result
            elif value == TOGGLE_SETTING:
              continue
            elif value == EDIT:
                result.edit = True
                return result
            elif value == SEARCH_THIS_CHAT:
                try:
                    result.message_query = read_chat_search_query()
                    if result.message_query is not None:
                        return result
                except EOFError:
                    pass
            elif value == SEARCH:
                try:
                    result.query = read_search_query()
                    if result.query is not None:
                        return result
                except EOFError:
                    pass
            elif value == SETTINGS:
                result.settings = True
                return result
            else:
                result.text = value
                return result
    except Exception as e:
        print(e)
        return None
