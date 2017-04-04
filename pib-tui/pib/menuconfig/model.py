import urwid

class MenuItem(urwid.ParentNode):
    def __init__(self):
        self._children = []

    def load_child_keys(self):
        value = self.get_value()
        return 

class SubmenuItem(MenuItem):
    def __init__(self):
        MenuItem.__init__(self)

class OptionItem(MenuItem):
    def __init__(self):
        MenuItem.__init__(self)
        self._selected = False

    def _get_selected(self):
        return self._selected
    def _set_selected(self, value):
        self._selected = value

    selected = property(_get_selected, _set_selected)

class LabelItem(MenuItem):
    def __init__(self):
        MenuItem.__init__(self)

    def selectable(self):
        return False
