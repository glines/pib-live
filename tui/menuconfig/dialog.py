import urwid

from menuconfig.buttonbox import ButtonBox
from menuconfig.motif import MotifLineBox

# This file implements a dialog box in the style of Linux's menuconfig
class MenuconfigDialog(urwid.WidgetWrap):
    def __init__(self, hint=None):  # TODO: Pass a root MenuItem as the "model"
        # TODO: Build a Menuconfig widget tree from the given menu item tree "model"


        # Provide a hint at the top of the screen (as in Linux's menuconfig)
        if hint == None:
            # XXX
            hint = u'Arrow keys navigate the menu. Press <space> to perform the selected action. Press <return> to enter submenus --->.\nLegend: <+> some builds selected  <*> all builds selected'
            # hint = u'';
        self._hint = urwid.Text(hint)

        # Make an empty space where the menu (option tree) will go
        menu_items = [
            { 'text': u'Suggested Tests', 'data': None },
            { 'text': u'Select Mesa Builds', 'data': None },
            { 'text': u'Select Piglit Builds', 'data': None },
        ]
        self._menu = []
        for item in menu_items:
            button = urwid.Button(item['text'])
            browser = self
            urwid.connect_signal(button, 'click', self._menu_item_clicked)
            self._menu.append(urwid.AttrMap(button, None, focus_map='focus'))
        self._menu = urwid.ListBox(urwid.SimpleFocusListWalker(self._menu))
        self._menu = MotifLineBox(self._menu, inset=True)
        self._menu = urwid.Padding(self._menu, left=1, right=1)

        # Dynamic buttons for controlling the menu (as in Linux's menuconfig)
        self._button_box = ButtonBox()

        # Place the menu on top and the button box on bottom
        self._main_widget = urwid.Frame(
              self._menu,
              header=self._hint,
              footer=self._button_box,
              focus_part='body'
            )

        # The first button has pseudo focus
        self._button_box.buttons[0].pseudo_focus = True

        urwid.WidgetWrap.__init__(self, self._main_widget)

#    def selectable(self):
#        # I'm thinking it will be easier to simulate double-focus if the dialog
#        # steals all the focus; it is controlling all of the focus
#        return True

    def keypress(self, size, key):
        # TODO: Send up/down key prcesses to the option tree
        # TODO: Send left/right key presses to the button box
        if key in ('left', 'right'):
            return self._button_box.keypress(size, key)
        elif key in ('up', 'down'):
            return self._menu.keypress(size, key)
        return key

    def _menu_item_clicked(self, item):
        # TODO: Maybe make a note that this menu item is in focus?
        pass
