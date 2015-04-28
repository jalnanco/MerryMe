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
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty, ReferenceListProperty
from kivy.core.audio import SoundLoader

# ScreenManager
from kivy.uix.screenmanager import ScreenManager, Screen

# BorderImage
from kivy.graphics import Color, BorderImage

# move
from kivy.vector import Vector
from kivy.clock import Clock

# random respon
import random

# i hate math
from math import atan2, degrees

#!/usr/bin/kivy
__version__ = '1.0'

# app을 글로벌로 사용
from kivy.app import App
# app = None

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
<Widget>:
    canvas.after:
        Line:
            rectangle: self.x+1,self.y+1,self.width-1,self.height-1
            dash_offset: 2
            dash_length: 3

<MenuScreen>:
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
                text: 'Crush On You'
                font_size: 30
                font_name: 'data/NanumGothic.ttf'
            Button:
                text: 'Start'
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

<CharacterScreen>:
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        # orientation: 'vertical' if self.height > self.width else 'horizontal'
        canvas:
            Color:
                rgb: 218 / 255., 218 / 255., 175 / 255.
            # BackGroundColor
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            size_hint_x:0.1
        BoxLayout:
            size_hint_x:0.2
            orientation: 'vertical' if self.height > self.width else 'horizontal'
            Label:
                text: 'There was a'
                font_size: 30
                font_name: 'data/NanumGothic.ttf'
            BoxLayout:
                orientation: 'vertical' if self.height > self.width else 'horizontal'
                Button:
                    text: 'Boy'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
                    on_press: root.manager.transition = WipeTransition(); root.manager.current = 'game screen'
                Button:
                    text: 'Girl'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
            BoxLayout:
                Button:
                    text: 'Back'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
                    on_press: root.manager.transition = WipeTransition(); root.manager.current = 'menu screen'

        BoxLayout:
            size_hint_x:0.1

<Enemy>:
    size: enemy_image.size
    Image:
        id: enemy_image
        source: 'data/girl32.png'
        pos: root.pos
        size: 32, 32

<Player>:
    size: player_image.size
    Image:
        id: player_image
        source: 'data/boy64.png'
        pos: root.pos
        size: 64, 64


<GameWidget>:
    player: player
    # enemy: enemy

    Player:
        id: player
        pos: root.center
        Label:
            text: "%s" % self.parent.size
            pos: self.parent.pos
            size: self.parent.size

    Label:
        text: "Score: %s" % root.score
        pos: root.x, root.height-40
        size: 100, 40

    # Enemy:
    #    id: enemy
    #    pos: root.center
    #    Label:
    #        text: "%s" % self.parent.size
    #        pos: self.parent.pos

<GameScreen>:
    game_widget: game_widget
    BoxLayout:
        GameWidget:
            id: game_widget
''')


class Player(Widget):
    angle = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class Enemy(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def respon(self):
        """ 적의 위치를 새롭게 지정한다."""
        self.velocity = random.randint(-2, 2), random.randint(-2, 2)
        if self.velocity_x == 0 and self.velocity_y == 0:
            x = random.randint(1, 4)
            if x == 1:
                self.velocity_x = 1
            elif x == 2:
                self.velocity_x = -1
            elif x == 3:
                self.velocity_y = 1
            elif x == 4:
                self.velocity_y = -1


class MenuScreen(Screen):
    pass


class CharacterScreen(Screen):
    pass


TIME_UP = 60


class GameWidget(Widget):
    player = ObjectProperty(None)
    enemies = ListProperty([])
    score = NumericProperty(0)
    count = 0

    def init_game(self):
        self.add_enemy()

    def update(self):
        """ 게임업데이트 """
        # 적의 이동
        for enemy in self.enemies:
            enemy.move()
            # 1. 리스폰 범위를 x축으로 벗어 나면 반대 쪽 x축에서 나온다.
            # 2. 현재 위치를 파악해서 발사한다.
            if self.width + enemy.width < enemy.x:
                # 1. 내 위치를 지정한다.
                enemy.x = self.x - enemy.width
                enemy.y = random.randint(self.y, self.height)

                # 2. 내 위치와 플레이어의 위치로 향하도록 각도를 구한다.
                degree = Vector(enemy.x, enemy.y).angle(
                    (self.player.x, self.player.y))

            elif self.height + enemy.height < enemy.y:
                enemy.y = self.y - enemy.height
                enemy.x = random.randint(self.x, self.width)
            elif self.x - enemy.width > enemy.x:
                enemy.x = self.width - enemy.x
                enemy.y = random.randint(self.y, self.height)
            elif self.y - enemy.height > enemy.y:
                enemy.y = self.height - enemy.y
                enemy.x = random.randint(self.x, self.width)

        # 적군 생성
        self.count += 1
        if self.count > TIME_UP:
            self.score += 1
            self.add_enemy()
            self.count = 0

    def add_enemy(self):
        new_enemy = Enemy()
        new_enemy.respon()
        self.add_widget(new_enemy)
        self.enemies = self.enemies + [new_enemy]

    def on_touch_down(self, touch):
        Animation.cancel_all(self.player)
        angle = degrees(atan2(touch.y - self.player.center_y,
                              touch.x - self.player.center_x))
        Animation(center=touch.pos, angle=self.player.angle).start(self.player)

    def on_touch_down(self, touch):
        Animation.cancel_all(self.player)
        angle = degrees(atan2(touch.y - self.player.center_y,
                              touch.x - self.player.center_x))
        Animation(center=touch.pos, angle=self.player.angle).start(self.player)


class GameScreen(Screen):
    game_widget = ObjectProperty(None)

    def on_enter(self):
        self.game_widget.init_game()

    def update(self, dt):
        self.game_widget.update()


class GameApp(App):

    """ app만 관리"""
    game = None

    def build(self):
        # global app
        # app = self
        self.title = 'MarryMe'

        root = ScreenManager()
        root.add_widget(MenuScreen(name='menu screen'))
        root.add_widget(CharacterScreen(name='character screen'))

        game = GameScreen(name='game screen')
        root.add_widget(game)

        Clock.schedule_interval(game.update, 1.0 / 60.0)

        return root

if __name__ in ('__main__', '__android__'):
    GameApp().run()
