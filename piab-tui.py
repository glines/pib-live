#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os

import urwid

import piab.buildtree
import piab.gitrepobrowser
import piab.piglittestbrowser
import piab.menuconfig

def top_menu():
    body = [urwid.Text(u'PIAB Top Menu'), urwid.Divider()]
    for item in top_menu_items:
        button = urwid.Button(item[0])
        urwid.connect_signal(button, 'click', top_menu_item_chosen, item)
        body.append(urwid.AttrMap(button, None, focus_map='focus'))
    body = urwid.ListBox(urwid.SimpleFocusListWalker(body))
    body = urwid.AttrWrap(body, 'body')
    return body

def shadow(widget, title=None):
    # Models the shadow after the Linux kernel's menuconfig
    if title:
        background = urwid.Pile([
            urwid.Text(title),
            urwid.Divider(u'─'),
            ])
        background = urwid.Filler(background)
        background = urwid.Overlay(background, urwid.SolidFill(u' '),
            align='center', width=('relative', 100), valign='top', height=2)
        background = urwid.AttrWrap(background, 'background')
    else:
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
    # XXX
    mc = piab.menuconfig.MenuconfigDialog(None)
    main.original_widget = mc

def select_piglit_tests():
    test_browser = piab.piglittestbrowser.PiglitTestBrowser()
    main.original_widget = test_browser.widget
    # TODO: Get a reference to our Mesa git repository
#    rb = gitrepobrowser.GitRepoBrowser(os.path.expanduser('~/repos/mesa'))
#    main.original_widget = rb.main_widget
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
    (u'Start Recommended Piglit Tests', recommended_piglit_tests),
    (u'Select Custom Piglit Tests', select_piglit_tests),
    (u'Phoronix Test Suite', phoronix_test_suite),
    (u'Quit', exit_program),
]

palette = [
    ('body', 'black', 'light gray'),
    ('background', 'light cyan', 'dark blue'),
    ('shadow', 'black', 'black'),
    ('tree_item', 'black', 'light gray'),
    ('focus', 'white', 'dark blue'),
    ('shadowed_line', 'black', 'light gray'),
    ('lit_line', 'white', 'light gray'),
    ('button', 'black', 'light gray'),
    ('button_focus', 'white', 'dark blue'),
]

main = top_menu()
top = shadow(main, title=u'Pigs In A Blanket Pre-Alpha')
urwid.MainLoop(top, palette=palette).run()
