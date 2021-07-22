import os
import pygame
from pygame import display, sprite, image, transform, mixer, draw
from pygame.locals import*
from random import randrange
import construir
import interacao
import imagem

pygame.init()

'''
imagems 
-> O arquivo imagem fica resposável por ser um banco de todas as imagens dentro do jogo

construir
-> O arquivo contruir importa todas as classes contruturas necessárias naquela fase especifica do jogo

interacao
-> Esse arquivo guarda todas as nossas funcaoes que forem ser necessarias ao longo das fases do jogo

'''

#Display
LARGURA = 1280
ALTURA = 720
TELA = (1280, 720)
display.set_caption('Líthium')
JANELA = display.set_mode(TELA,0,32)
FPS = pygame.time.Clock()


#Teste move background
ASD = imagem.chao_img
bg = pygame.transform.scale(ASD, (2560, 1440))
screen_size = JANELA.get_size()
bg_size = bg.get_size()

bg_x = (bg_size[0]-screen_size[0]) // 2
bg_y = (bg_size[1]-screen_size[1]) // 2


#Posicoes NPCs
x_npc = 301
y_npc = 314


#Constates
VELOCIDADE_PLAYER = 15
x_init_player = 950
y_init_player = 294
FLAG_CONTROL = True

#Objetos
chao = construir.Ambiente((LARGURA/2), (ALTURA/2), imagem.chao_img)
portao = construir.Ambiente(312,218, imagem.portao_img)
pinheiro = construir.Ambiente(1024, 450, imagem.pinheiro_img)
arbusto = construir.Ambiente(1024, 200, imagem.arbusto_img)
player = construir.Player(x_init_player, y_init_player, 0, imagem.sprite_enya)
nicolau = construir.NPC(x_npc, y_npc, 0, imagem.npc_img)
dialogo1 = construir.Textos(640, 600, imagem.dialogo_1_img, 4)

#Teste move NPC
nicolau1 = imagem.npc_img
nicolau_size = nicolau1.get_size()
print(nicolau_size)
x_npc = (nicolau_size[0]-screen_size[0]) // 2
y_npc = (nicolau_size[1]-screen_size[1]) // 2

#Formando os Grupos
fundo_sprites = sprite.Group()
frente_sprites = sprite.Group()
textos = sprite.Group()
npcs_sprites = sprite.Group()
player_sprite = sprite.Group()


#Adicionando aos grupos
fundo_sprites.add(chao)
frente_sprites.add(portao)
frente_sprites.add(pinheiro)
frente_sprites.add(arbusto)


player_sprite.add(player)
npcs_sprites.add(nicolau)


while True:
    FPS.tick(60)
    JANELA.fill((0, 0, 0))
    

    #move background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bg_x -= 10
        bg_x-=10
    if keys[pygame.K_RIGHT]:
        bg_x += 10
        bg_x+=10
    if keys[pygame.K_UP]:
        bg_y -= 10
        y_npc -=10
    if keys[pygame.K_DOWN]:
        bg_y += 10
        y_npc+=10
    bg_x = max(0, min(bg_size[0]-screen_size[0], bg_x)) 
    bg_y = max(0, min(bg_size[1]-screen_size[1], bg_y))

    JANELA.blit(bg, (-bg_x, -bg_y))
    JANELA.blit(nicolau1,(-x_npc,-y_npc))



    #Definido colisões
    colisao_npc = sprite.spritecollide(nicolau, player_sprite, False, pygame.sprite.collide_mask)

    #Objetos na tela divididos por grupos
    
    #fundo_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    #npcs_sprites.draw(JANELA)
    #frente_sprites.draw(JANELA)

    interacao.controlador(VELOCIDADE_PLAYER, FLAG_CONTROL, player)

    
    #Condições

    if colisao_npc:

        textos.add(dialogo1)
        textos.draw(JANELA)


    if 0 > player.rect.x or player.rect.x > 1280 or 0 > player.rect.y or player.rect.y > 720:
        player.rect.x = x_init_player
        player.rect.y = y_init_player

    
    player_sprite.update(player.rect.x,player.rect.y)
    #npcs_sprites.update()
    
    display.flip()  
