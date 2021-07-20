import os
import pygame
from pygame import display, sprite, image, transform, mixer, draw
from pygame import rect
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
display.set_caption('Lithium')
JANELA = display.set_mode(TELA,0,32)
FPS = pygame.time.Clock()

#Constates
VELOCIDADE_PLAYER = 15
x_init_player = 950
y_init_player = 294
FLAG_CONTROL = True
n_caixa = 0

#Objetos
chao = construir.Ambiente((LARGURA/2), (ALTURA/2), imagem.chao_img)
portao = construir.Ambiente(312,218, imagem.portao_img)
pinheiro = construir.Ambiente(1024, 450, imagem.pinheiro_img)
arbusto = construir.Ambiente(1024, 200, imagem.arbusto_img)
player = construir.Player(x_init_player, y_init_player, 0, imagem.sprite_enya)
nicolau = construir.NPC(301, 314, 0, imagem.npc_img)
dialogo1 = construir.Textos(640, 600, imagem.dialogo_1_img, 4)

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
    
    #Definido colisões
    colisao_npc = sprite.spritecollide(nicolau, player_sprite, False, pygame.sprite.collide_mask)

    #Objetos na tela divididos por grupos
    
    fundo_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    npcs_sprites.draw(JANELA)
    frente_sprites.draw(JANELA)
    

    interacao.controlador(VELOCIDADE_PLAYER, FLAG_CONTROL, player, n_caixas = 3)


    if colisao_npc:
        n = interacao.n_enters()

        dialogo1.caixa(n)

        textos.add(dialogo1)
        textos.draw(JANELA)



    if 0 > player.rect.x or player.rect.x > 1280 or 0 > player.rect.y or player.rect.y > 720:
        player.rect.x = x_init_player
        player.rect.y = y_init_player


    player_sprite.update(player.rect.x,player.rect.y)
    npcs_sprites.update()
    textos.update()
    display.flip()  
