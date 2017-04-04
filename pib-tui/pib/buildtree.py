import urwid

class BuildTreeWidget(urwid.TreeWidget):
    def get_display_text(self):
        return str(self.get_node().get_value()['text'])

    def selectable(self):
        # All nodes are selectable
        return True

    def get_indented_widget(self):
        widget = self.get_inner_widget()
        # Apply indentation padding first; the check boxes appear on the far
        # left, as in Linux's "menuconfig" that many people are familiar with
        indent_cols = self.get_indent_cols()
        widget = urwid.Padding(widget, width=('relative', 100), left=indent_cols)
        if self.is_leaf:
            # Leaf nodes have square brackets
            widget = urwid.Columns([('fixed', 3, urwid.SelectableIcon(u'[ ]')), widget], dividechars=1)
        else:
            # Non-leaf nodes have angle brackets to suggest a hierarchy
            widget = urwid.Columns([('fixed', 3, urwid.SelectableIcon(u'< >')), widget], dividechars=1)
        return widget

class BuildNodeWidget(BuildTreeWidget):
    # FIXME: Rename these to unselected_icon and selected_icon
    unexpanded_icon = urwid.SelectableIcon('[ ]', 0)
    expanded_icon = urwid.SelectableIcon('[*]', 0)

class BuildParentNodeWidget(BuildTreeWidget):
    # FIXME: Rename these to unselected_icon and selected_icon
    unexpanded_icon = urwid.SelectableIcon('< >', 0)
    expanded_icon = urwid.SelectableIcon('<*>', 0)

class BuildNode(urwid.TreeNode):
    def load_widget(self):
        return BuildNodeWidget(self)

class BuildParentNode(urwid.ParentNode):
    def __init__(self, *args, **kwargs):
        urwid.ParentNode.__init__(self, *args, **kwargs)
        self.get_widget().expanded = False

    def get_display_text(self):
        return str(self.get_node().get_value())

    def load_widget(self):
        return BuildParentNodeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        return range(len(data['children']))

    def load_child_node(self, key):
        child_value = self.get_value()['children'][key]
        if 'children' in child_value:
            child_class = BuildParentNode
        else:
            child_class = BuildNode
        child_depth = self.get_depth() + 1
        return child_class(child_value, parent=self, key=key, depth=child_depth)

test_tree = {
'text': 'Mesa Builds', 'children': [
  {'text': 'Mesa patches (from https://patchwork.freedesktop.org/)', 'children': [
    {'text': '[Mesa-dev] r600g: Implement ARB_texture_view'},
    {'text': '[Mesa-dev 7 patches] Patchset 2015-10-15 by Timothy Arceri', 'children': [
      {'text': '[Mesa-dev,1/7] nir: wrapper for glsl_type arrays_of_arrays_size()'},
      {'text': '[Mesa-dev,2/7] nir: add atomic lowering support for AoA'},
      {'text': '[Mesa-dev,3/7] glsl: add AoA support to subroutines'},
      {'text': '[Mesa-dev,4/7] glsl: set image access qualifiers for AoA'},
      {'text': '[Mesa-dev,5/7] i965: add support for image AoA'},
      {'text': '[Mesa-dev,6/7] i965: enable ARB_arrays_of_arrays'},
      {'text': '[Mesa-dev,7/7] docs: Mark AoA as done for i965'},
    ]},
  ]},
  {'text': 'Mesa Git Repositories (from http://cgit.freedesktop.org/)', 'children': [
    {'text': '~ab/mesa   Andreas\' mesa work'},
    {'text': '~abj/mesa   Abj\'s mesa experiments'},
    {'text': '~airlied/mesa   Dave\'s mesa hackery', 'children': [
      {'text': 'arb_gpu_shader_fp64-fixes  :  fixup left comps for 2'},
      {'text': 'arb_gpu_shader_fp64_fixes-2  :  st/glsl_to_tgsi: fix block movs for doubles'},
      {'text': 'arb_gpu_shader_int64  :  fixup lexer bits from Ilia'},
      {'text': 'cts-hacks  :  HACK: drop a load of fallbacks pixelstore CTS'},
      {'text': 'cts-swap-bytes-fixes  :  mesa/formats: 8-bit channel integer formats addition'},
      {'text': 'r600-arb_gpu_shader5  :  r600g: fixups'},
    ]},
  ]},
]}

class BuildBrowser:
    def __init__(self):
        self.root_node = BuildParentNode(test_tree)
        self.tree_list_box = urwid.TreeListBox(urwid.TreeWalker(self.root_node))
