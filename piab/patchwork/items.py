from piab.menuconfig.items import (OptionItem, SubmenuItem)

class PatchworkMenuItem(SubmenuItem):
    def __init__(self, url, project, *args, **kwargs):
        SubmenuItem.__init__(self, project, *args, **kwargs)
        self._url = url
        self._project = project

    def get_display_text(self):
        return self._project

    def _get_patch_list
        if self._patch_list is None:
            self._patch_list = self._fetch_patch_list()

    def _fetch_patch_list():
        # TODO: fetch the patch list (and cache it on the disk)
        pass

    def load_child_keys(self):
        # Return a list of the patches
