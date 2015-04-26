# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.animation import Animation

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty
from kivy.core.audio import SoundLoader

#!/usr/bin/kivy
__version__ = '1.0'

# app을 글로벌로 사용
app = None

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''
<Widget>:
    canvas.after:
        Line:
            rectangle: self.x+1,self.y+1,self.width-1,self.height-1
            dash_offset: 2
            dash_length: 3

<Menu>:
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        # orientation: 'vertical' if self.height > self.width else 'horizontal'
        canvas:
            Color:
                rgb: 0x00 / 255., 0x00 / 255., 0x33 / 255.
            # BackGroundColor
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
        BoxLayout:
            orientation: 'vertical' if self.height > self.width else 'horizontal'
            BoxLayout:
            Button:
                text: '시작하기'
                font_name: 'data/NanumGothic.ttf'
                size_hint_y:0.2
            BoxLayout:
                size_hint_y:0.1
            Button:
                text: '끝내기'
                font_name: 'data/NanumGothic.ttf'
                size_hint_y:0.2
            BoxLayout:
        BoxLayout:

''')



class Game(Widget):
    pass


class Menu(Widget):
    pass


class GameApp(App):

    def build(self):
        global app
        app = self

        self.title = 'MarryMe'
        self.menu = Menu()
        return self.menu


if __name__ in ('__main__', '__android__'):
    GameApp().run()

