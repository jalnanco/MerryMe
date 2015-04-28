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

#!/usr/bin/kivy
__version__ = '1.0'

# app을 글로벌로 사용
from kivy.app import App
app = None

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
<Widget>:
#    canvas.after:
#        Line:
#            rectangle: self.x+1,self.y+1,self.width-1,self.height-1
#            dash_offset: 2
#            dash_length: 3

<ScoreScreen>:
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
                text: '뿕렋(피하기게임)'
                font_size: 60
                font_name: 'data/NanumGothic.ttf'
                color: 0/255., 0/255., 0/255., 1
            Button:
                text: '시작하기'
                background_color: 122/255., 101/255., 54/255., 1
                font_name: 'data/NanumGothic.ttf'
                size_hint_y:0.2
                on_press: root.manager.transition = WipeTransition(); root.manager.current = 'character screen'
            BoxLayout:
                size_hint_y:0.1
            Button:
                text: '안먹는 버튼'
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
                text: '그곳에는..'
                font_size: 30
                font_name: 'data/NanumGothic.ttf'
                color: 0/255., 0/255., 0/255., 1
            BoxLayout:
                orientation: 'vertical' if self.height > self.width else 'horizontal'
                Button:
                    text: '한 소년이 있었다.'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
                    on_press: root.manager.transition = WipeTransition(); root.manager.current = 'game screen'
                Button:
                    text: '한 소녀가 있었다.(x)'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
            BoxLayout:
                Button:
                    text: '메뉴로'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
                    on_press: root.manager.transition = WipeTransition(); root.manager.current = 'menu screen'

        BoxLayout:
            size_hint_x:0.1

<Enemy>:
    size: enemy_image.width/2, enemy_image.height/2
    center: root.center
    Image:
        id: enemy_image
        source: 'data/girl64.png'
        center: root.center
        size: 64, 64

<Player>:
    size: player_image.width/2, player_image.height/2
    Image:
        id: player_image
        source: 'data/boy64.png'
        center: root.center
        size: 64, 64
    Label:
        text: root.comment
        size: 200, 20,
        pos: root.x - 15, root.center_y + 30
        font_size: 15
        font_name: 'data/NanumGothic.ttf'



<GameWidget>:
    player: player
    # enemy: enemy

    Player:
        id: player
        # pos: root.center
        Label:
            # text: "%s" % self.parent.size
            pos: self.parent.pos
            size: self.parent.size

    Label:
        text: "Score: %s" % root.score
        font_size: 30
        font_name: 'data/NanumGothic.ttf'
        pos: root.x, root.height-40
        size: 100, 40

    Label:
        text: 'FPS: ' + root.fps if root.fps != None else 'FPS:'
        font_size: 30
        font_name: 'data/NanumGothic.ttf'
        pos: root.x, root.height-80
        size: 100, 40
        halign: 'right'

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
    velocity_x = 0
    velocity_y = 0
    velocity = [0, 0]
    comment = StringProperty("")

    def move(self):
        self.center = Vector(*self.velocity) + self.center


class Enemy(Widget):
    velocity_x = 0
    velocity_y = 0
    velocity = [0, 0]
    speed = 2

    def move(self):
        self.center = Vector(*self.velocity) + self.center

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
        self.speed = random.randint(1, 4)


class MenuScreen(Screen):
    pass


class CharacterScreen(Screen):
    pass


class ScoreScreen(Screen):
    score = NumericProperty(0)
    def on_enter(self):
        self.score = app.last_score
    pass


TIME_UP = 60


class GameWidget(Widget):
    fps = StringProperty(None)
    player = None
    enemies = []
    score = NumericProperty(0)
    count = 0

    is_start = False
    is_invincible = True

    player_label = ObjectProperty(None)

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))
        # if fps < 40:
        # self.remove_widget(self.enemies[0])
        # self.enemies.remove(self.enemies[0])
        # print "ddd", len(self.enemies)
        # self.enemies[-1].width += 10
        #self.enemies[-1].height += 10

    def init_game(self):
        # start
        self.is_start = True
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_interval(self.update_fps, .1)
        Clock.schedule_interval(self.test, 5)
        Clock.schedule_once(self.test, 1)


        # re position player
        self.player.center = self.center

        # add enemy
        for n in xrange(20):
            self.add_enemy()
        self.score = 0

    def test(self, *args):
        seed = random.randint(1, 4)
        if seed == 1:
            self.player.comment = "음 훠훠 난 피하기의 달인!"
        elif seed == 2:
            self.player.comment = "반갑군 친구들!"
        elif seed == 3:
            self.player.comment = "배고프다아~!"
        elif seed == 4:
            self.player.comment = "어짜피 테스트인걸!"
        Clock.schedule_once(self.remove_player_label, 3)

    def remove_player_label(self, *args):
        self.player.comment = ""


    def update(self, dt):
        """ 게임업데이트 """
        if not self.is_start:
            return

        # Player's Move
        self.player.move()

        # Enemy's Move
        for enemy in self.enemies:
            enemy.move()
            # 1. 리스폰 범위를 x축으로 벗어 나면 반대 쪽 x축에서 나온다.
            # 2. 현재 위치를 파악해서 발사한다.
            is_out = False

            if self.width + enemy.width < enemy.center_x:
                enemy.center_x = self.x - enemy.width
                enemy.center_y = random.randint(self.y, self.height)
                is_out = True
            elif self.height + enemy.height < enemy.center_y:
                enemy.center_y = self.y - enemy.height
                enemy.center_x = random.randint(self.x, self.width)
                is_out = True
            elif self.x - enemy.width > enemy.center_x:
                enemy.center_x = self.width - enemy.center_x
                enemy.center_y = random.randint(self.y, self.height)
                is_out = True
            elif self.y - enemy.height > enemy.center_y:
                enemy.center_y = self.height - enemy.center_y
                enemy.center_x = random.randint(self.x, self.width)
                is_out = True
            if is_out:
                # Chase player
                v = Vector(self.player.center) - Vector(enemy.center)
                v = v.normalize()
                v *= enemy.speed
                enemy.velocity = v

            # GameOver
            if self.player.collide_widget(enemy):
                print "hit enemy id: %s" % enemy.uid
                self.is_start = False
                # delete enemies
                for e in self.enemies:
                    e.center = [10, 10]
                    self.remove_widget(e)
                    self.enemies = []
                app.last_score = self.score
                app.root.current = "score screen"
                Clock.unschedule(self.update)
                Clock.unschedule(self.update_fps)
                # self.clear_widgets()

        # Score
        self.count += 1
        if self.count > TIME_UP:
            self.score += 1
            # self.add_enemy()
            self.count = 0
            if self.score % 5 == 0:
                self.add_enemy()

    def add_enemy(self):
        new_enemy = Enemy()
        new_enemy.respon()
        self.add_widget(new_enemy)
        self.enemies = self.enemies + [new_enemy]

    def on_touch_down(self, touch):
        self.add_value(touch)

    def on_touch_move(self, touch):
        self.add_value(touch)

    def add_value(self, touch):
        v = Vector(touch.x, touch.y) - Vector(self.player.center)
        v = v.normalize()
        v *= 4
        self.player.velocity = v

    def on_touch_up(self, touch):
        self.player.velocity = [0, 0]


class GameScreen(Screen):
    game_widget = ObjectProperty(None)

    def on_enter(self):
        self.game_widget.init_game()


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
        root.add_widget(CharacterScreen(name='character screen'))
        root.add_widget(ScoreScreen(name='score screen'))

        game = GameScreen(name='game screen')
        root.add_widget(game)
        return root

if __name__ in ('__main__', '__android__'):
    GameApp().run()
