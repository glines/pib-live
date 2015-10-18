import urwid

import optiontreewidget

class GitBranchNodeWidget(optiontreewidget.OptionTreeWidget):
    pass

class GitBranchNode(urwid.TreeNode):  # TODO: Change this to ParentNode when we add commit browsing support
    def __init__(self, branch, **kwargs):
        self._branch = branch
        urwid.TreeNode.__init__(self, branch.name, **kwargs)

    def get_display_text(self):
        return self._branch.name

    def load_widget(self):
        return GitBranchNodeWidget(self)
