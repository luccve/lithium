#combat aranha ou cobra
import construir
import imagem
import pygame
from random import randint, randrange
from time import sleep
import os
pygame.init()

#tela

screen = (1280,720)
JANELA = pygame.display.set_mode(screen,0,32)
pygame.display.set_caption('Lithium')
FPS = pygame.time.Clock()

#caminho relativo

monstros = pygame.sprite.Group()



for i in range(6):
    skeleto = construir.Monster(1280,0, imagem.skeleto_walk)
    monstros.add(skeleto)



while True:
#Desenhando
    FPS.tick(60)
    JANELA.fill((0, 0, 0))
    

    
    monstros.draw(JANELA)
    monstros.update()
    pygame.display.flip() 

