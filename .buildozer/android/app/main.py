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
# <Widget>:
#    canvas.after:
#        Line:
#            rectangle: self.x+1,self.y+1,self.width-1,self.height-1
#            dash_offset: 2
#            dash_length: 3

<EndScreen>:
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        canvas:
            Color:
                rgb: 218/255., 204/255., 175/255., 1
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
                text: "당신의 축복 점수는 무려 %s 점" % root.score
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
    canvas:
        Color:
            rgb: 255/255., 255/255., 255/255., 1
        Rectangle:
            pos: self.pos
            size: self.size
    # Image:
    #    source: 'data/hudHeart_full.png'
    #    pos: root.pos[0], root.pos[1] + 100
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
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
            BoxLayout:
        BoxLayout:
            size_hint_x:0.1

<Brick>:
    size: brick_image.width, brick_image.height
    center: root.center
    Image:
        id: brick_image
        source: 'data/box.png'
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

<Character>:
    player_image:player_image
    other_image:other_image

    size: player_image.width-10, player_image.height-10
    Image:
        id: player_image
        source: 'data/angel.png' if root.is_man else 'data/knight_right.png'
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
    Image:
        id: other_image
        source: 'data/knight.png' if root.is_man else 'data/angel_right.png'
        center:  [root.center[0] + root.block_size, root.center[1]] if root.is_man else [root.center[0] - root.block_size, root.center[1]]
        size: root.block_size, root.block_size
        allow_stretch: True


<Trap>
    size: trap_image.width/2, trap_image.height/2
    Image:
        id: trap_image
        source: 'data/spikes.png'
        center: root.center
        size: root.block_size, root.block_size

<GameWidget>:
    character: character
    background_widget: background_widget
    tip_label: tip_label
    tip2_label: tip2_label

    Widget:
        id: background_widget
        pos: self.parent.pos
        size: self.parent.size

    Character:
        id: character
    Label:
        id: tip_label
        text: root.tip
        font_size: 40
        font_name: 'data/NanumGothic.ttf'
        center: [root.center[0], root.center[1]+40]
        size: 100, 40
        color: (0, 0, 0, 1)

    Label:
        id: tip2_label
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
        font_size: 20
        font_name: 'data/NanumGothic.ttf'
        pos: root.x, root.parent.height - 100
        color: (0, 0, 0, 1)

    Label:
        text: "축복 점수: %s" % root.score
        font_size: 20
        font_name: 'data/NanumGothic.ttf'
        pos: root.x, root.parent.height - 150
        color: (0, 0, 0, 1)

    Label:
        text: 'FPS: ' + root.fps if root.fps != None else 'FPS:'
        font_size: 20
        font_name: 'data/NanumGothic.ttf'
        pos: root.x, root.parent.height - 200
        size: 100, 40
        halign: 'right'
        color: (0, 0, 0, 1)

<GameScreen>:
    game_widget: game_widget
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        GameWidget:
            size_hint_y:0.7
            id: game_widget
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y:0.3
            Image:
                source: 'data/ground2.png'
                pos: self.pos
                size: self.size
                allow_stretch: True
                keep_ratio: False
''')


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
        elif self.status == 22:
            self.source_dir = "data/flagSilver.png"
        elif self.status == 23:
            self.source_dir = "data/bolt_gold.png"
        elif self.status == 24:
            self.source_dir = "data/flower.png"

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

        elif self.status == 30:
            self.source_dir = "data/alienBeige_hurt.png"
        elif self.status == 31:
            self.source_dir = "data/alienBlue_hurt.png"
        elif self.status == 32:
            self.source_dir = "data/alienGreen_hurt.png"
        elif self.status == 33:
            self.source_dir = "data/alienPink_hurt.png"
        elif self.status == 34:
            self.source_dir = "data/alienYellow_hurt.png"


class Trap(Widget):
    block_size = NumericProperty(64)
    pass


class MenuScreen(Screen):
    pass


# STAGE 0
STAGE0_BRICKS = [[0, 0]]
STAGE0_SIGNS = []
STAGE0_MONSTERS = []
STAGE0_TRAPS = []

# STAGE 1
STAGE1_BRICKS = [[-4, 0], [-2, 0], [0, 0], [2, 0], [4, 0]]
STAGE1_SIGNS = []
STAGE1_MONSTERS = []
STAGE1_TRAPS = []

# STAGE 2
STAGE2_BRICKS = [
    [6, 0],

    [3, 0], [4, 0],
    [4, 1],

    [-1, 0], [0, 0], [1, 0],
    [0, 1], [1, 1],
    [1, 2],

    [-6, 0], [-5, 0], [-4, 0], [-3, 0],
    [-5, 1], [-4, 1], [-3, 1],
    [-4, 2], [-3, 2],
    [-3, 3],
]

STAGE2_SIGNS = []
STAGE2_MONSTERS = []
STAGE2_TRAPS = []

# STAGE 3
STAGE3_BRICKS = []
STAGE3_SIGNS = []
STAGE3_MONSTERS = []
STAGE3_TRAPS = [[-4, 0], [0, 0], [4, 0]]

# STAGE 4
STAGE4_BRICKS = [[-4, 1], [1, 0], [0, 0], [4, 1]]
STAGE4_SIGNS = []
STAGE4_MONSTERS = []
STAGE4_TRAPS = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0],
                [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]


# STAGE 5
STAGE5_BRICKS = [[4, 0]]
STAGE5_SIGNS = []
STAGE5_MONSTERS = [[0, 0, 24]]
STAGE5_TRAPS = [[-4, 0]]

# STAGE 6
STAGE6_BRICKS = []
STAGE6_SIGNS = []
STAGE6_MONSTERS = [
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
    [3, 3, 8],
    [1, 2, 8], [2, 2, 8], [3, 2, 8], [4, 2, 8], [5, 2, 8],
    [1, 0, 8], [2, 1, 8], [4, 1, 8], [5, 0, 8],
    # cha
    [7, 3, 8], [8, 3, 8], [9, 3, 8], [10, 3, 8],
    [10, 2, 8],
    [7, 1, 8], [8, 1, 8], [9, 1, 8], [10, 1, 8],
    [10, 0, 8],
]
STAGE6_TRAPS = []

# STAGE 7
STAGE7_BRICKS = []
STAGE7_SIGNS = []
STAGE7_MONSTERS = [[0, 0, 23]]
STAGE7_TRAPS = []


# STAGE 8
STAGE8_BRICKS = [[2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                 [3, 1], [4, 1], [5, 1], [6, 1], [7,
                                                  1],
                 [4, 2], [5, 2], [6, 2], [7,
                                          2],
                 [5, 3], [6, 3], [7, 3],
                 [6, 4], [7, 4],
                 [7, 5],
                 [10, 0],
                 [-4, 0], [-3, 0], [-3, 1], [-2, 0],
                 [-9, 0], [-8, 0], [-8, 1], [-7, 0]
                 ]
STAGE8_SIGNS = []
STAGE8_MONSTERS = [
    [-10, 0, 8], [-9, 1, 8], [-8, 2, 8], [-7, 1, 8], [-6, 0, 8],
    [-5, 0, 8], [-4, 1, 8], [-3, 2, 8], [-2, 1, 8], [-1, 0, 8],
    # FLAG
    [10, 1, 22], [10, 2, 6], [10, 3, 6], [10, 4, 6], [10, 5, 6], [10, 6, 7]]
STAGE8_TRAPS = []

# STAGE 9
STAGE9_BRICKS = [[3, 0], [0, 0], [-3, 0], [-3, 1]]
STAGE9_SIGNS = []
STAGE9_MONSTERS = [
    # GOLD RING
    [10, 0, 23],  # Flash
    [11, 0, 5],
    [9, 0, 5],
    [8, 0, 5],
    [8, 0, 5],
    [7, 0, 5],
    [7, 0, 5],
    [6, 0, 5],
    [6, 0, 5],
    [5, 0, 5],
    [4, 0, 5],
    [3, 1, 5],
    [2, 0, 5],
    [1, 0, 5],
    [0, 1, 23],  # Flash
    [-1, 0, 5],
    [-2, 0, 5],
    [-3, 2, 5],
    [-4, 0, 5],
    [-5, 0, 5],
    [-6, 0, 5],
    [-7, 0, 5],
    [-8, 0, 5],
    [-9, 0, 5],
    [-10, 0, 5],
    [-11, 0, 23],  # Flash
]
STAGE9_TRAPS = []

# STAGE 5 - 챕터2
# STAGE5_BRICKS = []
# STAGE5_SIGNS = []  # [[1, 0]]
# STAGE5_MONSTERS = [[-3, 0, 2], [0, 0, 2], [3, 0, 9], [7, 0, 10]]
# STAGE5_TRAPS = []

# STAGE 10 - AVOID MONSTER WITH BLOCK
STAGE10_BRICKS = []
STAGE10_SIGNS = []  # [[1, 0]]
STAGE10_MONSTERS = [[-5, 0, 12], [-4, 0, 13], [-3, 0, 14], [-2, 0, 15], [-1, 0, 16],
                    [0, 0, 17], [1, 0, 18], [2, 0, 19], [3, 0, 20], [4, 0, 17], [5, 0, 21], [6, 0, 13], [7, 0, 14]]
STAGE10_TRAPS = []


# STAGE 11 - 돕기
STAGE11_BRICKS = []
STAGE11_SIGNS = []  # [[1, 0]]
STAGE11_MONSTERS = [[-6, 0, 1], [-5, 0, 1], [-4, 0, 1], [-3, 0, 1], [-2, 0, 1], [-1, 0, 1],
                    [0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [
    4, 0, 1], [5, 0, 1], [6, 0, 1],
    [-5, 1, 1], [-4, 1, 1], [-3, 1, 1], [-2, 1, 1], [-1, 1, 1],
    [0, 1, 1], [1, 1, 1], [2, 1, 1], [
    3, 1, 1], [4, 1, 1], [5, 1, 1],
    [-4, 2, 1], [-3, 2, 1], [-2, 2, 1], [-1, 2, 1],
    [0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1], [
    4, 2, 1], [5, 2, 1], [6, 2, 1], [6, 1, 1]
]
STAGE11_TRAPS = []


# STAGE 12
STAGE12_BRICKS = []
STAGE12_SIGNS = []
STAGE12_MONSTERS = [
    [-5, 0, 30], [-3, 0, 31], [0, 0, 32], [3, 0, 33], [5, 0, 34]]
STAGE12_TRAPS = []

# STAGE10_BRICKS = [[-6, 0], [-5, 0], [-4, 0], [-2, 0],
#                   [0, 0],  [2, 0], [4, 0], [5, 0], [6, 0],
#                   [-5, 1], [-4, 1],  [-2, 1],
#                   [0, 1],  [2, 1], [4, 1], [5, 1],
#                   [-4, 2],  [-2, 2],
#                   [0, 2], [2, 2], [4, 2]]
# STAGE10_SIGNS = []
# STAGE10_MONSTERS = []
# STAGE10_TRAPS = [[-3, 0], [-1, 0], [1, 0], [3, 0]]

# STAGE 11
STAGE13_BRICKS = [[-6, 0], [-5, 0], [-2, 0], [-1, 0],
                  [0, 0], [1, 0], [2, 0],
                  [5, 0], [6, 0]]
STAGE13_SIGNS = []  # [[1, 0]]
STAGE13_MONSTERS = []
STAGE13_TRAPS = [[-4, 0], [-3, 0], [3, 0], [4, 0]]

# STAGE 12
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
    tip2_label = ObjectProperty()

    is_start = False
    is_invincible = True

    # Character's Move
    is_key_down = False
    is_jumping = False
    is_ycoll = False

    player_label = ObjectProperty(None)

    # timer
    time_limit = 0
    time = NumericProperty(0.1)

    block_size = NumericProperty(64)

    # Speed
    speed_ratio = 12

    def update_time(self, dt):
        if self.is_start:
            self.time -= 0.1
            if self.time <= 0:
                self.failed_stage()

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))

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

        self.is_start = False
        self.score += int(self.time)

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

        self.stage += 1

        if self.stage == 15:
            self.tip = "GAME OVER"
            return

        self.bring_stage()

        if self.stage % 2 == 0:
            self.character.velocity = [self.block_size / self.speed_ratio, 0]
            self.character.is_man = 0
        else:
            self.character.velocity = [-self.block_size / self.speed_ratio, 0]
            self.character.is_man = 1

        self.character_pos_init()

        self.time = self.time_limit

        Clock.schedule_once(self.start_game, 2)

    def init_game(self):
        is_start = False

        # bring stage
        self.bring_stage()

        self.character.velocity = [self.block_size / self.speed_ratio, 0]

        # map init
        with self.background_widget.canvas:
            texture = CoreImage('data/blue_land.png').texture
            texture.wrap = 'repeat'
            self.rect_1 = Rectangle(
                texture=texture, size=self.size, pos=self.pos)
        self.character_pos_init()
        self.init_stage()

    def start_game(self, dt):
        self.character_pos_init()
        self.is_start = True
        self.tip2_label.opacity = 1.0

    def failed_stage(self):
        left = Animation(
            center_y=self.character.center_y + 50, duration=.1)
        right = Animation(center_y=self.character.center_y - 100, duration=.2)
        anim = left + right
        anim.start(self.character)

        self.init_stage()

    def init_stage(self):
        # time
        self.time = self.time_limit
        self.is_start = False

        Clock.unschedule(self.update)
        Clock.unschedule(self.update_fps)
        Clock.unschedule(self.update_time)
        Clock.unschedule(self.start_game)

        # 멈췄다가 시작하도록 유도
        Clock.schedule_interval(self.update, 1 / 60)
        Clock.schedule_interval(self.update_fps, .1)
        Clock.schedule_interval(self.update_time, .1)
        Clock.schedule_once(self.start_game, 2)

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

    countt = 0

    def update(self, dt):
        """ 게임업데이트 """

        if not self.is_start:
            self.txupdate(dt)
            # tip label
            if self.tip_label.opacity <= 1.0:
                self.tip_label.opacity += 0.005

            return

        self.txupdate(dt)

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
                    self.score += 1

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
                    self.score += 2

                elif monster.status == 9:  # Boss
                    monster.source_dir = "data/spider_dead.png"
                    monster.status = 3
                    self.score += 3

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
                    self.score += 1

                # Hurt
                elif monster.status in [30, 31, 32, 33, 34]:
                    left = Animation(
                        center_y=monster.center_y + 400, duration=.2)
                    right = Animation(center_y=monster.center_y, duration=.2)
                    anim = left + right
                    if anim:
                        anim.stop(self)
                    anim.start(monster)
                    monster.source_dir = monster.source_dir.replace(
                        "_hurt", "")
                    monster.status = 3
                    self.score += 2

                # 3. MESSAGE
                elif monster.status == 3:
                    pass
                # 4. JUMP - SONIC
                elif monster.status == 4:
                    self.character_jump(2)  # jump time x 2
                # 5. Gold Ring - SONIC
                elif monster.status == 5:
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
                    self.score += 1
                # 6. speed up
                elif monster.status == 23:
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
                    self.score += 1
                    self.character.velocity = [
                        self.character.velocity[0] * 2, 0]

                # 6,7. FLAGS - MARIO
                elif monster.status == 6:
                    self.character.velocity = [0, 0]
                    self.score += 1
                elif monster.status == 22:
                    self.character.velocity = [
                        self.block_size / self.speed_ratio, 0]

                # 8. Gold coin - MARIO
                elif monster.status in [8, 24]:
                    self.remove_widget(monster)
                    self.monsters.remove(monster)
                    self.score += 1
                self.is_jumping = False

        # trap
        for trap in self.traps:
            if self.character.collide_widget(trap):
                self.failed_stage()

    def bring_stage(self):

        # default
        self.time_limit = 10
        self.tip_label.opacity = 0.0
        self.tip2_label.opacity = 0.0

        # Chapter 1 - 블럭넘는 것을 알려줌
        if self.stage == 0:
            _bricks = STAGE0_BRICKS
            _signs = STAGE0_SIGNS
            _monsters = STAGE0_MONSTERS
            _traps = STAGE0_TRAPS

            # hide controller
            self.tip = "신랑 완호와"
            self.tip2 = ""
            self.character.comment = ""
            self.block_size = 64
            self.character.other_image.opacity = 0.0
            self.time_limit = 7

        if self.stage == 1:
            _bricks = STAGE1_BRICKS
            _signs = STAGE1_SIGNS
            _monsters = STAGE1_MONSTERS
            _traps = STAGE1_TRAPS

            # hide controller
            self.tip = "신부 여진의"
            self.tip2 = ""
            self.character.comment = ""
            self.block_size = 64
            self.time_limit = 9

        # Chapter 2 - 가시를 피하는 게임
        elif self.stage == 2:
            _bricks = STAGE2_BRICKS
            _signs = STAGE2_SIGNS
            _monsters = STAGE2_MONSTERS
            _traps = STAGE2_TRAPS
            self.tip = "축복을 모으는 게임"
            self.tip2 = ""
            self.character.comment = ""
            self.block_size = 64
            self.time_limit = 10

        # Chapter 3 - 가시와 블럭 운영
        elif self.stage == 3:
            _bricks = STAGE3_BRICKS
            _signs = STAGE3_SIGNS
            _monsters = STAGE3_MONSTERS
            _traps = STAGE3_TRAPS

            self.tip = "1차 클로즈 베타입니다."
            self.tip2 = ""
            self.character.comment = ""
            self.block_size = 55
            self.time_limit = 13

        elif self.stage == 4:
            _bricks = STAGE4_BRICKS
            _signs = STAGE4_SIGNS
            _monsters = STAGE4_MONSTERS
            _traps = STAGE4_TRAPS
            self.block_size = 64
            self.tip = "스테이즈는 아직 구상중이니 엉망일수 있어요"
            self.tip2 = ""
            self.character.comment = ""


#            self.tip = "신부 여진이가 좋아하는"
#            self.tip2 = "달리는 게임과"
#           self.tip = "신랑 완호가 좋아하는"
#           self.tip2 = "점프 게임으로"
#           self.tip = "결혼을 축하하고자 하는 목적으로"
#           self.tip2 = "특별하게 제작하게 되었습니다."
#             self.tip = "게임은"
#             self.tip2 = "몬스터를 물리치고 공주를 구하듯이"

            self.character.comment = ""

        elif self.stage == 5:
            _bricks = STAGE5_BRICKS
            _signs = STAGE5_SIGNS
            _monsters = STAGE5_MONSTERS
            _traps = STAGE5_TRAPS
            self.block_size = 64

            self.tip = "테마, 컨셉, 크기, 조작? 등 다양한 의견좀 주세요"
            self.tip2 = ""
            self.character.comment = ""

        elif self.stage == 6:
            _bricks = STAGE6_BRICKS
            _signs = STAGE6_SIGNS
            _monsters = STAGE6_MONSTERS
            _traps = STAGE6_TRAPS
            self.block_size = 40

            self.tip = ""
            self.tip2 = ""
            self.character.comment = ""

        elif self.stage == 7:
            _bricks = STAGE7_BRICKS
            _signs = STAGE7_SIGNS
            _monsters = STAGE7_MONSTERS
            _traps = STAGE7_TRAPS

            self.tip = "STAGE 2"
            self.tip2 = "스토리 모드"
            self.character.comment = ""
            self.block_size = 64

        elif self.stage == 8:
            _bricks = STAGE8_BRICKS
            _signs = STAGE8_SIGNS
            _monsters = STAGE8_MONSTERS
            _traps = STAGE8_TRAPS

            self.tip = "신랑 완호와 신부 여진은"
            self.tip2 = "잘 어울리는 커플입니다."
            self.character.comment = ""
            self.block_size = 40

        elif self.stage == 9:
            _bricks = STAGE9_BRICKS
            _signs = STAGE9_SIGNS
            _monsters = STAGE9_MONSTERS
            _traps = STAGE9_TRAPS
            self.tip = "둘 다 먹는 걸 매우 좋아하고"
            self.tip2 = ""
            self.block_size = 40

        elif self.stage == 10:
            _bricks = STAGE10_BRICKS
            _signs = STAGE10_SIGNS
            _monsters = STAGE10_MONSTERS
            _traps = STAGE10_TRAPS
            self.tip = "둘 다 사람을 돕는 일을 하고 있으며"
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 11:
            _bricks = STAGE11_BRICKS
            _signs = STAGE11_SIGNS
            _monsters = STAGE11_MONSTERS
            _traps = STAGE11_TRAPS
            self.tip = "한눈에 봐도 잘 어울려요"
            self.tip2 = "비율, 외모, 성격, 울보, 먹보, 바보.."
            self.block_size = 64

        elif self.stage == 12:
            _bricks = STAGE12_BRICKS
            _signs = STAGE12_SIGNS
            _monsters = STAGE12_MONSTERS
            _traps = STAGE12_TRAPS
            self.tip = "무엇보다 서로를 이해하고"
            self.tip2 = "아껴주는 한쌍입니다."
            self.block_size = 64

        elif self.stage == 13:
            _bricks = STAGE13_BRICKS
            _signs = STAGE13_SIGNS
            _monsters = STAGE13_MONSTERS
            _traps = STAGE13_TRAPS
            self.tip = "STAGE 3"
            self.tip2 = "스토리 모드"
            self.block_size = 64
            self.character.other_image.opacity = 1.0

        elif self.stage == 14:
            _bricks = STAGE14_BRICKS
            _signs = STAGE14_SIGNS
            _monsters = STAGE14_MONSTERS
            _traps = STAGE14_TRAPS
            self.tip = "결혼식 날짜는 6월 27일"
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 15:
            _bricks = STAGE15_BRICKS
            _signs = STAGE15_SIGNS
            _monsters = STAGE15_MONSTERS
            _traps = STAGE15_TRAPS
            self.tip = "판교에서 이루어 집니다."
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 16:
            _bricks = STAGE16_BRICKS
            _signs = STAGE16_SIGNS
            _monsters = STAGE16_MONSTERS
            _traps = STAGE16_TRAPS
            self.tip = "많은 참석 바랍니다."
            self.tip2 = ""
            self.block_size = 64

        elif self.stage == 17:
            _bricks = STAGE17_BRICKS
            _signs = STAGE17_SIGNS
            _monsters = STAGE17_MONSTERS
            _traps = STAGE17_TRAPS
            self.tip = "쓸 내용이 없다"
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
            self.tip = "마지막"
            self.tip2 = "총 20스테이지 예상중"
            self.block_size = 64


#        elif self.stage == 15:
#            _bricks = STAGE15_BRICKS
#            _signs = STAGE15_SIGNS
#            _monsters = STAGE15_MONSTERS
#            _traps = STAGE15_TRAPS
#            self.tip = "BONUS STAGE"
#            self.tip2 = "스토리는 끝났습니다. 이제 게임이 어려워집니다."
#            self.block_size = 64
#
#        elif self.stage == 16:
#            _bricks = STAGE16_BRICKS
#            _signs = STAGE16_SIGNS
#            _monsters = STAGE16_MONSTERS
#            _traps = STAGE16_TRAPS
#            self.tip = "1"
#            self.tip2 = ""
#            self.block_size = 64
#
#        elif self.stage == 17:
#            _bricks = STAGE17_BRICKS
#            _signs = STAGE17_SIGNS
#            _monsters = STAGE17_MONSTERS
#            _traps = STAGE17_TRAPS
#            self.tip = "2"
#            self.tip2 = ""
#            self.block_size = 64
#
#        elif self.stage == 18:
#            _bricks = STAGE18_BRICKS
#            _signs = STAGE18_SIGNS
#            _monsters = STAGE18_MONSTERS
#            _traps = STAGE18_TRAPS
#            self.tip = "3"
#            self.tip2 = ""
#            self.block_size = 64
#
#        elif self.stage == 19:
#            _bricks = STAGE19_BRICKS
#            _signs = STAGE19_SIGNS
#            _monsters = STAGE19_MONSTERS
#            _traps = STAGE19_TRAPS
#            self.tip = "4"
#            self.tip2 = ""
#            self.block_size = 64

        elif self.stage == 20:
            _bricks = STAGE20_BRICKS
            _signs = STAGE20_SIGNS
            _monsters = STAGE20_MONSTERS
            _traps = STAGE20_TRAPS
            self.tip = "5"
            self.tip2 = ""
            self.block_size = 64

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
        self.character_jump(1.1)

    def on_touch_up(self, touch):
        pass

    def on_touch_move(self, touch):
        pass

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

    def on_enter(self):
        self.game_widget.init_game()


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
        root.add_widget(EndScreen(name='end screen'))

        self.game = GameScreen(name='game screen')
        root.add_widget(self.game)
        return root


if __name__ in ('__main__', '__android__'):
    GameApp().run()
