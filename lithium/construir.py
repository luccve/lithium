import os
import pygame
from pygame import display, sprite, image, transform,mixer,draw
from pygame.locals import*
from random import randrange
import imagem

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
        return n
    

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
    def __init__(self,x, nc):
        pygame.sprite.Sprite.__init__(self)

        self.estado = {'morto': False, 'vivo': True, 'golpeado': False} 
        self.pos_x = list()
        self.pos_y = list()
        self.frames = list()
        self.img_vivo = imagem.skeleto_walk
        self.img_dead =  imagem.skeleto_dead
        self.img_golpeado = imagem.skeleto_hit

        for m in range(13):
            self.temp = self.img_vivo.subsurface((22*m, 0), (22, 33))
            self.frames.append(self.temp)
        
        for m in range(15):
            self.temp = self.img_dead.subsurface((33*m, 0), (33, 32))
            self.frames.append(self.temp)

        for m in range(8):
            self.temp = self.img_dead.subsurface((30*m, 0), (30, 32))
            self.frames.append(self.temp)
        
        '''
        0 - 12 = vivo
        13 - 14 =  morto
        15 -  26 = golpeado
        
        '''
        
        self.c_cena = nc
        self.image = self.frames[self.c_cena]

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        #Posição
        self.x_init =  x
        self.y_init = randrange(50, 700, 50)
        
        self.rect.x = self.x_init
        self.rect.y = self.y_init

        self.pos_x.append(self.x_init)
        self.pos_y.append(self.y_init)

    def morte(self):
        self.estado['morto'] =  True

    def update(self):

        '''if self.estado['morto'] == True:
            self.c_cena = 13
            while self.c_cena < 27:
                self.c_cena += 0.25
                self.image = self.frames[int(self.c_cena)]
            self.estado['morto'] = False'''

        if self.c_cena>=12:
            self.c_cena = 0
        self.c_cena += 0.25
        self.image = self.frames[int(self.c_cena)]
        self.rect.x +=1
        self.pos_x.append(self.rect.x)
        self.pos_y.append(self.rect.y)
        
        if self.rect.x >= 1280:
            self.rect.x = 0


class Spear(sprite.Sprite):
    #X e Y definimos a posição inicias nc = n de cena da sprite inicial
    def __init__(self, player, img):
        sprite.Sprite.__init__(self)
        self.lançar = False
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.x_init = player.rect.centerx
        self.y_init = player.rect.y

        self.rect.x = self.x_init
        self.rect.y = self.y_init
    def mov(self, m):
        self.lançar = True
        '''if m == 0:
            self.rect.y += 10
        elif m == 1:
            self.rect.x -= 10
        elif m == 2:
            self.rect.x += 10
        elif m == 3:
            self.rect.y -= 10'''
    
    def update(self):
        if self.lançar:
            self.rect.x
            self.rect.y

            