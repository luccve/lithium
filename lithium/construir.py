import os
import pygame
from pygame import display, sprite, image, transform,mixer,draw
from pygame.locals import*
from random import randrange

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
        self.x_init = x
        self.y_init = y
        self.rect.x = x
        self.rect.y = y

    def movimento(self, n=0):
        self.c_cena = n
    

    def update(self):
        if 50 > self.rect.x or 50 > self.rect.y:
            self.rect.x += 50
            self.rect.y += 50

        if self.rect.x > 1200 or self.rect.y > 680:
            self.rect.x -= 50
            self.rect.y -= 50
        

        self.rect.x
        self.rect.y
        self.image = self.frames_enya[self.c_cena]
        

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
        self.rect.x = x
        self.rect.y = y
        

    def cena(self, n):
        self.c_cena = n

    def pos_npc(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x
        self.rect.y
        self.image = self.npc_lista[self.c_cena]

'''Observação: as varíaveis de ambiente apresentam movimentação por isso é necessário update das posiçãoes em tela seguindo a proporção do display'''

class Ambiente(sprite.Sprite):
    #XeY posição img = imagem do objeto
    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)

    def update(self):
        self.rect.x 
        self.rect.y
        

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

        self.n_caixas = n_caixas
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
    
    def caixa(self, enter):
        self.caixa_txt = enter
        #print(F"class: {enter}")

    
    def update(self):
        self.image = self.lista_de_msg[self.caixa_txt]


class Monster(pygame.sprite.Sprite):
    #X e Y definimos a posição inicias nc = n de cena da sprite inicial
    def __init__(self,x, nc, img):
        pygame.sprite.Sprite.__init__(self)

        self.estado = 0
        self.frames_life = []
        self.pos_x = []
        self.pos_y = []

        for m in range(13):
            self.img = img.subsurface((22*m, 0), (22, 33))
            self.frames_life.append(self.img)
        self.c_cena = nc

        self.image = self.frames_life[self.c_cena]
        #self.image = pygame.transform.scale(self.image,(500,500))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = randrange(50,700,75)
        

    def morte(self, img):
        self.estado = 1
        self.frames_dead = []

        for m in range(15):
            self.img = img.subsurface((33*m, 0), (33, 32))
            self.frames_dead.append(self.img)
        
        self.c_cena = 0

        self.image = self.frames_dead[self.c_cena]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.image

        if self.estado == 0:
            if self.c_cena>=12:
                self.c_cena = 0
            self.c_cena += 0.25
            self.image = self.frames_life[int(self.c_cena)]
            self.rect.x +=1
            self.pos_x.append(self.rect.x)
            self.pos_y.append(self.rect.y)

        if self.estado == 1:

            if self.c_cena>=14:
                self.c_cena = 0
                self.estado = 0
                self.rect.x = self.pos_x[0] 
                self.rect.y = self.pos_y[0]

            self.c_cena += 0.10
            self.image = self.frames_dead[int(self.c_cena)]
            self.rect.x =  self.pos_x[-1]
            self.rect.y = self.pos_y[-1]

        
        if self.rect.x >= 1280:
            self.rect.x = 0