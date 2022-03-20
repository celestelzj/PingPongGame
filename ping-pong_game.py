from pygame import *
from random import randint

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (255, 204, 255)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        #self.image_set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    pass

pad_1 = Player('C:\\Celeste Lee Zi Jia local\\Python Games\\Ping-Pong Game\\Pad 1.png' ,30, 200, 4, 50, 150)
pad_2 = Player('C:\\Celeste Lee Zi Jia local\\Python Games\\Ping-Pong Game\\Pad 2.png' ,520, 200, 4, 50, 150)
ball = GameSprite('C:\\Celeste Lee Zi Jia local\\Python Games\\Ping-Pong Game\\ball.png' ,200, 200, 4, 50, 50)


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        pad_1.reset()
        pad_2.reset()
        ball.reset()

    display.update()