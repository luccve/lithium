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
XeY = 0
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

vertice_img = image.load(os.path.join(pasta_imagens, 'vertice.png')).convert_alpha()
vertice_img.set_colorkey([0, 0, 0])

npc_img = image.load(os.path.join(pasta_imagens, 'npc.png')).convert_alpha()
npc_img.set_colorkey([0, 0, 0])

def mouse():
    global XeY
    if event.type == pygame.MOUSEBUTTONDOWN:
        XeY = pygame.mouse.get_pos()
        print(XeY)

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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (pos_x, pos_y)

    def movimento(self, n = 0):
        self.c_cena = n

    def update(self):
        self.image = self.frames_enya[self.c_cena]
        self.rect.center = (pos_x, pos_y)


class NPC(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)

        self.npc_lista = []
        for m in range(3):
            self.img = npc_img.subsurface((0, m*32), (30, 32))
            self.npc_lista.append(self.img)
        self.c_cena = 0

        self.image = self.npc_lista[self.c_cena]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (333, 143)
    
    def cena(self, n=0):
        self.c_cena = n
    
        
class Chao(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = chao
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (pos_x, pos_y)


class Vertice(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = vertice_img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (pos_x, pos_y)
    
    def update(self):
        pass


#Imagems

#sound_back = pygame.mixer.Sound("musica/drama1.wav")
#pygame.mixer.music.play(0)
#sound_back.set_volume(0.25)


#Sprite do chao

#Sprite do player
player_sprite = sprite.Group()

chao = Chao()
player_sprite.add(chao)

vertice = Vertice()
#player_sprite.add(vertice)

player = Player()
player_sprite.add(player)

#Grupo do NPC
npc_sprites =  sprite.Group()
amigo = NPC()
npc_sprites.add(amigo)


#Sprite do Fundo
obstaculos_sprites = sprite.Group()
vertice = Vertice()
obstaculos_sprites.add(vertice)


while True:
    #sound_back.play()
    FPS.tick(60)
    JANELA.fill((174, 249, 255))
    
    colisao = sprite.spritecollide(player, obstaculos_sprites, False, pygame.sprite.collide_mask)
    colisao_npc = sprite.spritecollide(player, npc_sprites, False, pygame.sprite.collide_mask)

    for event in pygame.event.get():

        mouse()

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
        else:
            pos_x = (LARGURA/2)
            pos_y = (ALTURA/2)
        
    if colisao_npc:
        pos_x -= 1
        pos_y -= 1

    obstaculos_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    npc_sprites.draw(JANELA)

    player_sprite.update()
    npc_sprites.update()

    display.flip()  
