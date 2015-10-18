import urwid

class OptionTreeWidget(urwid.TreeWidget):
    """ This class implements a tree of options styled after
        Linux's venerable menuconfig
    """
    def __init__(self, *args, **kwargs):
        urwid.TreeWidget.__init__(self, *args, **kwargs)
        if self.is_leaf:
            # FIXME: Rename these to unselected_icon and selected_icon
            self.unexpanded_icon = urwid.SelectableIcon('[ ]', 0)
            self.expanded_icon = urwid.SelectableIcon('[*]', 0)
        else:
            # FIXME: Rename these to unselected_icon and selected_icon
            # TODO: Add icons to indicate only some things are selected
            self.unexpanded_icon = urwid.SelectableIcon('< >', 0)
            self.expanded_icon = urwid.SelectableIcon('<*>', 0)
        self.expanded = False
        self.update_expanded_icon()

    def get_display_text(self):
        return self.get_node().get_display_text()

    def collapse(self):
        self.expanded = False
        self.update_expanded_icon()

    def expand(self):
        self.expanded = True
        self.update_expanded_icon()

    def toggle_expanded(self):
        self.expanded = not self.expanded
        self.update_expanded_icon()

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        # Apply indentation padding first; the check boxes appear on the far
        # left, as in Linux's "menuconfig" that many people are familiar with
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        # Add the < > or [ ] check box
        widget = urwid.Columns([('fixed', 3,
              [self.unexpanded_icon, self.expanded_icon][self.expanded]),
              widget], dividechars=1)
        return widget

    def keypress(self, size, key):
        # TODO: Make the entire line selectable
        # TODO: Return key to show node details (as in Linux's menuconfig)

        if key in (' '):
            self.toggle_expanded()
        else:
            return key

    def mouse_event(self, size, event, button, col, row, focus):
        if event != 'mouse press' or button != 1:
            return False

        if row == 0 and (col >= 0 and col <= 2):
            self.toggle_expanded()
            return True
        return False
