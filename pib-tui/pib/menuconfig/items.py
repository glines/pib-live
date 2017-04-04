import urwid

from pib.menuconfig.widgets import (MenuItemWidget, SubmenuItemWidget, OptionItemWidget, LabelItemWidget, DividerItemWidget)

class MenuItem(urwid.ParentNode):
    def __init__(self, *args, **kwargs):
        urwid.ParentNode.__init__(self, *args, **kwargs)

    def load_widget(self):
        return MenuItemWidget(self)

    def is_submenu(self):
        return False

class SubmenuItem(MenuItem):
    def __init__(self, *args, **kwargs):
        MenuItem.__init__(self, *args, **kwargs)

    def load_widget(self):
        return SubmenuItemWidget(self)

    def is_submenu(self):
        return True

class OptionItem(MenuItem):
    def __init__(self, *args, **kwargs):
        MenuItem.__init__(self, *args, **kwargs)
        self._selected = False

    def load_widget(self):
        return OptionItemWidget(self)

    def _get_selected(self):
        return self._selected
    def _set_selected(self, value):
        self._selected = value

    selected = property(_get_selected, _set_selected)

class LabelItem(MenuItem):
    def __init__(self, *args, **kwargs):
        MenuItem.__init__(self, *args, **kwargs)

    def load_widget(self):
        return LabelItemWidget(self)

    def selectable(self):
        return False

class DividerItem(MenuItem):
    def __init__(self, *args, **kwargs):
        MenuItem.__init__(self, *args, **kwargs)

    def load_widget(self):
        return DividerItemWidget(self)

    def selectable(self):
        return False
