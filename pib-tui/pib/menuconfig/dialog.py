import urwid

from pib.menuconfig.buttonbox import ButtonBox
from pib.menuconfig.motif import MotifLineBox
from pib.menuconfig.subtreewalker import SubtreeWalker

# This file implements a dialog box in the style of Linux's menuconfig
class MenuconfigDialog(urwid.WidgetWrap):
    def __init__(self, root_menu_item, hint=None):
        self._menu_history = []
        self._root_menu_item = root_menu_item

        # Provide a hint at the top of the screen (as in Linux's menuconfig)
        if hint == None:
            # XXX
            hint = u'Arrow keys navigate the menu. Press <space> to perform the selected action. Press <return> to enter submenus --->.\nLegend: <+> some builds selected  <*> all builds selected'
            # hint = u'';
        self._hint = urwid.Text(hint)

        # Dynamic buttons for controlling the menu (as in Linux's menuconfig)
        self._button_box = ButtonBox()

        # Make a dummy menu widget
        self._menu = urwid.SolidFill('X')
        # Add decoration around the menu
        self._menu = MotifLineBox(self._menu, inset=True)
        self._menu = urwid.Padding(self._menu, left=1, right=1)

        # Build the self._menu "view" from the given root_menu_item "model"
        self._enter_menu(root_menu_item)

        # Place the menu on top and the button box on bottom
        self._main_widget = urwid.Frame(
              self._menu,
              header=self._hint,
              footer=self._button_box,
              focus_part='body'
            )

        urwid.WidgetWrap.__init__(self, self._main_widget)

    def _enter_menu(self, root_menu_item):
        keys = root_menu_item.get_child_keys()
        if len(keys) <= 0:
            return  # Can't enter an empty menu
        self._menu_history.append(root_menu_item)
        self._set_menu(root_menu_item)

    def _back_menu(self, foo=None):  # Eat the button argument
        if len(self._menu_history) <= 1:
            # Don't pop the root menu item
            return
        self._menu_history.pop()
        prev_menu = self._menu_history[-1]
        self._set_menu(prev_menu)

    def _set_menu(self, root_menu_item):
        keys = root_menu_item.get_child_keys()
        first_item = root_menu_item.get_child_node(keys[0])
        self._menu_tree = urwid.TreeListBox(SubtreeWalker(first_item))
        self._menu.original_widget.set_original_widget(self._menu_tree)
        # Now that we're in a different menu, we will have new buttons
        self._update_buttons()
        self._invalidate()

    def _update_buttons(self):
        current_focus = self._menu_tree.get_focus()
        focus_actions = current_focus[0].get_actions()
        menu_actions = []
        if len(self._menu_history) > 1:
            menu_actions.append(('Back', self._back_menu))
        self._button_box.set_actions(
            focus_actions +
            menu_actions
            )
        # Select the first button by default
        if len(self._button_box.buttons) > 0:
            self._button_box.buttons[0].pseudo_focus = True
        

    def keypress(self, size, key):
        if key in ('left', 'right'):
            return self._button_box.keypress(size, key)
        elif key in ('up', 'down', 'page up', 'page down'):
            initial_focus = self._menu_tree.get_focus()
            result = self._menu.keypress(size, key)
            current_focus = self._menu_tree.get_focus()
            if initial_focus[0] is not current_focus[0]:
                self._update_buttons()
            return result
        elif key in (' '):
            # Send space keys to the action in focus in the button box
            return self._button_box.keypress(size, key)
        elif key in ('enter'):
            current_focus = self._menu_tree.get_focus()
            node = current_focus[0].get_node()
            if node.is_submenu():
                self._enter_menu(node)
                return None
            return key
        return key

    def _menu_item_clicked(self, item):
        # TODO: Maybe make a note that this menu item is in focus?
        pass
