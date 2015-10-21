import os

import urwid

import buildbrowser
import motiflinebox

class PiglitTestBrowser:
    # TODO: Add a menu entry for selecting mesa builds
    # TODO: Add a menu entry for selecting piglit builds
    def __init__(self):
        self._mesa_build_browser = buildbrowser.BuildBrowser(
            git_repo_path=os.path.expanduser('~/repos/mesa'),
            patchwork_url='https://patchwork.freedesktop.org/xmlrpc/',
            patchwork_project='mesa')
#        self._piglit_build_browser = buildbrowser.BuildBrowser(
#            git_repo_path=os.path.expanduser('~/repos/piglit'),
#            patchwork_url='https://patchwork.freedesktop.org/xmlrpc/',
#            patchwork_project='piglit')
        # TODO: The test browser widget itself is a list of build types
        # (BuildBrowsers) that can be explored as submenus. All possible build
        # combinations (i.e. the "cartesian product" of all builds) are made into
        # tests.

        # Build the menu
        menu_items = [
            { 'text': u'Suggested Tests', 'callback': self.suggested_tests },
            { 'text': u'Select Mesa Builds', 'callback': self.select_mesa_builds },
            { 'text': u'Select Piglit Builds', 'callback': self.select_piglit_builds },
        ]
        self._menu = []
        for item in menu_items:
            button = urwid.Button(item['text'])
            browser = self
            urwid.connect_signal(button, 'click', item['callback'])
            self._menu.append(urwid.AttrMap(button, None, focus_map='focus'))
        self._menu = urwid.ListBox(urwid.SimpleFocusListWalker(self._menu))
        self._menu = motiflinebox.MotifLineBox(self._menu, inset=True)
        self._menu = urwid.Padding(self._menu, left=1, right=1)

        # Add <Select>, <Details>, <Start>, and <Exit> buttons to the bottom
        def make_button(name):
            result = urwid.Button(name)
            result = urwid.AttrMap(result, 'button', focus_map='button_focus')
            return result
        self._select_button = make_button(u'Select')
        self._details_button = make_button(u'Details')
        self._back_button = make_button(u'Back')
        self._button_box = urwid.Columns([
              self._select_button,
              self._details_button,
              self._back_button,
            ], dividechars=3, min_width=(8))
        self._button_box = urwid.Padding(self._button_box,
            align='center', width=55)
        self._button_box = motiflinebox.MotifLineBox(self._button_box)

        self.widget = urwid.Frame(
              self._menu,
              footer=self._button_box,
            )

    def suggested_tests(self, button):
        pass  # TODO: somehow swap the current widget out?

    def select_mesa_builds(self, button):
        self._menu.original_widget = motiflinebox.MotifLineBox(self._mesa_build_browser.widget, inset=True)

    def select_piglit_builds(self, button):
        pass  # TODO: somehow swap the current widget out?

    def get_tests(self):
        # TODO: Compute the cartesian product of all selected Mesa and Piglet builds
        build_product = []
        for mesa_build in self._mesa_build_browser.get_builds():
            for piglit_build in self._piglit_build_browser.get_builds():
                build_product.append({
                    'mesa_build': mesa_build,
                    'piglit_build': piglit_build })
        # TODO: Combine these into tests?
