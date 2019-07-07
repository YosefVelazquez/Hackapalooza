import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((739,552))

pygame.init()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround= Background('IBM.png',[0,0])

while True:
    screen.fill([255,255,255])
    screen.blit(BackGround.image,BackGround.rect)
    time.sleep(200)
