import os

from piab.gitmenu.items import (GitRepoMenuItem)
from piab.menuconfig.items import (MenuItem, SubmenuItem)

class PiabTopMenu(MenuItem):
    def __init__(self, *args, **kwargs):
        MenuItem.__init__(self, None, *args, **kwargs)
        child_depth = self.get_depth() + 1
        self._menu_items = []
        self._menu_items.append(
            SuggestedPiglitTestsMenu(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            CustomPiglitTestsMenu(
              parent=self, key=len(self._menu_items), depth=child_depth))

    def get_display_text(self):
        return ''

    def load_child_keys(self):
        return range(len(self._menu_items))

    def load_child_node(self, key):
        return self._menu_items[key]

class SuggestedPiglitTestsMenu(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Run Suggested Piglit Tests'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO

class CustomPiglitTestsMenu(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)
        child_depth = self.get_depth() + 1
        self._menu_items = []
        self._menu_items.append(
            SelectMesaSources(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectMesaPatches(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectPiglitSources(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectPiglitPatches(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectPiglitArguments(
              parent=self, key=len(self._menu_items), depth=child_depth))

    def get_display_text(self):
        return 'Run Custom Piglit Tests'

    def load_child_keys(self):
        return range(len(self._menu_items))

    def load_child_node(self, key):
        return self._menu_items[key]

class SelectMesaSources(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)
        self._repo_paths = [
            os.path.expanduser('~/repos/mesa')
        ]

    def get_display_text(self):
        return 'Select Mesa Sources'

    def load_child_keys(self):
        return range(len(self._repo_paths))

    def load_child_node(self, key):
        child_depth = self.get_depth() + 1
        return GitRepoMenuItem(self._repo_paths[key],
            parent=self, key=key, depth=child_depth)

class SelectMesaPatches(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)
        child_depth = self.get_depth() + 1
        self._menu_items = []
        self._menu_items.append(
            SelectIndividualMesaPatches(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectMesaPatchSets(
              parent=self, key=len(self._menu_items), depth=child_depth))

    def get_display_text(self):
        return 'Select Mesa Patches'

    def load_child_keys(self):
        return range(len(self._menu_items))

    def load_child_node(self, key):
        return self._menu_items[key]

class SelectIndividualMesaPatches(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Select Individual Mesa Patches'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO

class SelectMesaPatchSets(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Select Mesa Patch Sets'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO

class SelectPiglitSources(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)
        self._repo_paths = [
            os.path.expanduser('~/repos/piglit')
        ]

    def get_display_text(self):
        return 'Select Piglit Sources'

    def load_child_keys(self):
        return range(len(self._repo_paths))

    def load_child_node(self, key):
        child_depth = self.get_depth() + 1
        return GitRepoMenuItem(self._repo_paths[key],
            parent=self, key=key, depth=child_depth)

class SelectPiglitPatches(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)
        child_depth = self.get_depth() + 1
        self._menu_items = []
        self._menu_items.append(
            SelectIndividualPiglitPatches(
              parent=self, key=len(self._menu_items), depth=child_depth))
        self._menu_items.append(
            SelectPiglitPatchSets(
              parent=self, key=len(self._menu_items), depth=child_depth))

    def get_display_text(self):
        return 'Select Piglit Patches'

    def load_child_keys(self):
        return range(len(self._menu_items))

    def load_child_node(self, key):
        return self._menu_items[key]

class SelectIndividualPiglitPatches(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Select Individual Piglit Patches'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO

class SelectPiglitPatchSets(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Select Piglit Patch Sets'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO

class SelectPiglitArguments(SubmenuItem):
    def __init__(self, *args, **kwargs):
        SubmenuItem.__init__(self, None, *args, **kwargs)

    def get_display_text(self):
        return 'Select Piglit Arguments'

    def load_child_keys(self):
        return []  # TODO

    def load_child_node(self, key):
        pass  # TODO
