# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.animation import Animation

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, ReferenceListProperty

from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage


# ScreenManager
from kivy.uix.screenmanager import ScreenManager, Screen

# BorderImage
# from kivy.graphics import Color, BorderImage
from kivy.graphics import Rectangle

# move
from kivy.vector import Vector

# random respon
import random

from kivy.uix.screenmanager import WipeTransition

from math import sin

#!/usr/bin/kivy
__version__ = '1.0'

# app을 글로벌로 사용
from kivy.app import App
app = None

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
<Widget>:
    canvas.after:
        Line:
            rectangle: self.x+1,self.y+1,self.width-1,self.height-1
            dash_offset: 2
            dash_length: 3

<EndScreen>:
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        # orientation: 'vertical' if self.height > self.width else 'horizontal'
        canvas:
            Color:
                rgb: 218/255., 204/255., 175/255., 1
            # BackGroundColor
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_x:0.1
        BoxLayout:
            size_hint_x:0.2
            orientation: 'vertical' if self.height > self.width else 'horizontal'
            BoxLayout:
            Label:
                text: "당신의 점수는 무려 %s 점" % root.score
                font_size: 80
                font_name: 'data/NanumGothic.ttf'
            Button:
                text: 'Re Start'
                background_color: 122/255., 101/255., 54/255., 1
                font_name: 'data/NanumGothic.ttf'
                size_hint_y:0.2
                on_press: root.manager.transition = WipeTransition(); root.manager.current = 'character screen'
            BoxLayout:
                size_hint_y:0.1
            Button:
                text: 'End'
                background_color: 122/255., 101/255., 54/255., 1
                font_name: 'data/NanumGothic.ttf'
                size_hint_y:0.2
            BoxLayout:
        BoxLayout:
            size_hint_x:0.1

<MenuScreen>:
    Image:
    #    source: 'data/colored_land.png'
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        # orientation: 'vertical' if self.height > self.width else 'horizontal'
        BoxLayout:
            size_hint_x:0.1
        BoxLayout:
            size_hint_x:0.2
            orientation: 'vertical' if self.height > self.width else 'horizontal'
            BoxLayout:
            Label:
                text: 'Summer Wedding Run'
                font_size: 60
                font_name: 'data/PH-600RegularCaps.otf'
                color: (0, 0, 0, 1)
            Button:
                text: 'Start'
                background_color: 0/255., 140/255., 140/255., 1
                font_name: 'data/PH-600RegularCaps.otf'
                size_hint_y:0.2
                on_press: root.manager.transition = WipeTransition(); root.manager.current = 'game screen'
            BoxLayout:
                size_hint_y:0.1
            # Button:
            #    text: '안먹는 버튼'
            #    background_color: 122/255., 101/255., 54/255., 1
            #    font_name: 'data/NanumGothic.ttf'
            #    size_hint_y:0.2
            BoxLayout:
        BoxLayout:
            size_hint_x:0.1

<Brick>:
    size: brick_image.width, brick_image.height
    center: root.center
    Image:
        id: brick_image
        source: 'data/box2.png'
        center: root.center
        size: root.block_size, root.block_size
<Sign>:
    size: brick_image.width, brick_image.height
    center: root.center
    Image:
        id: brick_image
        source: 'data/signRight.png'
        center: root.center
        size: root.block_size, root.block_size
<Monster>:
    size: monster_image.width, monster_image.height
    center: root.center
    Image:
        id: monster_image
        source: root.source_dir
        center: root.center
        size: root.block_size, root.block_size

# <Princess>:
#     size: player_image.width, player_image.height
#     Image:
#         id: player_image
#         source: 'data/girl64.png'
#         center: root.center
#         size: 64, 64
#     Image:
#         source: 'data/laserBlue2.png'
#         x: player_image.x
#         y: player_image.y - 100
#         size: 64, 100
#         opacity: 0.5
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'

<Character>:
    player_image:player_image

    size: player_image.width-10, player_image.height-10
    Image:
        id: player_image
        source: 'data/angel.png' if root.is_man else 'data/knight.png'
        center: root.center
        size: root.block_size, root.block_size
        allow_stretch: True
    Label:
        text: root.comment
        size: 200, 20,
        pos: root.x - 15, root.center_y + 30
        font_size: 15
        font_name: 'data/NanumGothic.ttf'
        color: (0, 0, 0, 1)


# <Monster>:
#     size: monster_image.width/2, monster_image.height/2
#     Image:
#         id: monster_image
#         source: 'data/spinner.png'
#         center: root.center
#         size: root.block_size, root.block_size
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'

<Trap>
    size: trap_image.width/2, trap_image.height/2
    Image:
        id: trap_image
        source: 'data/spikes.png'
        center: root.center
        size: root.block_size, root.block_size
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'


<GameWidget>:
    # princess: princess
    character: character
    background_widget: background_widget
    tip_label: tip_label

    Widget:
        id: background_widget
        pos: self.parent.pos
        size: self.parent.size

    # Princess:
    #     id: princess
        # pos: root.center
        # Label:
        #    # text: "%s" % self.parent.size
        #    pos: self.parent.pos
        #    size: self.parent.size
    Character:
        id: character
        # pos: root.center
        # Label:
        #    # text: "%s" % self.parent.size
        #    pos: self.parent.pos
        #    size: self.parent.size
    Label:
        id: tip_label
        text: root.tip
        font_size: 40
        font_name: 'data/NanumGothic.ttf'
        center: [root.center[0], root.center[1]+40]
        size: 100, 40
        color: (0, 0, 0, 1)

    Label:
        text: root.tip2
        font_size: 20
        font_name: 'data/NanumGothic.ttf'
        center: [root.center[0], root.center[1]]
        size: 100, 40
        color: (0, 0, 0, 1)

    Label:
        text: "%s초" % root.time
        font_size: 80
        font_name: 'data/NanumGothic.ttf'
        center: [root.center[0], root.center[1] + 120]
        size: 100, 40
        color: (0, 0, 0, 1)

    Label:
        text: "STAGE: %s" % root.stage
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-120
        color: (0, 0, 0, 1)

    Label:
        text: "Score: %s" % root.score
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-40
        color: (0, 0, 0, 1)

    Label:
        text: 'FPS: ' + root.fps if root.fps != None else 'FPS:'
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-80
        size: 100, 40
        halign: 'right'
        color: (0, 0, 0, 1)

    # Enemy:
    #    id: enemy
    #    pos: root.center
    #    Label:
    #        text: "%s" % self.parent.size
    #        pos: self.parent.pos

# GameScreen
<GameScreen>:
    game_widget: game_widget
    control_widget_a: control_widget_a
    control_widget_b: control_widget_b
    left_button: left_button
    right_button: right_button
    a_button: a_button
    # b_button: b_button

    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        GameWidget:
            size_hint_y:0.7
            id: game_widget
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y:0.3
            ControlWidget:
                id: control_widget_a
                Image:
                    id: left_button
                    center: self.parent.x + self.width + 25, self.parent.center_y
                    size: 100, 100
                    source: 'data/lineDark19.png'
                Image:
                    id: right_button
                    size: 100, 100
                    center: self.parent.x + self.width + 175, self.parent.center_y
                    source: 'data/lineDark20.png'
            ControlWidget:
                id: control_widget_b
                Image:
                    id: a_button
                    size: 100, 100
                    center: root.width - self.width - 25, self.parent.center_y
                    source: 'data/lineDark31.png'
                # Image:
                #     id: b_button
                #     size: 100, 100
                #     center: root.width - self.width - 175, self.parent.center_y
                #     source: 'data/lineDark32.png'
''')

# WIDGETS


# class Princess(Widget):
#     velocity_x = 0
#     velocity_y = 0
#     velocity = [0, 0]
#     comment = StringProperty("")
#
#     def move(self):
#         self.center = Vector(*self.velocity) + self.center
#
#     def stop(self):
#         self.velocity = [0, 0]


class Character(Widget):
    velocity_x = 0
    velocity_y = 0
    velocity = [0, 0]
    comment = StringProperty("")
    is_man = NumericProperty(0)
    block_size = NumericProperty(64)

    def move(self):
        self.center = Vector(*self.velocity) + self.center


class Brick(Widget):
    block_size = NumericProperty(64)
    pass


class Sign(Widget):
    block_size = NumericProperty(64)
    pass


class Enemy(Widget):
    block_size = NumericProperty(64)
    pass


class Monster(Widget):
    block_size = NumericProperty(64)
    status = 0
    source_dir = StringProperty("")

    def init_image_dir(self):
        if self.status == 1:
            self.source_dir = "data/cherry.png"
        elif self.status == 2:
            self.source_dir = "data/mouse.png"
        elif self.status == 4:
            self.source_dir = "data/springboardUp.png"
        elif self.status == 5:
            self.source_dir = "data/sandRing.png"
        elif self.status == 6:
            self.source_dir = "data/flagSilver.png"
        elif self.status == 7:
            self.source_dir = "data/flagRed.png"
        elif self.status == 8:
            self.source_dir = "data/coinGold.png"
        elif self.status == 9:
            self.source_dir = "data/spider.png"
        elif self.status == 10:
            self.source_dir = "data/angel.png"
        elif self.status == 11:
            self.source_dir = "data/knight.png"

        # Letter
        elif self.status == 12:
            self.source_dir = "data/letterC.png"
        elif self.status == 13:
            self.source_dir = "data/letterO.png"
        elif self.status == 14:
            self.source_dir = "data/letterN.png"
        elif self.status == 15:
            self.source_dir = "data/letterG.png"
        elif self.status == 16:
            self.source_dir = "data/letterR.png"
        elif self.status == 17:
            self.source_dir = "data/letterA.png"
        elif self.status == 18:
            self.source_dir = "data/letterT.png"
        elif self.status == 19:
            self.source_dir = "data/letterU.png"
        elif self.status == 20:
            self.source_dir = "data/letterL.png"
        elif self.status == 21:
            self.source_dir = "data/letterI.png"


class Trap(Widget):
    block_size = NumericProperty(64)
    pass


class MenuScreen(Screen):
    pass


class ControlWidget(Widget):
    pass

# STAGE DEFINE
# 64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768 (12)
# BOX - 64 x 64


# STAGE 0
STAGE0_BRICKS = []
STAGE0_SIGNS = []
STAGE0_MONSTERS = []
STAGE0_TRAPS = []

# STAGE 1
STAGE1_BRICKS = []
STAGE1_SIGNS = [[-6, 0]]
STAGE1_MONSTERS = []
STAGE1_TRAPS = []

# STAGE 2
STAGE2_BRICKS = [[-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0],
                 [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0],
                 [-5, 1], [-4, 1], [-3, 1], [-2, 1], [-1, 1],
                 [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1],
                 [-4, 2], [-3, 2], [-2, 2], [-1, 2],
                 [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [6, 1]
                 ]
STAGE2_SIGNS = []  # [[3, 3]]
STAGE2_MONSTERS = [
    # MAP
    [8, 0, 4],
    # GOLD RING
    [10, 0, 5],
    [11, 0, 5],
    [9, 0, 5],
    [8, 1, 5],
    [8, 2, 5],
    [7, 3, 5],
    [7, 4, 5],
    [6, 4, 5],
    [6, 3, 5],
    [5, 5, 5],
    [4, 4, 5],
    [3, 3, 5],
    [2, 3, 5],
    [1, 3, 5],
    [0, 4, 5],
    [-1, 5, 5],
    [-2, 4, 5],
    [-3, 5, 5],
    [-4, 4, 5],
    [-5, 5, 5],
    [-6, 4, 5],
    [-7, 3, 5],
    [-8, 2, 5],
    [-9, 1, 5],
    [-10, 0, 5],
    [-11, 0, 5],
]
STAGE2_TRAPS = []

# STAGE 3
STAGE3_BRICKS = [[2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                 [3, 1], [4, 1], [5, 1], [6, 1], [7,
                                                  1],
                 [4, 2], [5, 2], [6, 2], [7,
                                          2],
                 [5, 3], [6, 3], [7, 3],
                 [6, 4], [7, 4],
                 [7, 5],
                 [10, 0],
                 ]
STAGE3_SIGNS = []
STAGE3_MONSTERS = [
    [-10, 0, 8], [-9, 1, 8], [-8, 2, 8], [-7, 1, 8], [-6, 0, 8],
    [-5, 0, 8], [-4, 1, 8], [-3, 2, 8], [-2, 1, 8], [-1, 0, 8],


    [10, 1, 6], [10, 2, 6], [10, 3, 6], [10, 4, 6], [10, 5, 6], [10, 6, 7]]
STAGE3_TRAPS = []

# STAGE 4
STAGE4_BRICKS = []
STAGE4_SIGNS = []
STAGE4_MONSTERS = [
    # chu
    [-8, 3, 8],
    [-10, 2, 8], [-9, 2, 8], [-8, 2, 8], [-7, 2, 8], [-6, 2, 8],
    [-10, 0, 8], [-9, 1, 8], [-7, 1, 8], [-6, 0, 8],

    # cha
    [-4, 3, 8], [-3, 3, 8], [-2, 3, 8], [-1, 3, 8],
    [-1, 2, 8],
    [-4, 1, 8], [-3, 1, 8], [-2, 1, 8], [-1, 1, 8],
    [-1, 0, 8],

    # chu
    [3, 3, 5],
    [1, 2, 5], [2, 2, 5], [3, 2, 5], [4, 2, 5], [5, 2, 5],
    [1, 0, 5], [2, 1, 5], [4, 1, 5], [5, 0, 5],

    # cha
    [7, 3, 5], [8, 3, 5], [9, 3, 5], [10, 3, 5],
    [10, 2, 5],
    [7, 1, 5], [8, 1, 5], [9, 1, 5], [10, 1, 5],
    [10, 0, 5],
]
STAGE4_TRAPS = []

# STAGE 5 - 챕터2
STAGE5_BRICKS = []
STAGE5_SIGNS = []  # [[1, 0]]
STAGE5_MONSTERS = [[-3, 0, 2], [0, 0, 2], [3, 0, 9], [7, 0, 10]]
STAGE5_TRAPS = []

# STAGE 6 - AVOID MONSTER WITH BLOCK
STAGE6_BRICKS = []
STAGE6_SIGNS = []  # [[1, 0]]
STAGE6_MONSTERS = [[-5, 0, 12], [-4, 0, 13], [-3, 0, 14], [-2, 0, 15], [-1, 0, 16],
                   [0, 0, 17], [1, 0, 18], [2, 0, 19], [3, 0, 20], [4, 0, 17], [5, 0, 21], [6, 0, 13], [7, 0, 14]]
STAGE6_TRAPS = []

# STAGE 7
STAGE7_BRICKS = []
STAGE7_SIGNS = []
STAGE7_MONSTERS = []
STAGE7_TRAPS = []

# STAGE 8
STAGE9_BRICKS = []
STAGE9_SIGNS = []  # [[1, 0]]
STAGE9_MONSTERS = [[-6, 0, 1], [-5, 0, 1], [-4, 0, 1], [-3, 0, 1], [-2, 0, 1], [-1, 0, 1],
                   [0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [
                       4, 0, 1], [5, 0, 1], [6, 0, 1],
                   [-5, 1, 1], [-4, 1, 1], [-3, 1, 1], [-2, 1, 1], [-1, 1, 1],
                   [0, 1, 1], [1, 1, 1], [2, 1, 1], [
                       3, 1, 1], [4, 1, 1], [5, 1, 1],
                   [-4, 2, 1], [-3, 2, 1], [-2, 2, 1], [-1, 2, 1],
                   [0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1], [
    4, 2, 1], [5, 2, 1], [6, 2, 1], [6, 1, 1]
]
STAGE9_TRAPS = []

# STAGE 9
STAGE8_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                 [0, 0], [1, 0], [2, 0],
                 [5, 0], [6, 0]]
STAGE8_SIGNS = []  # [[1, 0]]
STAGE8_MONSTERS = []
STAGE8_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 10
STAGE10_BRICKS = [[-6, 0], [-5, 0], [-4, 0], [-2, 0],
                  [0, 0],  [2, 0], [4, 0], [5, 0], [6, 0],
                  [-5, 1], [-4, 1],  [-2, 1],
                  [0, 1],  [2, 1], [4, 1], [5, 1],
                  [-4, 2],  [-2, 2],
                  [0, 2], [2, 2], [4, 2]]
STAGE10_SIGNS = []
STAGE10_MONSTERS = []
STAGE10_TRAPS = [[-3, 0], [-1, 0], [1, 0], [3, 0]]

# STAGE 11
STAGE11_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE11_SIGNS = []  # [[1, 0]]
STAGE11_MONSTERS = []
STAGE11_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 12
STAGE12_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE12_SIGNS = []  # [[1, 0]]
STAGE12_MONSTERS = []
STAGE12_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 13
STAGE13_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE13_SIGNS = []  # [[1, 0]]
STAGE13_MONSTERS = []
STAGE13_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 14
STAGE14_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE14_SIGNS = []  # [[1, 0]]
STAGE14_MONSTERS = []
STAGE14_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 15
STAGE15_BRICKS = []
STAGE15_SIGNS = []
STAGE15_MONSTERS = []
STAGE15_TRAPS = []

# STAGE 16
STAGE16_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE16_SIGNS = []  # [[1, 0]]
STAGE16_MONSTERS = []
STAGE16_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 17
STAGE17_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE17_SIGNS = []  # [[1, 0]]
STAGE17_MONSTERS = []
STAGE17_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 18
STAGE18_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE18_SIGNS = []  # [[1, 0]]
STAGE18_MONSTERS = []
STAGE18_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 19
STAGE19_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE19_SIGNS = []  # [[1, 0]]
STAGE19_MONSTERS = []
STAGE19_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 20
STAGE20_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE20_SIGNS = []  # [[1, 0]]
STAGE20_MONSTERS = []
STAGE20_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]


TIME_UP = 60


class GameWidget(Widget):
    fps = StringProperty(None)
    # princess = None
    character = None

    bricks = []
    signs = []
    monsters = []
    traps = []
    score = NumericProperty(0)
    stage = NumericProperty(0)
    tip = StringProperty("")
    tip2 = StringProperty("")
    tip_label = ObjectProperty()

    is_start = False
    is_invincible = True

    # Princess's Move
    # is_touch = False
    # touch = None

    # Character's Move
    is_key_down = False
    is_jumping = False
    is_ycoll = False

    player_label = ObjectProperty(None)
    control_widget_a = None
    control_widget_b = None

    # timer
    time_limit = 0
    time = NumericProperty(0.1)

    block_size = NumericProperty(64)

    # Speed
    speed_ratio = 12

    def update_time(self, dt):
        self.time -= 0.1
        if self.time <= 0:
            self.init_stage()

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))

    def init_stage(self):
        """ when game failed """
        self.is_start = True

        # time
        self.time = self.time_limit
        self.character_pos_init()

        # re position princess
        # self.princess.pos = [self.width - self.princess.width - 20, self.y]

    def character_pos_init(self):
        self.character.player_image.size = [self.block_size, self.block_size]

        if self.character.is_man == 0:
            self.character.pos = [self.x + 20, self.y]
            self.character.velocity = [self.block_size / self.speed_ratio, 0]
        else:
            self.character.velocity = [-self.block_size / self.speed_ratio, 0]
            self.character.pos = [
                self.width - self.character.width - 20, self.y]

    def clear_stage(self):
        """ when game cleard """
        # 오브젝트 삭제
        for b in self.bricks:
            self.remove_widget(b)
        self.bricks = []
        for m in self.monsters:
            self.remove_widget(m)
        self.monsters = []
        for s in self.signs:
            self.remove_widget(s)
        self.signs = []
        for t in self.traps:
            self.remove_widget(t)
        self.traps = []

        # self.princess.pos = [self.width - self.princess.width - 20, self.y]

        self.stage += 1

        self.bring_stage()

        if self.stage % 2 == 1:
            self.character.velocity = [self.block_size / self.speed_ratio, 0]
            self.character.is_man = 0
        else:
            self.character.velocity = [-self.block_size / self.speed_ratio, 0]
            self.character.is_man = 1

        self.character_pos_init()

        self.time = self.time_limit

    def init_game(self, ca, cb):

        # start
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_interval(self.update_fps, .1)
        Clock.schedule_interval(self.update_time, .1)
        # Clock.schedule_interval(self.test, 5)
        # Clock.schedule_once(self.test, 1)
        Clock.schedule_interval(self.txupdate, 1.0 / 60.0)

        # bring stage
        self.bring_stage()

        self.character.velocity = [self.block_size / self.speed_ratio, 0]

        # map init
        with self.background_widget.canvas:
            texture = CoreImage('data/blue_land.png').texture
            texture.wrap = 'repeat'
            self.rect_1 = Rectangle(
                texture=texture, size=self.size, pos=self.pos)

        # controller
        self.control_widget_a = ca
        self.control_widget_b = cb

        self.init_stage()

    def character_x_collision(self, brick):
        if self.character.x < brick.x:
            self.character.x = brick.x - self.character.width - 3
        else:
            self.character.x = brick.x + brick.width + 3

    def character_y_collision(self, brick):
        if self.character.y > brick.y:
            self.character.y = brick.y + brick.height
            return True
        else:
            self.character.y = brick.y - self.character.height
            return False

    def update(self, dt):
        """ 게임업데이트 """

        if not self.is_start:
            return

        # Princess's Move
        # if self.is_touch:
        #     self.princess.move()
        #     self.on_touch_down(self.touch)

        self.is_ycoll = False

        # Character's Move
        for brick in self.bricks:

            # meet Block
            if self.character.collide_widget(brick):
                z = Vector(self.character.center) - Vector(brick.center)

                if -0.70 < z.normalize()[0] < 0.70:
                    # down
                    if self.character_y_collision(brick):
                        self.is_jumping = False
                        self.is_ycoll = True
                else:
                    self.character_x_collision(brick)

        self.character.move()

        # y 충돌이면 떨어지지 않는다. // 표면보다 같거나 낮으면 떨어지지 않는다.
        if not self.is_ycoll and not self.character.y <= self.y:
            self.character.y -= 5.0

        # floor
        if self.character.y <= self.y and self.is_jumping:
            self.is_jumping = False
            self.character.y = self.y

        # next stage
        if self.character.center_x > self.width or self.character.center_x < 0:
            self.clear_stage()

        # monster
        for monster in self.monsters:
            if self.character.collide_widget(monster):

                if monster.status == 1:  # Food
                    anim = Animation(
                        size=[self.character.player_image.width * 1.2, self.character.player_image.height * 1.2], duration=.2)
                    if anim:
                        anim.stop(self.character.player_image)
                        anim.start(self.character.player_image)
                    # remove monster
                    self.remove_widget(monster)
                    self.monsters.remove(monster)

                elif monster.status == 2:  # Enemy
                    monster.source_dir = "data/mouse_dead.png"
                    monster.status = 3

                    left = Animation(
                        center_x=monster.center_x + 10, duration=.2)
                    right = Animation(center_x=monster.center_x, duration=.2)
                    anim = left + right
                    if anim:
                        anim.stop(self)
                    anim.start(monster)

                elif monster.status == 9:  # Boss
                    monster.source_dir = "data/spider_dead.png"
                    monster.status = 3

                elif monster.status == 10:  # Girl
                    self.character.velocity = [0, 0]
                    self.character.y += 6
                    monster.y += 1
                    if self.center[1] < self.character.y:
                        self.clear_stage()

                # Letter
                elif monster.status in [12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
                    left = Animation(
                        center_y=monster.center_y + 400, duration=.2)
                    right = Animation(center_y=monster.center_y, duration=.2)
                    anim = left + right
                    if anim:
                        anim.stop(self)
                    anim.start(monster)
                    monster.status = 3

                # 3. MESSAGE
                elif monster.status == 3:
                    pass
                # 4. JUMP - SONIC
                elif monster.status == 4:
                    self.character_jump(2)  # jump time x 2
                # 5. Gold Ring - SONIC
                elif monster.status == 5:
                    # up and hide animation
                    # remove gold ring
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
                # 6,7. FLAGS - MARIO
                elif monster.status == 6:
                    self.character.velocity = [0, 0]
                    if self.is_ycoll:
                        self.character.velocity = [
                            self.block_size / self.speed_ratio, 0]
                    pass
                elif monster.status == 7:
                    pass
                # 8. Gold coin - MARIO
                elif monster.status == 8:
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
                self.is_jumping = False

        # trap
        for trap in self.traps:
            if self.character.collide_widget(trap):
                self.init_stage()

        # tip label
        if self.tip_label.opacity <= 1.0:
            self.tip_label.opacity += 0.005

    def bring_stage(self):

        # default
        self.time_limit = 10
        self.tip_label.opacity = 0.0

        # Chapter 1
        if self.stage == 0:
            _bricks = STAGE0_BRICKS
            _signs = STAGE0_SIGNS
            _monsters = STAGE0_MONSTERS
            _traps = STAGE0_TRAPS

            # hide controller
            app.game.left_button.opacity = 0.0
            app.game.right_button.opacity = 0.0
            self.tip = "STAGE 1"
            self.tip2 = "게임 소개"
            self.character.comment = "이 게임은 '잘난코'가 만들었습니다."
            self.block_size = 64

        if self.stage == 1:
            _bricks = STAGE1_BRICKS
            _signs = STAGE1_SIGNS
            _monsters = STAGE1_MONSTERS
            _traps = STAGE1_TRAPS

            # hide controller
            app.game.left_button.opacity = 0.0
            app.game.right_button.opacity = 0.0
            self.tip = "한 여름의 결혼식을"
            self.tip2 = "게임으로 축하드리고자"
            self.character.comment = "따듯한 6월 27일입니다."
            self.block_size = 64

        # Sonic Theme
        elif self.stage == 2:
            _bricks = STAGE2_BRICKS
            _signs = STAGE2_SIGNS
            _monsters = STAGE2_MONSTERS
            _traps = STAGE2_TRAPS
            self.tip = "여진이가 좋아하는"
            self.tip2 = "달리는 게임"
            self.character.comment = "안녕하세요 여진입니다."
            self.block_size = 40

        # Super Mario Theme
        elif self.stage == 3:
            _bricks = STAGE3_BRICKS
            _signs = STAGE3_SIGNS
            _monsters = STAGE3_MONSTERS
            _traps = STAGE3_TRAPS
            self.tip = "완호가 좋아하는"
            self.tip2 = "점프 게임"
            self.character.comment = ""
            self.block_size = 35
            self.time_limit = 15

        elif self.stage == 4:
            _bricks = STAGE4_BRICKS
            _signs = STAGE4_SIGNS
            _monsters = STAGE4_MONSTERS
            _traps = STAGE4_TRAPS
            self.block_size = 58
            self.block_size = 40

            self.tip = "여러가지 게임이 마구마구 섞여서"
            self.tip2 = "알아볼 수 없도록"
            self.character.comment = ""

        elif self.stage == 5:
            _bricks = STAGE5_BRICKS
            _signs = STAGE5_SIGNS
            _monsters = STAGE5_MONSTERS
            _traps = STAGE5_TRAPS
            self.block_size = 58

            self.tip = "게임은"
            self.tip2 = "전설의 용사가 공주를 구하듯 만들어서"
            self.character.comment = ""

        elif self.stage == 6:
            _bricks = STAGE6_BRICKS
            _signs = STAGE6_SIGNS
            _monsters = STAGE6_MONSTERS
            _traps = STAGE6_TRAPS
            self.block_size = 35

            # 장모님 캐릭터?
            self.tip = "결론은"
            self.tip2 = "결혼을 축하하는 게임입니다."
            self.character.comment = "재미있게 즐겨주세요"

        elif self.stage == 7:
            _bricks = STAGE7_BRICKS
            _signs = STAGE7_SIGNS
            _monsters = STAGE7_MONSTERS
            _traps = STAGE7_TRAPS

            self.tip = "STAGE 2"
            self.tip2 = "이제부터 어려워 질꺼에요"
            self.character.comment = ""
            self.block_size = 64

        elif self.stage == 8:
            _bricks = STAGE8_BRICKS
            _signs = STAGE8_SIGNS
            _monsters = STAGE8_MONSTERS
            _traps = STAGE8_TRAPS

            self.tip = "완호와 여진은"
            self.tip2 = "꽤 괜찮은 커플이에요"
            self.character.comment = ""
            self.block_size = 64

        elif self.stage == 9:
            _bricks = STAGE9_BRICKS
            _signs = STAGE9_SIGNS
            _monsters = STAGE9_MONSTERS
            _traps = STAGE9_TRAPS
            self.tip = "둘 다 먹는 걸 좋아하고"
            self.tip2 = "살은 남자만 찝니다"
            self.block_size = 64

        elif self.stage == 10:
            _bricks = STAGE10_BRICKS
            _signs = STAGE10_SIGNS
            _monsters = STAGE10_MONSTERS
            _traps = STAGE10_TRAPS
            self.tip = "두 분 모두 사람을 돕는 일을 하고 있으며"
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 11:
            _bricks = STAGE11_BRICKS
            _signs = STAGE11_SIGNS
            _monsters = STAGE11_MONSTERS
            _traps = STAGE11_TRAPS
            self.tip = "한눈에 봐도 잘 어울려요"
            self.tip2 = "비율, 외모, 성격, 울보, 먹보.."
            self.block_size = 64

        elif self.stage == 12:
            _bricks = STAGE12_BRICKS
            _signs = STAGE12_SIGNS
            _monsters = STAGE12_MONSTERS
            _traps = STAGE12_TRAPS
            self.tip = "서로를 아끼고"
            self.tip2 = "무엇보다 두 분이"
            self.block_size = 64

        elif self.stage == 13:
            _bricks = STAGE13_BRICKS
            _signs = STAGE13_SIGNS
            _monsters = STAGE13_MONSTERS
            _traps = STAGE13_TRAPS
            self.tip = "사랑하니까요"
            self.tip2 = "무엇보다 두 분이"
            self.block_size = 64

        elif self.stage == 14:
            _bricks = STAGE14_BRICKS
            _signs = STAGE14_SIGNS
            _monsters = STAGE14_MONSTERS
            _traps = STAGE14_TRAPS
            self.tip = "결혼을 축하드립니다"
            self.tip2 = "여기가 게임의 끝입니다."
            self.block_size = 64

        elif self.stage == 15:
            _bricks = STAGE15_BRICKS
            _signs = STAGE15_SIGNS
            _monsters = STAGE15_MONSTERS
            _traps = STAGE15_TRAPS
            self.tip = "STAGE 3"
            self.tip2 = "이제부터는 정말 어렵습니다. 도전하실분만 하세요"
            self.block_size = 64

        elif self.stage == 16:
            _bricks = STAGE16_BRICKS
            _signs = STAGE16_SIGNS
            _monsters = STAGE16_MONSTERS
            _traps = STAGE16_TRAPS
            self.tip = ""
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 17:
            _bricks = STAGE17_BRICKS
            _signs = STAGE17_SIGNS
            _monsters = STAGE17_MONSTERS
            _traps = STAGE17_TRAPS
            self.tip = ""
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 18:
            _bricks = STAGE18_BRICKS
            _signs = STAGE18_SIGNS
            _monsters = STAGE18_MONSTERS
            _traps = STAGE18_TRAPS
            self.tip = ""
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 19:
            _bricks = STAGE19_BRICKS
            _signs = STAGE19_SIGNS
            _monsters = STAGE19_MONSTERS
            _traps = STAGE19_TRAPS
            self.tip = ""
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 20:
            _bricks = STAGE20_BRICKS
            _signs = STAGE20_SIGNS
            _monsters = STAGE20_MONSTERS
            _traps = STAGE20_TRAPS
            self.tip = ""
            self.tip2 = ""
            self.block_size = 64

        # 청첩장 링크 바로가기
        # 게임 종료
        # 크레딧

        self.character.block_size = self.block_size

        for pos in _bricks:
            new_brick = Brick()
            new_brick.block_size = self.block_size
            new_brick.x = self.center[0] + (pos[0] * self.block_size)
            new_brick.y = self.y + (pos[1] * self.block_size)
            self.add_widget(new_brick)
            self.bricks = self.bricks + [new_brick]

        for pos in _signs:
            new_sign = Sign()
            new_sign.block_size = self.block_size
            new_sign.x = self.center[0] + (pos[0] * self.block_size)
            new_sign.y = self.y + (pos[1] * self.block_size)
            self.add_widget(new_sign)
            self.signs = self.signs + [new_sign]

        for pos in _monsters:
            self.get_monster(pos)

        for pos in _traps:
            new_trap = Trap()
            new_trap.block_size = self.block_size
            new_trap.x = self.center[
                0] + (pos[0] * self.block_size) + self.block_size / 4
            new_trap.y = self.y + \
                (pos[1] * self.block_size) + self.block_size / 4
            self.add_widget(new_trap)
            self.traps = self.traps + [new_trap]

    def get_monster(self, pos):
        new_monster = Monster()
        new_monster.block_size = self.block_size
        new_monster.x = self.center[
            0] + (pos[0] * self.block_size)
        new_monster.y = self.y + \
            (pos[1] * self.block_size)
        new_monster.status = pos[2]
        new_monster.init_image_dir()
        self.add_widget(new_monster)
        self.monsters = self.monsters + [new_monster]

    # Control
    def on_touch_down(self, touch):
        # if app.game.a_button.collide_point(*touch.pos):
        self.character_jump()

        # Princess Move
        # if self.collide_point(*touch.pos):
        #    if self.princess.collide_point(*touch.pos):
        #        self.princess.velocity = [0, 0]
        #    else:
        #        v = Vector(touch.x, touch.y) - Vector(self.princess.center)
        #        v = v.normalize()
        #        v *= 4
        #        self.princess.velocity = v
        #        self.is_touch = True
        #        self.touch = touch

        # Character Move
        # if self.stage in [1, ]:
        #     pass
        # else:
        #     if app.game.left_button.collide_point(*touch.pos):
        #         self.character.velocity = [-self.block_size / self.speed_ratio, 0]
        #         self.is_key_down = True
        #         touch.grab(self)
        #     if app.game.right_button.collide_point(*touch.pos):
        #         self.character.velocity = [self.block_size / self.speed_ratio, 0]
        #         self.is_key_down = True
        #         touch.grab(self)

        # if app.game.b_button.collide_point(*touch.pos):
        #     self.character_jump()

    def on_touch_up(self, touch):
        pass
        # if self.princess.collide_point(*touch.pos):
        #     self.is_touch = False
        #     self.princess.velocity = [0, 0]

        # if self.stage:
        #     pass
        # else:
        #     if self.control_widget_a.collide_point(*touch.pos) & self.is_key_down:
        #         self.character.velocity = [0, 0]
        #         self.is_key_down = False
        #         touch.ungrab(self)

    def on_touch_move(self, touch):
        pass
        # if self.stage in [1, ]:
        #     pass
        # else:
        #     if touch.grab_current is self:
        #         if not self.control_widget_a.collide_point(*touch.pos):
        #             self.character.velocity = [0, 0]
        #             self.is_key_down = False
        #             touch.ungrab(self)

        # Jump
    before_y = 0
    dt = 0

    def character_jump(self, ratio=1):
        if self.is_jumping:
            return
        Clock.schedule_interval(self.up, 1.0 / 60.0)
        Clock.schedule_once(self.character_jump_high, 0.2 * ratio)

        # before
        self.before_y = self.character.y
        self.dt = 0

    def character_jump_high(self, dt):
        Clock.unschedule(self.up)

    def up(self, dt):
        self.dt += dt
        self.character.y = self.before_y + \
            sin(self.dt * 3.14) * self.character.block_size * 4
        self.is_jumping = True

        # Background Control
    def txupdate(self, *l):
        t = Clock.get_boottime()
        v = 0.05
        ratio = round(self.width / self.height, 1)

        if self.stage % 2 == 1:
            self.rect_1.tex_coords = - \
                (t * v), 0, -(t * v + ratio), 0,  - \
                (t * v + ratio), -1, -(t * v), -1
        else:
            self.rect_1.tex_coords = - \
                (t * v), 0, -(t * v - ratio), 0,  - \
                (t * v - ratio), -1, -(t * v), -1


class GameScreen(Screen):
    game_widget = ObjectProperty(None)
    control_widget_a = ObjectProperty(None)
    control_widget_b = ObjectProperty(None)

    left_button = None
    right_button = None
    a_button = None
    # b_button = None

    def on_enter(self):
        self.game_widget.init_game(
            self.control_widget_a, self.control_widget_b)


class EndScreen(Screen):
    score = 0
    pass


class GameApp(App):

    """ app만 관리"""
    game = None
    last_score = 0

    def build(self):
        global app
        app = self
        self.title = 'MarryMe'

        root = ScreenManager()
        root.add_widget(MenuScreen(name='menu screen'))
        # root.add_widget(ChapterScreen(name='chapter screen'))
        root.add_widget(EndScreen(name='end screen'))

        self.game = GameScreen(name='game screen')
        root.add_widget(self.game)
        return root


if __name__ in ('__main__', '__android__'):
    GameApp().run()
