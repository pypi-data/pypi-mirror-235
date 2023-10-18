from tui_toolkit import App, BlockingInput, List, style_none


class Chat(App):
    def __init__(self):
        super().__init__(self.input_loop)

    def initialise(self):
        self.input = BlockingInput(
                self.term, 0, self.term.height - 1,
                self.term.width, 1,
                prompt='-> ')
        self.messages = List(
                self.term, 0, 0,
                self.term.width, self.term.height - 1,
                style_focus=style_none)

    def layout(self):
        self.input.resize(width=self.term.width)
        self.messages.resize(
            width=self.term.width, height=self.term.height - 1)
        self.messages.render()
        self.input.render()

    def input_loop(self):
        while not self.terminal_resized:
            msg = self.input.interact()
            self.messages.contents.append(
                    (msg,
                     lambda text, width: self.term.bold(
                         self.term.rjust(text, width))))
            self.messages.contents.append(
                    ('Some smart reply...',
                     lambda text, width: self.term.ljust(text, width)))
            self.messages.set_focus_index(len(self.messages.contents) - 1)
            with self.term.hidden_cursor():
                self.messages.render()
        return self.input_loop


def chat():
    c = Chat()
    c.run()
