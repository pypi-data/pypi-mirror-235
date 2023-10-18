from tui_toolkit import App, List, Text, TextBlock, navigate, style_none


class Styling(App):
    def __init__(self):
        super().__init__(self.choose_loop)

    def initialise(self):
        self.heading = Text(
                self.term, 0, 0, 20, 1,
                text='The Article Title')
        self.text = TextBlock(
                self.term, 0, 2,
                20, self.term.height,
                text=('This is the body of the article. There could be quite'
                      ' a lot of text so it should get wrapped automatically'
                      ' and any newlines\nshould be handled properly.'))
        self.chooser = List(
                self.term, 25, 5, self.term.width, self.term.height,
                contents=[
                    'none', 'right', 'bold', 'underline', 'greens', 'blues'],
                style_focus=self.term.reverse,
                focus_listeners=[self.on_style_changed])
        self.chooser.set_focus_index(0)

    def layout(self):
        self.text.resize(height=self.term.height)
        self.chooser.resize(width=self.term.width, height=self.term.height)

    def on_style_changed(self, style_name):
        match style_name:
            case 'none':
                self.heading.style = style_none
                self.text.style = style_none
            case 'right':
                self.heading.style = style_none
                self.text.style = self.term.rjust
            case 'bold':
                self.heading.style = lambda text, width: self.term.bold(text)
                self.text.style = style_none
            case 'underline':
                self.heading.style = (
                        lambda text, width: self.term.underline(text))
                self.text.style = style_none
            case 'greens':
                self.heading.style = (
                        lambda text, width: self.term.darkgreen_on_green(
                            self.term.ljust(text, width)))
                self.text.style = (
                        lambda text, width: self.term.green_on_darkgreen(
                            self.term.ljust(text, width)))
            case 'blues':
                self.heading.style = (
                        lambda text, width: self.term.underline(
                            self.term.blue_on_darkblue(text)))
                self.text.style = (
                        lambda text, width: self.term.darkblue_on_blue(
                            self.term.ljust(text, width)))
        self.heading.render()
        self.text.render()

    def choose_loop(self):
        with self.term.hidden_cursor():
            self.heading.render()
            self.text.render()
            navigate(self.chooser, [self.term.KEY_ENTER])
            if self.terminal_resized:
                return self.choose_loop


def styling():
    s = Styling()
    s.run()
