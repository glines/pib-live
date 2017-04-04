import copy

import urwid

class SubtreeWalker(urwid.TreeWalker):
    def __init__(self, start_from):
        urwid.TreeWalker.__init__(self, start_from)
        self._initial_depth = start_from.get_depth()

    def get_next(self, start_from):
        widget = start_from.get_widget()
        target = widget.next_inorder()
        if target is None:
            return None, None
        elif target.get_node().get_depth() < self._initial_depth:
            # We simply prevent TreeWalker from walking up past our subtree
            return None, None
        return urwid.TreeWalker.get_next(self, start_from)

    def get_prev(self, start_from):
        widget = start_from.get_widget()
        target = widget.prev_inorder()
        if target is None:
            return None, None
        elif target.get_node().get_depth() < self._initial_depth:
            # We simply prevent TreeWalker from walking up past our subtree
            return None, None
        return urwid.TreeWalker.get_prev(self, start_from)
