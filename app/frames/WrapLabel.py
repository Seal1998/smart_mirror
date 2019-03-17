#!/usr/bin/env python
# -*- coding: utf-8 -*-

#by https://gist.github.com/ykmm/9938073

from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.metrics import sp
from kivy.logger import Logger
from kivy.properties import ListProperty, BooleanProperty

class ColorLabel(Label):
    bgcolor = ListProperty([0, 0, 0, 0])
    def __init__(self, **kwargs):
        super(ColorLabel, self).__init__(**kwargs)

        with self.canvas.before:
            r, g, b, a = self.bgcolor
            Color(r, g, b, a)
            self.rect = Rectangle(
                            size=self.size,
                            pos=self.pos)
            self.bind(size=self._update_rect,
                      pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class WrapLabel(ColorLabel):
    """
    A wrapping label

    the text tries to extend as much as possible, text that cannot be displayed is shortened

    if wrap = True the cell extends vertically to show all the content

    width (if passed) defines the maximum width this label is allowed to extend
    """

    wrap = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(WrapLabel, self).__init__(**kwargs)
        self.size_hint = (None, None)
        if 'width' not in kwargs:
            self.width=sp(100)
        if 'height' not in kwargs:
            self.height=sp(18)

        if self.wrap:
            #Constrain horizontally to size of label and free vertically
            self.text_size = (self.width, None)
        else:
            self.text_size = self.size
            self.shorten = True

    def on_texture_size(self,*args):
        Logger.debug('WrapLabel:on_texture_size [%s] texture_size %r size %r text_size %r',
                     self.text[0:5], self.texture_size, self.size, self.text_size)
        if self.wrap:
            self.texture_update()
            self.height = self.texture_size[1]