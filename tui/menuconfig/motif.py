#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Urwid graphics widgets
#    Copyright (C) 2004-2011  Ian Ward
#
#    Modifications Copyright 2015  Jonathan Glins
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Urwid web site: http://excess.org/urwid/

from urwid import *

class MotifLineBox(LineBox):
    def __init__(self, original_widget, inset=False, title="",
                 tlcorner=u'┌', tline=u'─', lline=u'│',
                 trcorner=u'┐', blcorner=u'└', rline=u'│',
                 bline=u'─', brcorner=u'┘'):

        # Most of LineBox's constructor had to be copied to make these
        # Motif-style shadow modifications
        tline, bline = Divider(tline), Divider(bline)
        lline, rline = SolidFill(lline), SolidFill(rline)
        tlcorner, trcorner = Text(tlcorner), Text(trcorner)
        blcorner, brcorner = Text(blcorner), Text(brcorner)

        if inset:
            tline = AttrWrap(tline, 'shadowed_line')
            lline = AttrWrap(lline, 'shadowed_line')
            bline = AttrWrap(bline, 'lit_line')
            rline = AttrWrap(rline, 'lit_line')
            tlcorner = AttrWrap(tlcorner, 'shadowed_line')
            blcorner = AttrWrap(blcorner, 'shadowed_line')
            trcorner = AttrWrap(trcorner, 'lit_line')
            brcorner = AttrWrap(brcorner, 'lit_line')
        else:
            tline = AttrWrap(tline, 'lit_line')
            lline = AttrWrap(lline, 'lit_line')
            bline = AttrWrap(bline, 'shadowed_line')
            rline = AttrWrap(rline, 'shadowed_line')
            tlcorner = AttrWrap(tlcorner, 'lit_line')
            blcorner = AttrWrap(blcorner, 'lit_line')
            trcorner = AttrWrap(trcorner, 'shadowed_line')
            brcorner = AttrWrap(brcorner, 'shadowed_line')

        self.title_widget = Text(self.format_title(title))
        self.tline_widget = Columns([
            tline,
            ('flow', self.title_widget),
            tline,
        ])

        top = Columns([
            ('fixed', 1, tlcorner),
            self.tline_widget,
            ('fixed', 1, trcorner)
        ])

        middle = Columns([
            ('fixed', 1, lline),
            original_widget,
            ('fixed', 1, rline),
        ], box_columns=[0, 2], focus_column=1)

        bottom = Columns([
            ('fixed', 1, blcorner), bline, ('fixed', 1, brcorner)
        ])

        pile = Pile([('flow', top), middle, ('flow', bottom)], focus_item=1)

        WidgetDecoration.__init__(self, original_widget)
        WidgetWrap.__init__(self, pile)
