import pygame
from pygame import display, sprite, image, transform
from pygame import mixer
from pygame.draw import rect
from pygame.image import load
from pygame.locals import*
from random import randrange

pygame.init()

#Abertura
larg = 1280
altura = 720
pygame.display.set_caption('lithium')
tela = pygame.display.set_mode((larg, altura))
frames = pygame.time.Clock()

global_sprites = sprite.Group()
global_sprites.add()


while True:
    frames.tick(60)
    tela.fill((0, 0, 0))
    #Fundamentos dos eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    global_sprites.draw(tela)
    global_sprites.update()
    #O fim do código
    display.flip()
