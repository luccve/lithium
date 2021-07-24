#def fase_21():

#combat aranha ou cobra
import os

from pygame.constants import KEYDOWN, K_ESCAPE, K_r, QUIT
import restart
import mov_fase21
import construir
import imagem
import pygame
import interacao
from random import randint, randrange
from time import sleep, time

pygame.init()

#tela

screen = (1280,720)
JANELA = pygame.display.set_mode(screen,0,32)
pygame.display.set_caption('Lithium')
FPS = pygame.time.Clock()


#Constantes
x_init_player = 1100
y_init_player = 360
lista_skeleton = list()
pontos = 0 #CONTADOR DE MONSTROS QUE MORRERAM
speed = 60 #FPS
mov = 1 #VELOCIDADE DO EIXO X DOS MONSTROS
passou = 0 #CONTADOR DE MONSTROS QUE PASSARAM


#Grupos
monstros = pygame.sprite.Group()
sprite_player = pygame.sprite.Group()
npcs = pygame.sprite.Group()
trap_group = pygame.sprite.Group()#O grupo será usado pelo controlador para desenhar as setas

#Aparecer aleatoríamente os 6 esqueletos
for i in range(6):
    skeleton = construir.Monster(0, 0)
    lista_skeleton.append(skeleton)
    monstros.add(skeleton)
    

#Objetos
player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
nicolau = construir.NPC(1100, 300, 0, imagem.npc_img)


#Adicionando 

sprite_player.add(player)
npcs.add(nicolau)


while True:
    #Desenhando
    FPS.tick(speed)
    JANELA.fill((0, 0, 0))

    for skeleto in lista_skeleton:
        colisao_spear = pygame.sprite.spritecollide(skeleto, trap_group, True, pygame.sprite.collide_mask)
        if colisao_spear:
            
            pontos += 1
            passou-=1

            monstros.remove(skeleto)
            lista_skeleton.remove(skeleto)

            skeleton = construir.Monster(0, 0)
            lista_skeleton.append(skeleton)
            monstros.add(skeleton)
        
        if skeleto.rect.x == 1200:
            pontos -= 1
            passou+=1
    
    #Condições de Game Over
    if passou > 5:
        JANELA.fill((0, 0, 0))
        interacao.textoscomfundo(f'Já passaram {passou} Esqueletos.',200,20)
    if passou >10:
        pontos=0
        passou=0
        restart.gameover(JANELA,trap_group,player) 
        
    if pontos >=20:
        mov = 2
    if pontos >=50:
        mov = 3

    colisao_player = pygame.sprite.spritecollide(player, monstros, True, pygame.sprite.collide_mask)
    if colisao_player:
        pontos=0
        passou=0
        restart.gameover(JANELA,trap_group,player)
        
        '''Função restart'''
               
    sprite_player.draw(JANELA)
    npcs.draw(JANELA)
    monstros.draw(JANELA)

    mov_fase21.controlador(trap_group,VELOCIDADE=50 ,player = player)
    interacao.textoscomfundo(f"PONTOS: {pontos}", 1000, 50)

    sprite_player.update()
    npcs.update()
    monstros.update(mov)
    pygame.display.flip() 

#fase_21()