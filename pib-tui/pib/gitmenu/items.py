from git import Repo

import urwid

from pib.menuconfig.items import (MenuItem, SubmenuItem, OptionItem, LabelItem, DividerItem)

class GitRepoMenuItem(SubmenuItem):
    def __init__(self, repo_path, *args, **kwargs):
        SubmenuItem.__init__(self, repo_path, *args, **kwargs)
        self._repo_path = repo_path
        self._repo = Repo(repo_path)

    def get_display_text(self):
        return self._repo_path

    def load_child_keys(self):
        # Return a list of the names of remotes in this repository
        remotes = map(lambda remote: remote.name, self._repo.remotes)
        return remotes

    def load_child_node(self, key):
        remote = self._repo.remote(name=key)
        child_depth = self.get_depth() + 1
        child_node = GitRemoteMenuItem(remote, parent=self, key=key, depth=child_depth)
        return child_node

class GitRemoteMenuItem(OptionItem):
    def __init__(self, remote, *args, **kwargs):
        OptionItem.__init__(self, remote, *args, **kwargs)
        self._remote = remote

    def get_display_text(self):
        return self._remote.name

    def load_child_keys(self):
        # Return a list of the indices of refs in this remote
        try:
            refs = self._remote.refs
        except AssertionError:
            # GitPython does not handle remotes without any refs very
            # gracefully
            refs = []
        return range(len(refs))

    def load_child_node(self, key):
        ref = self._remote.refs[key]
        child_depth = self.get_depth() + 1
        child_node = GitRefMenuItem(ref, parent=self, key=key, depth=child_depth)
        return child_node

class GitRefMenuItem(OptionItem):
    def __init__(self, ref, *args, **kwargs):
        OptionItem.__init__(self, ref, *args, **kwargs)
        self._ref = ref

    def get_display_text(self):
        return "{}    {}".format(self._ref.name, self._ref.commit.summary)

    def load_child_keys(self):
        return []

    def load_child_node(self, key):
        pass
