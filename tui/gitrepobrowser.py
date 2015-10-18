from git import Repo
import urwid

import gitreponode

class GitRepoBrowser:
    _header_text = u'Press <space> to select or de-select a build. Press <return> to enter submenus --->. Legend: <+> some builds selected  <*> all builds selected'
    _footer_text = u'# of Mesa builds selected: 42   # of Piglit builds selected: 1   # of tests to run: 42 x 1 = 42'
    def __init__(self, repo_path):
        self._repo_path = repo_path
        self._root_node = gitreponode.GitRepoNode(self._repo_path)
        self._root_node = urwid.AttrWrap(self._root_node, 'tree_item', focus_attr='focus')
        self._tree = urwid.TreeListBox(urwid.TreeWalker(self._root_node))
        self._header = urwid.Text(self._header_text)
#        self._header = urwid.Filler(self._header, height='flow', top=0, bottom=1)
        self._header = urwid.Padding(self._header, left=0, right=0)
        self._footer = urwid.Text(self._footer_text)
        self.main_widget = urwid.Frame(
            urwid.AttrWrap(self._tree, 'body'),
            header=self._header,
            footer=self._footer)
            
