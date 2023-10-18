from tui_toolkit import App, List, Text, navigate


class Selector(App):
    def __init__(self, options):
        super().__init__(self.select_loop)
        self.options = options

    def initialise(self):
        self.list_options = List(
                self.term, 0, 0,
                self.term.width, self.term.height - 1,
                focus_listeners=[self.on_focus_changed],
                contents=self.options)
        self.text_selected = Text(
                self.term, 0, self.term.height - 1,
                self.term.width, 1)
        self.list_options.set_focus_index(0)

    def layout(self):
        self.list_options.resize(
                width=self.term.width, height=self.term.height - 1)
        self.text_selected.resize(
                y0=self.term.height - 1, width=self.term.width)

    def on_focus_changed(self, focus_item):
        self.text_selected.set_text(focus_item)

    def select_loop(self):
        with self.term.hidden_cursor():
            self.list_options.render()
            self.text_selected.render()
            while True:
                k = navigate(self.list_options, [self.term.KEY_ENTER])
                if self.terminal_resized:
                    return self.select_loop
                if k.is_sequence:
                    match k.code:
                        case self.term.KEY_ENTER:
                            return None


def selector():
    s = Selector(
            ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
             'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November',
             'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
             'Uniform', 'Victor', 'Whisky', 'X-Ray', 'Zulu'])
    s.run()
    print(f'You selected "{s.text_selected.text}".')
