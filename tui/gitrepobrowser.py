from git import Repo
import urwid

import gitreponode

class GitRepoBrowser:
    def __init__(self, repo_path):
        self._repo_path = repo_path
        self._root_node = gitreponode.GitRepoNode(self._repo_path)
        self.main_widget = urwid.TreeListBox(urwid.TreeWalker(self._root_node))
