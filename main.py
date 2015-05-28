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
        source:  "data/springboardUp.png" if root.status == 4 else "data/sandRing.png" if root.status == 5 else "data/cherry.png"

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
    status = NumericProperty(0)


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


# STAGE 1 - INTRO
STAGE1_BRICKS = []
STAGE1_SIGNS = [[-6, 0]]
STAGE1_MONSTERS = []
STAGE1_TRAPS = []

# STAGE 2 - SONIC THEME
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

# STAGE 3 - AVOID TRAP
STAGE3_BRICKS = []
STAGE3_SIGNS = [[-8, 0]]
STAGE3_MONSTERS = []
STAGE3_TRAPS = [[-6, 0], [-2, 0],
                [2, 0], [6, 0]]

# STAGE 4 - AVOID TRAP USING BLOCK SIZE DOWN(58)
STAGE4_BRICKS = [[-3, 0], [-3, 1], [-3, 2],
                 [-2, 0], [-2, 1], [-2, 2],
                 [1, 0], [1, 2],
                 [2, 0], [2, 2],
                 [5, 0], [6, 0]]
STAGE4_SIGNS = []
STAGE4_MONSTERS = []
STAGE4_TRAPS = [[-6, 0], [-5, 0], [-4, 0], [-1, 0], [0, 0], [3, 0], [4, 0]]

# STAGE 5 - 챕터2
STAGE5_BRICKS = []
STAGE5_SIGNS = [[-6, 0]]
STAGE5_MONSTERS = []
STAGE5_TRAPS = []

# STAGE 6 - AVOID MONSTER WITH BLOCK
STAGE6_BRICKS = []
STAGE6_SIGNS = []  # [[1, 0]]
STAGE6_MONSTERS = [[-3, 0, 2], [0, 0, 2], [3, 0, 2]]
STAGE6_TRAPS = []

# STAGE 7
STAGE7_BRICKS = [[-6, 0], [-5, 0], [-4, 0], [-2, 0],
                 [0, 0],  [2, 0], [4, 0], [5, 0], [6, 0],
                 [-5, 1], [-4, 1],  [-2, 1],
                 [0, 1],  [2, 1], [4, 1], [5, 1],
                 [-4, 2],  [-2, 2],
                 [0, 2], [2, 2], [4, 2]]
STAGE7_SIGNS = []  # [[1, 0]]
STAGE7_MONSTERS = []
STAGE7_TRAPS = [[-3, 0], [-1, 0], [1, 0], [3, 0]]

# # STAGE 7
# STAGE7_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
#                  [0, 0], [1, 0], [2, 0],
#                  [5, 0], [6, 0]]
# STAGE7_SIGNS = []  # [[1, 0]]
# STAGE7_MONSTERS = []
# STAGE7_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 8
STAGE8_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                 [0, 0], [1, 0], [2, 0],
                 [5, 0], [6, 0]]
STAGE8_SIGNS = []  # [[1, 0]]
STAGE8_MONSTERS = []
STAGE8_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 9
STAGE9_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                 [0, 0], [1, 0], [2, 0],
                 [5, 0], [6, 0]]
STAGE9_SIGNS = []  # [[1, 0]]
STAGE9_MONSTERS = []
STAGE9_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 10
STAGE10_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE10_SIGNS = []  # [[1, 0]]
STAGE10_MONSTERS = []
STAGE10_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

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
STAGE15_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE15_SIGNS = []  # [[1, 0]]
STAGE15_MONSTERS = []
STAGE15_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]


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
    stage = NumericProperty(1)
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
    time = NumericProperty(0.1)

    block_size = NumericProperty(64)

    def update_time(self, dt):
        self.time -= 0.1
        if self.time <= 0:
            print "over"
            self.init_stage()

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))

    def init_stage(self):
        """ when game failed """
        self.is_start = True

        print "STAGE: %d" % self.stage

        # time
        self.time = 10
        self.character_pos_init()

        # re position princess
        # self.princess.pos = [self.width - self.princess.width - 20, self.y]

    def character_pos_init(self):
        self.character.player_image.size = [self.block_size, self.block_size]

        if self.character.is_man == 0:
            self.character.pos = [self.x + 20, self.y]
        else:
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
            self.character.velocity = [self.block_size / 12, 0]
            self.character.is_man = 0
        else:
            self.character.velocity = [-self.block_size / 12, 0]
            self.character.is_man = 1

        self.character_pos_init()

    def init_game(self, ca, cb):

        # start
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_interval(self.update_fps, .1)
        Clock.schedule_interval(self.update_time, .1)
        # Clock.schedule_interval(self.test, 5)
        # Clock.schedule_once(self.test, 1)
        Clock.schedule_interval(self.txupdate, 0)

        # bring stage
        self.bring_stage()

        self.character.velocity = [self.block_size / 12, 0]

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

                print z.normalize()[0]

        self.character.move()

        # y 충돌이면 떨어지지 않는다. // 표면보다 같거나 낮으면 떨어지지 않는다.
        if not self.is_ycoll and not self.character.y <= self.y:
            self.character.y -= 5.0

        # floor
        if self.character.y <= self.y and self.is_jumping:
            print "jumping False flooor %d"
            self.is_jumping = False
            self.character.y = self.y

        # next stage
        if self.character.center_x > self.width or self.character.center_x < 0:
            self.clear_stage()

        # monster
        for monster in self.monsters:
            if self.character.collide_widget(monster):

                # 1. DIE
                if monster.status == 1:
                    self.character.pos = [self.x + 20, self.y]

                # 2. GROW
                elif monster.status == 2:
                    anim = Animation(
                        size=[self.character.player_image.width * 1.5, self.character.player_image.height * 1.5], duration=.2)
                    if anim:
                        anim.stop(self.character.player_image)
                        anim.start(self.character.player_image)
                    # remove monster
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
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
        self.time = 10
        self.tip_label.opacity = 0.0

        # Chapter 1
        if self.stage == 1:
            _bricks = STAGE1_BRICKS
            _signs = STAGE1_SIGNS
            _monsters = STAGE1_MONSTERS
            _traps = STAGE1_TRAPS

            # hide controller
            app.game.left_button.opacity = 0.0
            app.game.right_button.opacity = 0.0
            self.tip = "Chapter 1. Intro"
            self.tip2 = "게임을 소개합니다."
            self.character.comment = "안녕하세요 완호입니다."
            self.block_size = 64

        # Sonic Theme
        elif self.stage == 2:
            _bricks = STAGE2_BRICKS
            _signs = STAGE2_SIGNS
            _monsters = STAGE2_MONSTERS
            _traps = STAGE2_TRAPS
            self.tip = "소닉을 좋아하셨다는 형수님과.."
            self.tip2 = "화면을 터치하면 점프를 합니다."
            self.character.comment = "안녕하세요 여진입니다."
            self.block_size = 40

        elif self.stage == 3:
            _bricks = STAGE3_BRICKS
            _signs = STAGE3_SIGNS
            _monsters = STAGE3_MONSTERS
            _traps = STAGE3_TRAPS
            self.tip = "슈퍼마리오를 좋아하셨다는 형님께 바칩니다."
            self.tip2 = "재미있게 즐겨주세요"
            self.character.comment = ""
            self.block_size = 40

        elif self.stage == 4:
            _bricks = STAGE4_BRICKS
            _signs = STAGE4_SIGNS
            _monsters = STAGE4_MONSTERS
            _traps = STAGE4_TRAPS
            self.block_size = 58

            self.tip = "결혼을 축하드리고자 간단한 게임을 만들었습니다."
            self.tip2 = ""  # 동화처럼 오래오래 행복하게 잘살았으면 해요"
            self.character.comment = ""

        # 보너스 스테이지 추가예정
        # 다음 스테이지 전에 챕터 소개

        elif self.stage == 5:
            _bricks = STAGE5_BRICKS
            _signs = STAGE5_SIGNS
            _monsters = STAGE5_MONSTERS
            _traps = STAGE5_TRAPS
            self.block_size = 58

            self.tip = "Chapter 5"
            self.tip2 = "첫 만남"
            self.character.comment = "광주에서 있었던 일입니다."

        elif self.stage == 6:
            _bricks = STAGE6_BRICKS
            _signs = STAGE6_SIGNS
            _monsters = STAGE6_MONSTERS
            _traps = STAGE6_TRAPS
            self.block_size = 64

            # 장모님 캐릭터?
            self.tip = "회식이 있던 날, 형은 고깃집에 가게됩니다."
            self.tip2 = "먹으면 먹을수록 살이 찝니다."
            self.character.comment = "냠냠냠"

            # "고깃집 여사장님께서 형을 신랑감으로 알아보죠"
            # "미래의 장모님이십니다."
            # "자네 내 딸 한번 만나보지 않겠나? "

        elif self.stage == 7:
            _bricks = STAGE7_BRICKS
            _signs = STAGE7_SIGNS
            _monsters = STAGE7_MONSTERS
            _traps = STAGE7_TRAPS

            self.tip = "하지만 소개팅 당일 형은 지각을 합니다."
            self.tip2 = "무려 한시간을!!"
            self.character.comment = "아이고 늦었다아"
            self.block_size = 64

        elif self.stage == 8:
            _bricks = STAGE8_BRICKS
            _signs = STAGE8_SIGNS
            _monsters = STAGE8_MONSTERS
            _traps = STAGE8_TRAPS

            # 만남
            self.tip = "늦게 도착한 형은 형수님을 보고 첫눈에 반하십니다."
            self.tip2 = "형수님께서는 형의 마음을 서서히 받아주십니다."
            self.character.comment = "지각쟁이"
            self.block_size = 64

        # 보너스 스테이지 추가예정
        # 다음 스테이지 전에 챕터 소개

        elif self.stage == 9:
            _bricks = STAGE9_BRICKS
            _signs = STAGE9_SIGNS
            _monsters = STAGE9_MONSTERS
            _traps = STAGE9_TRAPS
            self.tip = "형과 형수님은 사람들의 건강을 도와주는 일을 합니다."
            self.tip2 = "그래서 서로를 잘 이해하나봐요"
            self.block_size = 64

        elif self.stage == 10:
            _bricks = STAGE10_BRICKS
            _signs = STAGE10_SIGNS
            _monsters = STAGE10_MONSTERS
            _traps = STAGE10_TRAPS
            self.tip = "열심히 일하고 여행도 가고 맛집도 갑니다."
            self.tip2 = "먹으면 찌는데 형만 찝니다. 심지어 형수님이 더 많이 먹는데.."
            self.block_size = 64

        elif self.stage == 11:
            _bricks = STAGE11_BRICKS
            _signs = STAGE11_SIGNS
            _monsters = STAGE11_MONSTERS
            _traps = STAGE11_TRAPS
            self.tip = "결혼준비로 바쁘던 5월에 데이트"
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 12:
            _bricks = STAGE12_BRICKS
            _signs = STAGE12_SIGNS
            _monsters = STAGE12_MONSTERS
            _traps = STAGE12_TRAPS
            self.tip = "형과 형수님께서 남산으로 데이트를 갑니다."
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 13:
            _bricks = STAGE13_BRICKS
            _signs = STAGE13_SIGNS
            _monsters = STAGE13_MONSTERS
            _traps = STAGE13_TRAPS
            self.tip = "한 건물에서 야경을 보면 이쁘다며 데려갑니다."
            self.tip2 = "우린 예약안해서 여기 투숙객인 것 처럼 위장해야되"
            self.block_size = 64

        elif self.stage == 14:
            _bricks = STAGE14_BRICKS
            _signs = STAGE14_SIGNS
            _monsters = STAGE14_MONSTERS
            _traps = STAGE14_TRAPS
            self.tip = "그곳에는 형이 준비한 팜플렛과 사진들이 걸려있었죠"
            self.tip2 = "서프라이즈!"
            self.block_size = 64

        elif self.stage == 15:
            _bricks = STAGE15_BRICKS
            _signs = STAGE15_SIGNS
            _monsters = STAGE15_MONSTERS
            _traps = STAGE15_TRAPS
            self.tip = "형이 준비한 영상을 틀자..형수님은 펑펑 웁니다."
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 16:
            _bricks = STAGE16_BRICKS
            _signs = STAGE16_SIGNS
            _monsters = STAGE16_MONSTERS
            _traps = STAGE16_TRAPS
            self.tip = "Will you marry me?"
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 17:
            _bricks = STAGE17_BRICKS
            _signs = STAGE17_SIGNS
            _monsters = STAGE17_MONSTERS
            _traps = STAGE17_TRAPS
            self.tip = "결혼식 소개를 마지막으로 이 게임을 마치도록 하겠습니다."
            self.tip2 = "오글거려서 손가락이 안펴지네요"
            self.block_size = 64

        elif self.stage == 18:
            _bricks = STAGE18_BRICKS
            _signs = STAGE18_SIGNS
            _monsters = STAGE18_MONSTERS
            _traps = STAGE18_TRAPS
            self.tip = "일시: 2015년 6월 27일 오후 1시"
            self.tip2 = "장소: 경기도 성남시 분당구 삼평동 689번지 (판교)차바이오컴플렉스"
            self.block_size = 64

        elif self.stage == 19:
            _bricks = STAGE19_BRICKS
            _signs = STAGE19_SIGNS
            _monsters = STAGE19_MONSTERS
            _traps = STAGE19_TRAPS
            self.tip = "게임을 플레이해주셔서 감사합니다."
            self.tip2 = "두 분의 행복을 축하해주세요."
            self.block_size = 64

        elif self.stage == 20:
            _bricks = STAGE20_BRICKS
            _signs = STAGE20_SIGNS
            _monsters = STAGE20_MONSTERS
            _traps = STAGE20_TRAPS
            self.tip = "조카는 언제쯤 볼 수 있을까요?."
            self.tip2 = "-끝-"
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
            new_monster = Monster()
            new_monster.block_size = self.block_size
            new_monster.x = self.center[
                0] + (pos[0] * self.block_size)
            new_monster.y = self.y + \
                (pos[1] * self.block_size)
            new_monster.status = pos[2]
            self.add_widget(new_monster)
            self.monsters = self.monsters + [new_monster]

        for pos in _traps:
            new_trap = Trap()
            new_trap.block_size = self.block_size
            new_trap.x = self.center[
                0] + (pos[0] * self.block_size) + self.block_size / 4
            new_trap.y = self.y + \
                (pos[1] * self.block_size) + self.block_size / 4
            self.add_widget(new_trap)
            self.traps = self.traps + [new_trap]

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
        #         self.character.velocity = [-self.block_size / 12, 0]
        #         self.is_key_down = True
        #         touch.grab(self)
        #     if app.game.right_button.collide_point(*touch.pos):
        #         self.character.velocity = [self.block_size / 12, 0]
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
        v = 0.1
        ratio = round(self.width / self.height, 1)

        if self.stage % 2 == 0:
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
