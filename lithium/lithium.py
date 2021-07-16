import pygame
from pygame import display, sprite, image, transform
from pygame import mixer
from pygame.draw import rect
from pygame.image import load
from pygame.locals import*
from random import randrange
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
x_player = LARGURA/2
y_player = ALTURA/2
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

chao_img = image.load(os.path.join(pasta_imagens, 'grama.png')).convert_alpha()
chao_img.set_colorkey([0, 0, 0])

vertice_img = image.load(os.path.join(pasta_imagens, 'vertice.png')).convert_alpha()
vertice_img.set_colorkey([0, 0, 0])

npc_img = image.load(os.path.join(pasta_imagens, 'npc.png')).convert_alpha()
npc_img.set_colorkey([0, 0, 0])

pinheiro_img = image.load(os.path.join(pasta_imagens, 'pinheiro.png')).convert_alpha()
npc_img.set_colorkey([0, 0, 0])



def mouse():
    global XeY
    if event.type == pygame.MOUSEBUTTONDOWN:
        XeY = pygame.mouse.get_pos()
        print(XeY)

def textos():
    pass

class Player(sprite.Sprite):
    #X e Y definimos a posição inicias nc = n de cena da sprite inicial
    def __init__(self, x, y, nc):
        sprite.Sprite.__init__(self)
        self.frames_enya = []
        for m in range(4):
            self.img = sprite_enya.subsurface((0 ,m*32),(30,32))
            self.frames_enya.append(self.img)
        self.c_cena = nc

        self.image = self.frames_enya[self.c_cena]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x, y)

    def movimento(self, n = 0):
        self.c_cena = n

    def update(self, x, y):
        self.image = self.frames_enya[self.c_cena]
        self.rect.center = (x, y)


class NPC(sprite.Sprite):
    #XeY definimos a posição e nc = número de cena
    def __init__(self, x, y, nc):
        sprite.Sprite.__init__(self)

        self.npc_lista = []
        for m in range(3):
            self.img = npc_img.subsurface((0, m*32), (30, 32))
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
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = vertice_img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (x_player, y_player)
    
    def update(self):
        pass


#Imagems

#sound_back = pygame.mixer.Sound("musica/drama1.wav")
#pygame.mixer.music.play(0)
#sound_back.set_volume(0.25)


#Grupos

ambiente_sprites = sprite.Group()
obstaculos_sprites = sprite.Group()
npcs_sprites = sprite.Group()
player_sprite = sprite.Group()


chao = Ambiente((LARGURA/2), (ALTURA/2), chao_img)
ambiente_sprites.add(chao)

pinheiros = []
for pin in range(2):
    x = 50
    y = 500

    for pin in range(10):
        x += 100
        pinheiros.append(Ambiente(x, y, pinheiro_img))
    
    x = 50
    y = 100

    for pin in range(10):
        x += 100
        pinheiros.append(Ambiente(x, y, pinheiro_img)) 


for p in pinheiros:
    ambiente_sprites.add(p)


limite = Limite_mov_player()
player = Player(x_player, y_player, 0)
nicolau = NPC(300, 300, 0)


#ambiente_sprites.add(limite)

obstaculos_sprites.add(limite)

player_sprite.add(player)

npcs_sprites.add(nicolau)




while True:
    #sound_back.play()
    FPS.tick(60)
    JANELA.fill((174, 249, 255))
    
    colisao = sprite.spritecollide(player, obstaculos_sprites, False, pygame.sprite.collide_mask)

    for event in pygame.event.get():

        mouse()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if colisao:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_player += VELOCIDADE_PLAYER
                    player.movimento(n=0)


                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_player -= VELOCIDADE_PLAYER
                    player.movimento(n=1)

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_player += VELOCIDADE_PLAYER
                    player.movimento(n=2)

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_player -= VELOCIDADE_PLAYER
                    player.movimento(n=3)
        else:
            x_player = (LARGURA/2)
            y_player = (ALTURA/2)

    colisao_npc = sprite.spritecollide(nicolau, player_sprite, False, pygame.sprite.collide_mask)
    if colisao_npc:
        x_player -= 1
        y_player -= 1
       

    obstaculos_sprites.draw(JANELA)
    ambiente_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    npcs_sprites.draw(JANELA)

    player_sprite.update(x_player,y_player)
    npcs_sprites.update()

    display.flip()  
