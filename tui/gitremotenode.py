from git import Repo

import urwid

import gitbranchnode
import optiontreewidget

class GitRemoteNodeWidget(optiontreewidget.OptionTreeWidget):
    pass

class GitRemoteNode(urwid.ParentNode):
    def __init__(self, remote, **kwargs):
        self._remote = remote
        urwid.ParentNode.__init__(self, remote.name, **kwargs)

    def get_display_text(self):
        return self._remote.name

    def load_widget(self):
        return GitRemoteNodeWidget(self)

    def load_child_keys(self):
        # Return a list of the indices of branches in this remote
        # FIXME: Can probably make a list of names
        return range(len(self._remote.refs))

    def load_child_node(self, key):
        branch = self._remote.refs[key]
        child_depth = self.get_depth() + 1
        # FIXME: We should probably be making "ref" nodes instead of "branches"...
        return gitbranchnode.GitBranchNode(branch, parent=self, key=key, depth=child_depth)
