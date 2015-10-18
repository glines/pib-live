from git import Repo

import urwid

from pprint import pprint

import gitremotenode
import optiontreewidget

class GitRepoNodeWidget(optiontreewidget.OptionTreeWidget):
    pass

class GitRepoNode(urwid.ParentNode):
    def __init__(self, repo_path, **kwargs):
        self._repo_path = repo_path
        self._repo = Repo(repo_path)
        urwid.ParentNode.__init__(self, repo_path, **kwargs)
#        self.get_widget().collapse()  # XXX

    def get_display_text(self):
        return self._repo_path

    def load_widget(self):
        return GitRepoNodeWidget(self)

    def load_child_keys(self):
        # Return a list of the names of remotes in this repository
        return map(lambda remote: remote.name, self._repo.remotes)

    def load_child_node(self, key):
        remote = self._repo.remote(name=key)
        child_depth = self.get_depth() + 1
        return gitremotenode.GitRemoteNode(remote, parent=self, key=key, depth=child_depth)
