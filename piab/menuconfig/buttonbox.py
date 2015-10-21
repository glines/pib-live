import urwid

from piab.menuconfig.motif import MotifLineBox

# TODO: Need a buttonbox class that will consume left/right events and pass
# down up/down events, but not stop drawing the buttons as in focus.
class ButtonBox(urwid.WidgetWrap):
    def __init__(self):
        # TODO: Make the list of buttons more flexible
        # Add <Select>, <Details>, <Start>, and <Exit> buttons to the bottom
        def make_button(name):
            result = ButtonBoxButton(name)
            return result
        self._buttons = []
        self._buttons.append(make_button(u'Select'))
        self._buttons.append(make_button(u'Details'))
        self._buttons.append(make_button(u'Back'))
        self._button_box = urwid.Columns(self._buttons,
            dividechars=3, min_width=(8))
        self._button_box = urwid.Padding(self._button_box,
            align='center', width=55)
        self._button_box = MotifLineBox(self._button_box)

        urwid.WidgetWrap.__init__(self, self._button_box)

    def _get_buttons(self):
        return self._buttons

    buttons = property(_get_buttons)

    def set_actions(self, actions):
        # Make new buttons for these actions
        self._buttons = []
        def make_button(label, callback):
            result = ButtonBoxButton(label, callback)
            return result
        for action in actions:
            button = make_button(label=action[0], callback=action[1])
            self._buttons.append(button)
        # Make a new button box
        self._button_box = urwid.Columns(self._buttons,
            dividechars=3, min_width=(8))
        self._button_box = urwid.Padding(self._button_box,
            align='center', width=55)
        self._button_box = MotifLineBox(self._button_box)
        self._w = self._button_box
        self._invalidate()

    def keypress(self, size, key):
        if key in ('left'):
            self._decrement_pseudo_focus()
            return None
        elif key in ('right'):
            self._increment_pseudo_focus()
        elif key in (' '):
            focus_button = self._find_pseudo_focus()
            if focus_button is None:
                return key
            return self.buttons[focus_button].keypress(size, key)

        return key

    def _find_pseudo_focus(self):
        for i in range(len(self.buttons)):
            if self.buttons[i].pseudo_focus:
                return i
        return None

    def _increment_pseudo_focus(self):
        current_index = self._find_pseudo_focus()
        next_index = (current_index + 1) % len(self.buttons)
        self.buttons[current_index].pseudo_focus = False
        self.buttons[current_index]._invalidate()
        self.buttons[next_index].pseudo_focus = True
        self.buttons[next_index]._invalidate()

    def _decrement_pseudo_focus(self):
        current_index = self._find_pseudo_focus()
        next_index = (current_index - 1) % len(self.buttons)
        self.buttons[current_index].pseudo_focus = False
        self.buttons[current_index]._invalidate()
        self.buttons[next_index].pseudo_focus = True
        self.buttons[next_index]._invalidate()

class ButtonBoxButton(urwid.WidgetWrap):
    def __init__(self, label, callback=None):
        self._button = urwid.Button(label)
        if callback is not None:
            urwid.connect_signal(self._button, 'click', callback)
        self._button = urwid.AttrMap(self._button, 'button', focus_map='button_focus')

        self._pseudo_focus = False

        urwid.WidgetWrap.__init__(self, self._button)

    def _get_pseudo_focus(self):
        return self._pseudo_focus
    def _set_pseudo_focus(self, focus):
        self._pseudo_focus = focus

    pseudo_focus = property(_get_pseudo_focus, _set_pseudo_focus)

    def render(self, size, focus):
        return urwid.WidgetWrap.render(self, size, self.pseudo_focus)
