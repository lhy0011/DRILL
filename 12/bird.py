from pico2d import *
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 20.0 # 새의 속도, 시속 20km
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = random.randint(100, 1500), random.randint(300, 500) # 새의 랜덤위치 지정
        self.velocity = FLY_SPEED_PPS
        self.dir = random.randint(-1, 1) # 좌우 이동이 랜덤으로 되도록
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14 # 새의 프레임 속도 조절
        if self.dir == 0:
            self.dir = 1
        if self.x > 1550: # 벽에 닿으면 반대쪽으로 이동할 수 있도록
            self. dir = -1
        elif self.x < 50:
            self.dir = 1
        self.x += self.velocity * game_framework.frame_time * self.dir

    def draw(self):
        if self.dir == 1:
            Bird.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            Bird.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

