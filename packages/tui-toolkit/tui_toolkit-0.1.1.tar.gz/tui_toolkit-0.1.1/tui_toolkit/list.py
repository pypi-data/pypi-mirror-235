from .core import Window, style_none, resized
from itertools import count


class List(Window):
    def __init__(
            self, term, x0, y0, width, height,
            style=style_none,
            style_focus=None,
            contents=None, formatter=None, focus_listeners=None):
        super().__init__(term, x0, y0, width, height)
        self.contents = contents if contents else []
        self.focus_index_ = None
        self.style = style
        self.style_focus = term.reverse if style_focus is None else style_focus
        self.formatter = formatter
        self.focus_listeners = (
                [] if focus_listeners is None else focus_listeners)

    def set_contents(self, contents):
        self.contents = contents
        if not contents:
            self.set_focus_index(None)
        elif self.focus_index is not None:
            self.set_focus_index(0, True)

    def render(self):
        offset = 0
        if self.focus_index is not None:
            offset = max(0, self.focus_index - self.height + 1)
        for i, item in zip(count(), self.contents[offset:]):
            line = self.formatter(item) if self.formatter else str(item)
            line = self.term.ljust(line)
            if i + offset == self.focus_index:
                line = self.style_focus(line)
            self.print_line(i, self.style(line))
        for i in range(len(self.contents), self.height):
            self.print_line(i, self.style(' ' * self.width))
        if offset:
            self.print(self.width - 1, 0, self.style('▲'))
        if len(self.contents) - offset > self.height:
            self.print(self.width - 1, self.height - 1, self.style('▼'))

    @property
    def focus_index(self):
        return self.focus_index_

    def set_focus_index(self, index, force_notify=False):
        old_index = self.focus_index_
        if not self.contents:
            index = None
        if index is None:
            self.focus_index_ = index
        else:
            self.focus_index_ = min(len(self.contents) - 1, max(0, index))
        if old_index != self.focus_index or force_notify:
            for listener in self.focus_listeners:
                listener(self.focus_item())

    def focus_item(self):
        if self.focus_index is None:
            return None
        return self.contents[self.focus_index]


def navigate(list, action_keys):
    with list.term.cbreak(), list.term.keypad():
        while not resized():
            list.render()
            k = list.term.inkey(1)
            if k.is_sequence:
                match k.code:
                    case other if other in action_keys:
                        return k
                    case list.term.KEY_UP:
                        list.set_focus_index(list.focus_index - 1)
                    case list.term.KEY_DOWN:
                        list.set_focus_index(list.focus_index + 1)
            elif k in action_keys:
                return k
