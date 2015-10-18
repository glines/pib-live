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
    body = urwid.ListBox(urwid.SimpleFocusListWalker(body))
    body = urwid.AttrWrap(body, 'body')
    return body

def shadow(widget):
    # Models the shadow after the Linux kernel's menuconfig
    background = urwid.AttrWrap(urwid.SolidFill(u' '), 'background')
    shadow = urwid.AttrWrap(urwid.SolidFill(u' '), 'shadow')
    result = urwid.Overlay(shadow, background,
        ('fixed left', 4), ('fixed right', 1),
        ('fixed top', 3), ('fixed bottom', 1))
    result = urwid.Overlay(widget, result,
        ('fixed left', 2), ('fixed right', 3),
        ('fixed top', 2), ('fixed bottom', 2))

    return result

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

palette = [
    ('body', 'black', 'light gray'),
    ('background', 'default', 'dark blue'),
    ('shadow', 'black', 'black'),
    ('tree_item', 'light gray', 'black'),
    ('focus', 'dark cyan', 'black', 'standout'),
]

main = top_menu()
top = shadow(main)
urwid.MainLoop(top, palette=palette).run()
