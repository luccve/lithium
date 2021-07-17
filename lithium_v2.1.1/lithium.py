import pygame
from pygame import display, sprite, image, transform
from pygame import mixer
from pygame.draw import rect
from pygame.image import load
from pygame.locals import*
from random import randrange
from time import sleep
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

enter_img = image.load(os.path.join(pasta_imagens, 'enter.png')).convert_alpha
npc_img.set_colorkey([0, 0, 0])

#Teste de movimentação do fundo
def background():
    background = pygame.transform.scale(chao_img,(2560,1080))
    background_rect= background.get_rect()
    background_rect.x-=VELOCIDADE_PLAYER


    if background_rect.right <0:
        background_rect.x+= background_rect.width
    if background_rect.left >= 1280:
        background_rect.x-=background_rect.width

    JANELA.blit(background, background_rect)
    background_rect2 = background_rect.copy()
    if background_rect.left>0:
        background_rect2.x-=background_rect2.width
    else:
        background_rect2.x+= background_rect2.width
    JANELA.blit(background,background_rect2)

#Funções para ajustes
def mouse():
    global XeY
    if event.type == pygame.MOUSEBUTTONDOWN:
        XeY = pygame.mouse.get_pos()
        print(XeY)

def botao_ir():
    global JANELA,largura_rect,altura_rect,ponto_0_y,ponto_0_x,mouse_botao
    largura_rect = 20
    altura_rect = 20
    ponto_0_x = 800
    ponto_0_y = 750

    pygame.draw.rect(JANELA,(255,255,255),(650,580,20,20))
    

    mouse_botao = pygame.mouse.get_pos()
    x = mouse_botao[0]
    y = mouse_botao[1]
    
    if x < ponto_0_x + largura_rect and x > ponto_0_x and y < ponto_0_y + altura_rect and y > ponto_0_y:
        print('Deu certo')

#Funções das conversas
def textoscomfundo(txt = "",x_text=680,y_text=600):

    global enter_img
    pygame.draw.rect(JANELA, (0,0,0), (650,580,600,400))
    
    FONTE = pygame.font.SysFont('arial', 20, True, False)
    msg = txt
    render = FONTE.render(msg, True, (255,255,255))
    JANELA.blit(render,(x_text,y_text))

def only_txt(txt = "",x_text=680,y_text=630):
    FONTE = pygame.font.SysFont('arial', 20, True, False)
    msg = txt
    render = FONTE.render(msg, True, (255,255,255))
    JANELA.blit(render,(x_text,y_text))

#Classes
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

enter = 0
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

def mov_player():
    global colisao, event, x_player, y_player, VELOCIDADE_PLAYER, enter,mouse
    colisao = sprite.spritecollide(player, obstaculos_sprites, False, pygame.sprite.collide_mask)

    for event in pygame.event.get():

        #mouse()
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
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    enter+=1
                if event.key == pygame.K_BACKSPACE:
                    enter-=1
                
                    
        else:       
            x_player = (LARGURA/2)
            y_player = (ALTURA/2)


while True:
    #sound_back.play()
    FPS.tick(60)
    JANELA.fill((174, 249, 255))
    background()
    mov_player()

    colisao_npc = sprite.spritecollide(nicolau, player_sprite, False, pygame.sprite.collide_mask)
    
    if enter <1 or enter >5:
        enter=0
    
    
    obstaculos_sprites.draw(JANELA)
    ambiente_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    npcs_sprites.draw(JANELA)

    player_sprite.update(x_player,y_player)
    npcs_sprites.update()

  
    if colisao_npc:
        
        textoscomfundo('Aperte ENTER para falar com Nicolas',x_text=750,y_text=650)
        print(enter)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYUP or event.type == KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                textoscomfundo('Nicolas: Percebi que você vai entrar no labirinto.')
                only_txt('Quer ir junto?',y_text=630)
                only_txt('Acho que teremos mais chances...',y_text=660)
                if enter ==2:
                    textoscomfundo('O labirinto flamejante...')
                    only_txt('Fazia parte da cerimônia do Despertar')
                    only_txt('Onde todas as naçoes se reunião...',y_text=660)
                    '''Digite backspace para voltar'''
                    '''Botoes ENTER E BACKSPACE'''
                
                if enter ==3:
                    textoscomfundo('Na esperança que os jovens retornem.')
                    only_txt('E ao retornarem seram vistos como')
                    only_txt('membros produtivos da sociedade.',y_text=660)
                    '''Digite backspace para voltar'''
                if enter ==4:
                    textoscomfundo('Enya é uma aventureira solitária...')
                    only_txt('Mas a dificuldade do labirinto dar muito medo.')
                    only_txt('Vai acompanhar Nicolas?', y_text=660)
                    '''Digite esc para recusar'''
                if enter ==5:
                    enter = 0
                    JANELA.fill((255,255,255))
                    '''PROXÍMO ESTÁGIO'''

                                       
            if enter==4 and event.key == pygame.K_ESCAPE:
                JANELA.fill((0, 0, 0))
                textoscomfundo('Nicolas: Então ok.')
                
                
                    
                    
        
            
               
                

        
    display.flip()  
