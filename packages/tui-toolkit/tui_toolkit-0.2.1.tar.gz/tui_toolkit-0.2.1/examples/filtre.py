from tui_toolkit import App, List, Input


class Filtre(App):
    def __init__(self, options):
        super().__init__(self.input_loop)
        self.options = options

    def initialise(self):
        self.filtre_term = Input(
                self.term, 0, 0, self.term.width, 1,
                change_listeners=[self.on_filtre_term_changed])
        self.result_list = List(
                self.term, 0, 1, self.term.width, self.term.height,
                contents=self.options)

    def layout(self):
        self.filtre_term.resize(width=self.term.width)
        self.result_list.resize(width=self.term.width, height=self.term.height)

    def on_filtre_term_changed(self, term):
        self.result_list.set_contents([o for o in self.options if term in o])
        self.result_list.render()

    def input_loop(self):
        with self.term.hidden_cursor():
            self.filtre_term.render()
            self.result_list.render()
            self.filtre_term.interact([self.term.KEY_ENTER])
            if self.terminal_resized:
                return self.input_loop


def filtre():
    f = Filtre(
            ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
             'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November',
             'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
             'Uniform', 'Victor', 'Whisky', 'X-Ray', 'Zulu'])
    f.run()
