#!/usr/bin/env python2

import os

import urwid

import buildtree
import gitrepobrowser

def top_menu():
    body = [urwid.Text(u'PIAB Top Menu'), urwid.Divider()]
    for item in top_menu_items:
        button = urwid.Button(item[0])
        urwid.connect_signal(button, 'click', top_menu_item_chosen, item)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def top_menu_item_chosen(button, item):
    # We just call the menu callback function
    item[1]()

def recommended_piglit_tests():
    pass  # TODO

def select_mesa_builds():
    # TODO: Get a reference to our Mesa git repository
    rb = gitrepobrowser.GitRepoBrowser(os.path.expanduser('~/repos/mesa'))
    main.original_widget = rb.main_widget
    # TODO: Enumerate the remotes/branches in the git repository
    # TODO: Make tree nodes out of each remote and each branch (we probably
    # want to have a GitRemoteNode and a GitBranchNode for the tree)
    # TODO: Fetch a list of all mesa patches
    # TODO: Make tree nodes for each mesa patch (probably with PatchNode)
#    bb = buildtree.BuildBrowser()
#    main.original_widget = bb.tree_list_box

def phoronix_test_suite():
    pass  # TODO

# TODO: Regression CT Scan

def exit_program():
    raise urwid.ExitMainLoop()

top_menu_items = [
    (u'Recommended Piglit Tests', recommended_piglit_tests),
    (u'Select Mesa Builds', select_mesa_builds),
    (u'Phoronix Test Suite', phoronix_test_suite),
    (u'Quit', exit_program),
]

main = urwid.Padding(top_menu(), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 90),
    valign='middle', height=('relative', 90),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
