import pygame
from pygame import display, sprite, image, transform
from pygame import mixer
from pygame.draw import rect
from pygame.image import load
from pygame.locals import*
import os

pygame.init()

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'sprites')
pasta_sons = os.path.join(pasta_principal, 'musica')
print(pasta_imagens)

#Display
LARGURA = 1280
ALTURA = 720
pos_x = LARGURA/2
pos_y = ALTURA/2
TELA = (1280, 720)
display.set_caption('Lithium')
JANELA = display.set_mode(TELA,0,32)
FPS = pygame.time.Clock()

#Constates
VELOCIDADE_PLAYER = 15

#imagens
sprite_enya = image.load(os.path.join(pasta_imagens, 'enya.png')).convert_alpha()
sprite_enya.set_colorkey([0, 255, 0])

chao = image.load(os.path.join(pasta_imagens, 'grama.png')).convert_alpha()
chao.set_colorkey([0, 0, 0])

fundo = image.load(os.path.join(pasta_imagens, 'vertice.png')).convert_alpha()
fundo.set_colorkey([0, 0, 0])

'''
self.s_enya = sprite_enya.subsurface((0, 0), (30, 32)) -- 0
self.l_enya = sprite_enya.subsurface((0, 32), (30, 32)) -- 1
self.r_enya = sprite_enya.subsurface((0, 64), (30, 32)) -- 2
self.w_enya = sprite_enya.subsurface((0, 96), (30, 32)) -- 3
'''

class Player(sprite.Sprite):
    global pos_x, pos_y
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.frames_enya = []
        for m in range(4):
            self.img = sprite_enya.subsurface((0 ,m*32),(30,32))
            self.frames_enya.append(self.img)
        self.c_cena = 0

        self.image = self.frames_enya[self.c_cena]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def movimento(self, n = 0):
        self.c_cena = n

    def update(self):
        self.image = self.frames_enya[self.c_cena]
        self.rect.center = (pos_x, pos_y)

class Chao(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = chao
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
    
    def update(self):
        self.mask = pygame.mask.from_surface(self.image)


class Fundo(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = fundo
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)

#Imagems

#sound_back = pygame.mixer.Sound("musica/drama1.wav")
#pygame.mixer.music.play(0)
#sound_back.set_volume(0.25)

#movimento = {r_enya:'Direito',l_enya:"Esquerdo", w_enya:'Cima', s_enya:'Baixo'}
#print(movimento)


#Sprite do chao
chao_sprite = sprite.Group()
chao = Chao()
chao_sprite.add(chao)

#Sprite do player
global_sprites = sprite.Group()
player = Player()
global_sprites.add(player)

#Sprite do Fundo
fundo_sprite = sprite.Group()
fundo_tela = Fundo()
fundo_sprite.add(fundo_tela)

while True:
    #sound_back.play()
    FPS.tick(30)

    JANELA.fill((0, 200, 0))

    fundo_sprite.draw(JANELA)
    chao_sprite.draw(JANELA)
    global_sprites.draw(JANELA)
    

    colisao = sprite.spritecollide(player, fundo_sprite, False, pygame.sprite.collide_mask)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if colisao:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pos_y += VELOCIDADE_PLAYER
                    player.movimento(n=0)

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pos_x -= VELOCIDADE_PLAYER
                    player.movimento(n=1)

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pos_x += VELOCIDADE_PLAYER
                    player.movimento(n=2)

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pos_y -= VELOCIDADE_PLAYER
                    player.movimento(n=3)
        

    global_sprites.update()
    display.flip()  

    
