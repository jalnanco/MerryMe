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
                text: '웨딩RPG'
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
                text: '캐릭터를 선택해주세요'
                font_size: 30
                font_name: 'data/NanumGothic.ttf'
                color: 0/255., 0/255., 0/255., 1
            BoxLayout:
                orientation: 'vertical' if self.height > self.width else 'horizontal'
                Button:
                    text: '신랑'
                    font_size: 30
                    background_color: 218/255., 195/255., 175/255., 1
                    font_name: 'data/NanumGothic.ttf'
                    on_press: root.manager.transition = WipeTransition(); root.manager.current = 'game screen'
                Button:
                    text: '신부'
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

<Brick>:
    size: brick_image.width, brick_image.height
    center: root.center
    Image:
        id: brick_image
        source: 'data/boxCrate_double.png'
        center: root.center
        size: 64, 64
<Sign>:
    size: brick_image.width, brick_image.height
    center: root.center
    Image:
        id: brick_image
        source: 'data/signRight.png'
        center: root.center
        size: 64, 64
<Monster>:
    size: monster_image.width, monster_image.height
    center: root.center
    Image:
        id: monster_image
        source: 'data/spinner.png'
        center: root.center
        size: 64, 64


<Princess>:
    size: player_image.width, player_image.height
    Image:
        id: player_image
        source: 'data/girl64.png'
        center: root.center
        size: 64, 64
    Image:
        source: 'data/laserBlue2.png'
        x: player_image.x
        y: player_image.y - 100
        size: 64, 100
        opacity: 0.5
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'

<Knight>:
    size: player_image.width, player_image.height
    Image:
        id: player_image
        source: 'data/boy64.png'
        center: root.center
        size: 64, 64
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'

<Monster>:
    size: monster_image.width, monster_image.height
    Image:
        id: monster_image
        source: 'data/spinner.png'
        center: root.center
        size: 64, 64
    # Label:
    #    text: root.comment
    #    size: 200, 20,
    #    pos: root.x - 15, root.center_y + 30
    #    font_size: 15
    #    font_name: 'data/NanumGothic.ttf'


<GameWidget>:
    princess: princess
    knight: knight
    background_widget: background_widget

    Widget:
        id: background_widget
        pos: self.parent.pos
        size: self.parent.size

    Princess:
        id: princess
        # pos: root.center
        # Label:
        #    # text: "%s" % self.parent.size
        #    pos: self.parent.pos
        #    size: self.parent.size
    Knight:
        id: knight
        # pos: root.center
        # Label:
        #    # text: "%s" % self.parent.size
        #    pos: self.parent.pos
        #    size: self.parent.size

    Label:
        text: "STAGE: %s" % root.stage
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-120
        size: 100, 40

    Label:
        text: "Score: %s" % root.score
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-40
        size: 100, 40

    Label:
        text: 'FPS: ' + root.fps if root.fps != None else 'FPS:'
        font_size: 25
        font_name: 'data/NanumGothic.ttf'
        pos: root.parent.x, root.parent.height-80
        size: 100, 40
        halign: 'right'

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


class Princess(Widget):
    velocity_x = 0
    velocity_y = 0
    velocity = [0, 0]
    comment = StringProperty("")

    def move(self):
        self.center = Vector(*self.velocity) + self.center

    def stop(self):
        self.velocity = [0, 0]


class Knight(Widget):
    velocity_x = 0
    velocity_y = 0
    velocity = [0, 0]
    comment = StringProperty("")

    def move(self):
        self.center = Vector(*self.velocity) + self.center

    # def stop(self):
    #     self.velocity = [0, 0]


class Brick(Widget):
    pass


class Sign(Widget):
    pass


class Enemy(Widget):
    pass


class Monster(Widget):
    pass

    # velocity_x = 0
    # velocity_y = 0
    # velocity = [0, 0]
    # speed = 2

    # def move(self):
    #     self.center = Vector(*self.velocity) + self.center

    # def respon(self):
    #     """ 적의 위치를 새롭게 지정한다."""
    #     self.velocity = random.randint(-2, 2), random.randint(-2, 2)
    #     if self.velocity_x == 0 and self.velocity_y == 0:
    #         x = random.randint(1, 4)
    #         if x == 1:
    #             self.velocity_x = 1
    #         elif x == 2:
    #             self.velocity_x = -1
    #         elif x == 3:
    #             self.velocity_y = 1
    #         elif x == 4:
    #             self.velocity_y = -1
    #     self.speed = random.randint(1, 4)


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


class ControlWidget(Widget):
    pass


# 64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768 (12)
# BOX - 64 x 64
STAGE1_BRICKS = [[-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0],
                 [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
STAGE1_SIGNS = [[-8, 0]]
STAGE1_MONSTERS = []  # [[-4, 1]]

STAGE2_BRICKS = [[200, 0], [264, 0], [328, 0]]
STAGE2_SIGNS = [[100, 0]]
STAGE2_MONSTERS = []


class GameWidget(Widget):
    fps = StringProperty(None)
    princess = None
    knight = None

    bricks = []
    signs = []
    monsters = []
    score = NumericProperty(0)
    count = 0
    stage = NumericProperty(1)

    is_start = False
    is_invincible = True

    # Princess's Move
    is_touch = False
    touch = None

    # Knight's Move
    is_key_down = False
    is_jumping = False
    is_ycoll = False

    player_label = ObjectProperty(None)
    control_widget_a = None
    control_widget_b = None

    def update_fps(self, dt):
        self.fps = str(int(Clock.get_fps()))
        # if fps < 40:
        # self.remove_widget(self.enemies[0])
        # self.enemies.remove(self.enemies[0])
        # print "ddd", len(self.enemies)
        # self.enemies[-1].width += 10
        # self.enemies[-1].height += 10

    def init_game(self, ca, cb):
        # start
        self.is_start = True
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_interval(self.update_fps, .1)
        # Clock.schedule_interval(self.test, 5)
        # Clock.schedule_once(self.test, 1)
        Clock.schedule_interval(self.txupdate, 0)

        # re position princess
        self.princess.pos = [self.width - self.princess.width - 20, self.y]
        self.knight.pos = [self.x + 20, self.y]

        # bring stage
        self.bring_stage()
        self.score = 0
        self.knight.velocity = [5, 0]

        # map init
        with self.background_widget.canvas:
            texture = CoreImage('data/starBackground.png').texture
            texture.wrap = 'repeat'
            self.rect_1 = Rectangle(
                texture=texture, size=self.size, pos=self.pos)

        # controller
        self.control_widget_a = ca
        self.control_widget_b = cb

    # def test(self, *args):
    #    seed = random.randint(1, 4)
    #    if seed == 1:
    #        self.princess.comment = "언제쯤 오시나요"
    #    elif seed == 2:
    #        self.princess.comment = "약속시간이 꽤 지났는데"
    #    elif seed == 3:
    #        self.princess.comment = "소개팅남은 언제오시는 걸까요?"
    #    elif seed == 4:
    #        self.princess.comment = "집에 가야되나"
    #    Clock.schedule_once(self.remove_player_label, 3)

    # def remove_player_label(self, *args):
    #     self.princess.comment = ""

    def knight_x_collision(self, brick):

        if self.knight.x < brick.x:
            self.knight.x = brick.x - self.knight.width - 1
        else:
            self.knight.x = brick.x + brick.width + 1

        # print self.knight.y, self.knight.height, brick.y, brick.height, brick.size
        # if self.knight.y == brick.y + brick.height:
        #     print 1111
        # self.knight.velocity[0] = 0

    def knight_y_collision(self, brick):
        if self.knight.y > brick.y:
            self.knight.y = brick.y + brick.height
            print "jumping False yCollision"
            return True
        else:
            self.knight.y = brick.y - self.knight.height
            return False

    def update(self, dt):
        """ 게임업데이트 """
        if not self.is_start:
            return

        if self.is_touch:
            # Princess's Move
            self.princess.move()
            self.on_touch_down(self.touch)

        self.is_ycoll = False

        # Knight's Move
        for brick in self.bricks:
            if self.knight.collide_widget(brick):
                z = Vector(self.knight.center) - Vector(brick.center)
                # check y
                if -0.71 < z.normalize()[0] < 0.71:
                    if self.knight_y_collision(brick):
                        self.is_jumping = False
                        self.is_ycoll = True
                        break
                else:
                    # check x
                    self.knight_x_collision(brick)

        self.knight.move()

        # y 충돌이면 떨어지지 않는다. // 표면보다 같거나 낮으면 떨어지지 않는다.
        if not self.is_ycoll and not self.knight.y <= self.y:
            self.knight.y -= 5.0

        # floor
        self.count
        if self.knight.y <= self.y and self.is_jumping:
            print "jumping False flooor %d"
            self.is_jumping = False
            self.knight.y = self.y

        # next stage
        if self.knight.center_x > self.width:
            self.clear_stage()
            self.knight.pos = [self.x + 20, self.y]

            self.stage += 1
            self.stage_name = "STAGE%d" % self.stage
            self.bring_stage()

        # monster
        for monster in self.monsters:
            if self.knight.collide_widget(monster):
                self.knight.pos = [self.x + 20, self.y]
                print "hit monster id: %s" % monster.uid
                self.is_jumping = False

                # self.is_start = False
                # delete enemies
            #         for e in self.enemies:
            #             e.center = [10, 10]
            #             self.remove_widget(e)
            #             self.enemies = []
            #         app.last_score = self.score
            #         app.root.current = "score screen"
            #         Clock.unschedule(self.update)
            #         Clock.unschedule(self.update_fps)

            #     enemy.move()
            #     # 1. 리스폰 범위를 x축으로 벗어 나면 반대 쪽 x축에서 나온다.
            #     # 2. 현재 위치를 파악해서 발사한다.
            #     is_out = False

            #     if self.width + enemy.width < enemy.center_x:
            #         enemy.center_x = self.x - enemy.width
            #         enemy.center_y = random.randint(self.y, self.height)
            #         is_out = True
            #     elif self.height + enemy.height < enemy.center_y:
            #         enemy.center_y = self.y - enemy.height
            #         enemy.center_x = random.randint(self.x, self.width)
            #         is_out = True
            #     elif self.x - enemy.width > enemy.center_x:
            #         enemy.center_x = self.width - enemy.center_x
            #         enemy.center_y = random.randint(self.y, self.height)
            #         is_out = True
            #     elif self.y - enemy.height > enemy.center_y:
            #         enemy.center_y = self.height - enemy.center_y
            #         enemy.center_x = random.randint(self.x, self.width)
            #         is_out = True
            #     if is_out:
            #         # Chase princess
            #         v = Vector(self.princess.center) - Vector(enemy.center)
            #         v = v.normalize()
            #         v *= enemy.speed
            #         enemy.velocity = v

            #     # GameOver
            #     if self.princess.collide_widget(enemy):
            #         print "hit enemy id: %s" % enemy.uid
            #         self.is_start = False
            #         # delete enemies
            #         for e in self.enemies:
            #             e.center = [10, 10]
            #             self.remove_widget(e)
            #             self.enemies = []
            #         app.last_score = self.score
            #         app.root.current = "score screen"
            #         Clock.unschedule(self.update)
            #         Clock.unschedule(self.update_fps)
            # self.clear_widgets()

            # Score
            # self.count += 1
            # if self.count > TIME_UP:
            #    self.score += 1
            #    # self.add_enemy()
            #    self.count = 0
            #    if self.score % 5 == 0:
            #        self.add_enemy()

            #    def add_enemy(self):
            #        new_brick = Brick()
            #        # new_brick.respon()
            #        self.add_widget(new_brick)
            #        self.bricks = self.bricks + [new_brick]

    def bring_stage(self):
        if self.stage == 1:
            _bricks = STAGE1_BRICKS
            _signs = STAGE1_SIGNS
            _monsters = STAGE1_MONSTERS

            # hide controller
            app.game.left_button.opacity = 0.0
            app.game.right_button.opacity = 0.0

        elif self.stage == 2:
            _bricks = STAGE2_BRICKS
            _signs = STAGE2_SIGNS
            _monsters = STAGE2_MONSTERS
            # app.game.left_button.opacity = 1.0
            # app.game.right_button.opacity = 1.0

        for pos in _bricks:
            new_brick = Brick()
            new_brick.x = self.center[0] + (pos[0] * 64)
            new_brick.y = self.y + (pos[1] * 64)
            self.add_widget(new_brick)
            self.bricks = self.bricks + [new_brick]
        for pos in _signs:
            new_sign = Sign()
            new_sign.x = self.center[0] + (pos[0] * 64)
            new_sign.y = self.y + (pos[1] * 64)
            self.add_widget(new_sign)
            self.signs = self.signs + [new_sign]
        for pos in _monsters:
            new_monster = Monster()
            new_monster.x = self.center[0] + (pos[0] * 64)
            new_monster.y = self.y + (pos[1] * 64)
            self.add_widget(new_monster)
            self.monsters = self.monsters + [new_monster]

    def clear_stage(self):
        for b in self.bricks:
            self.remove_widget(b)
        self.bricks = []
        for m in self.monsters:
            self.remove_widget(m)
        self.monsters = []
        for s in self. signs:
            self.remove_widget(s)
        self.signs = []

    # Control
    def on_touch_down(self, touch):

        # Princess Move
        if self.collide_point(*touch.pos):
            if self.princess.collide_point(*touch.pos):
                self.princess.velocity = [0, 0]
            else:
                v = Vector(touch.x, touch.y) - Vector(self.princess.center)
                v = v.normalize()
                v *= 4
                self.princess.velocity = v
                self.is_touch = True
                self.touch = touch

        # Knight Move
        if self.stage in [1, ]:
            pass
        else:
            if app.game.left_button.collide_point(*touch.pos):
                self.knight.velocity = [-5, 0]
                self.is_key_down = True
                touch.grab(self)
            if app.game.right_button.collide_point(*touch.pos):
                self.knight.velocity = [5, 0]
                self.is_key_down = True
                touch.grab(self)
        if app.game.a_button.collide_point(*touch.pos):
            self.knight_jump()
        # if app.game.b_button.collide_point(*touch.pos):
        #     self.knight_jump()

    def on_touch_up(self, touch):
        if self.princess.collide_point(*touch.pos):
            self.is_touch = False
            self.princess.velocity = [0, 0]

        if self.stage in [1, ]:
            pass
        else:
            if self.control_widget_a.collide_point(*touch.pos) & self.is_key_down:
                self.knight.velocity = [0, 0]
                self.is_key_down = False
                touch.ungrab(self)

    def on_touch_move(self, touch):
        if self.stage in [1, ]:
            pass
        else:
            if touch.grab_current is self:
                if not self.control_widget_a.collide_point(*touch.pos):
                    self.knight.velocity = [0, 0]
                    self.is_key_down = False
                    touch.ungrab(self)

    # Jump
    def knight_jump(self):
        if self.is_jumping:
            return
        Clock.schedule_interval(self.up, 1.0 / 60.0)
        Clock.schedule_once(self.knight_jump_high, 0.2)

    def knight_jump_high(self, dt):
        Clock.unschedule(self.up)

    def up(self, dt):
        # Chemi
        if self.knight.y < self.princess.y and self.princess.x + 20 >= self.knight.x and self.princess.x - 20 < self.knight.x:
            self.knight.y += 32.0
        else:
            self.knight.y += 16.0
        self.is_jumping = True

    # Background Control
    def txupdate(self, *l):
        t = Clock.get_boottime()
        v = 0.1
        ratio = round(self.width / self.height, 1)
        self.rect_1.tex_coords = - \
            (t * v), 0, -(t * v + ratio), 0,  - \
            (t * v + ratio), -1, -(t * v), -1


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

        self.game = GameScreen(name='game screen')
        root.add_widget(self.game)
        return root

if __name__ in ('__main__', '__android__'):
    GameApp().run()
