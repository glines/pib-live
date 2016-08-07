#!/usr/bin/python2
# -*- coding: utf-8 -*-

import urwid

class MenuItemWidget(urwid.TreeWidget):
    def __init__(self, *args, **kwargs):
        urwid.TreeWidget.__init__(self, *args, **kwargs)
        self.expanded = False

#    def render(self, size, focus=False):
#        canvas = urwid.TreeWidget.render(self, size, focus=focus)
#        canvas = urwid.CompositeCanvas(canvas)
#        attr_map = {None: 'tree_item'}
#        if focus:
#            attr_map = {None: 'focus'}
#        canvas.fill_attr_apply(attr_map)
#        return canvas

    def get_display_text(self):
        return self.get_node().get_display_text()

class SubmenuItemWidget(MenuItemWidget):
    _right_arrow = urwid.Text(u'--->')

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        # Add the ---> to the end
        widget = urwid.Columns([
              ('pack', widget),
              ('fixed', 4, self._right_arrow),
            ], dividechars=2)
        # Apply the indentation
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        widget = urwid.AttrWrap(widget, 'tree_item', focus_attr='focus')
        return widget

    def get_actions(self):
        actions = []
        node = self.get_node()
        if len(node.get_child_keys()) > 0:
            actions.append(('Enter', lambda x: x))
        return actions

class OptionItemWidget(MenuItemWidget):
    def __init__(self, *args, **kwargs):
        MenuItemWidget.__init__(self, *args, **kwargs)
        self._update_checkbox()

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        # Apply indentation padding first; the check boxes appear on the far
        # left, as in Linux's "menuconfig" that many people are familiar with
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        # Add the < > or [ ] checkbox
        widget = urwid.Columns([
              ('fixed', 3, self._get_checkbox()),
              widget], dividechars=1)
        widget = urwid.AttrWrap(widget, 'tree_item', focus_attr='focus')
        return widget

    def _get_checkbox(self):
        node = self.get_node()
        if len(node.get_child_keys()) > 0:
            checkbox = '<{}>'
        else:
            checkbox = '[{}]'
        if node._get_selected():
            checkbox = checkbox.format('*')
        else:
            checkbox = checkbox.format(' ')
        checkbox = urwid.Text(checkbox)
        return checkbox

    def _update_checkbox(self):
        self._w.base_widget.widget_list[0] = self._get_checkbox()

    def toggle_selected(self, button):
        node = self.get_node()
        node.selected = not node.selected
        self.expanded = node.selected
        self._update_checkbox()

    def get_actions(self):
        actions = []
        actions.append(('Select', self.toggle_selected))
        node = self.get_node()
        if len(node.get_child_keys()) > 0:
            actions.append(('Select All', lambda x: x))
        return actions

class LabelItemWidget(MenuItemWidget):
    def get_indented_widget(self):
        widget = self.get_inner_widget()
        # Apply the indentation
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        return widget

class DividerItemWidget(MenuItemWidget):
    def get_indented_widget(self):
        widget = urwid.Divider(u'─')
        # Apply the indentation
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        return widget
