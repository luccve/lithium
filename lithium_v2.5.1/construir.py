import os
import pygame
from pygame import display, sprite, image, transform,mixer,draw
from pygame.locals import*
from random import randrange, randint

class Player(sprite.Sprite):
    #X e Y definimos a posição inicias nc = n de cena da sprite inicial
    def __init__(self, x, y, nc, img):
        sprite.Sprite.__init__(self)
        self.frames_enya = []
        for m in range(4):
            self.img = img.subsurface((0, m*32), (30, 32))
            self.frames_enya.append(self.img)
        self.c_cena = nc

        self.image = self.frames_enya[self.c_cena]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def movimento(self, n=0):
        self.c_cena = n
    

    def update(self, x_player, y_player):
        self.image = self.frames_enya[self.c_cena]
        self.rect.x = x_player
        self.rect.y = y_player


class NPC(sprite.Sprite):
    #XeY definimos a posição e nc = número de cena
    def __init__(self, x, y, nc, img):
        sprite.Sprite.__init__(self)

        self.npc_lista = []
        for m in range(3):
            self.img = img.subsurface((0, m*32), (30, 32))
            self.npc_lista.append(self.img)
        self.c_cena = nc

        self.image = self.npc_lista[self.c_cena]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)

    def cena(self, n):
        self.c_cena = n

    def pos_npc(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.npc_lista[self.c_cena]


class Ambiente(sprite.Sprite):
    #XeY posição img = imagem do objeto
    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)


class Limite_mov_player(sprite.Sprite):
    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)

    def update(self):
        pass


'''Na classe texto teremos um padrão de recorte assim como nas sprites 32x32.Agora nessa que vai abrigar os textos teremos o padrão de recorte de uma imagem lista em 1280x240px. Nossa sprite de texto terá n_caixas camadas de acordo com o diálalogo'''


class Textos(sprite.Sprite):
    def __init__(self,x, y, img, n_caixas):
        sprite.Sprite.__init__(self)

        self.lista_de_msg = []

        for m in range(n_caixas):
            self.img = img.subsurface((0, m*240), (1280, 240))
            self.lista_de_msg.append(self.img)
        
        self.caixa_txt = 0
        
        self.image = self.lista_de_msg[self.caixa_txt]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        #Por padrão de posicionamento na tela(640, 600)
        self.rect.center = (x, y)
    
    def caixa(self, n):
        self.caixa_txt = n
    
    def update(self):
        self.image = self.lista_de_msg[self.caixa_txt]

class Monster(pygame.sprite.Sprite):
    #X e Y definimos a posição inicias nc = n de cena da sprite inicial
    def __init__(self,x,nc, img):
        pygame.sprite.Sprite.__init__(self)
        self.frames_monster = []
        for m in range(13):
            self.img = img.subsurface((22*m, 0), (22, 33))
            self.frames_monster.append(self.img)
        self.c_cena = nc

        self.image = self.frames_monster[self.c_cena]
        #self.image = pygame.transform.scale(self.image,(500,500))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = randrange(50,700,75)
    def update(self):
        if self.c_cena>=12:
            self.c_cena = 0
        self.c_cena +=0.25
        self.image = self.frames_monster[int(self.c_cena)]
        self.rect.x +=1
        if self.rect.x >= 1280:
            self.rect.x =0