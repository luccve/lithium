#def fase_21():

#combat aranha ou cobra
from pygame import sprite
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
pontos = 0

#Grupos
monstros = sprite.Group()
sprite_player = sprite.Group()
npcs = sprite.Group()
spear_grup = sprite.Group()#O grupo será usado pelo controlador para desenhar as setas

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
    FPS.tick(60)
    JANELA.fill((0, 0, 0))

    for skeleto in lista_skeleton:
        colisao_spear = sprite.spritecollide(skeleto, spear_grup, True, sprite.collide_mask)
        if colisao_spear:
            
            pontos += 1
            player.rect.x -= 30

            monstros.remove(skeleto)
            lista_skeleton.remove(skeleto)

            skeleton = construir.Monster(0, 0)
            lista_skeleton.append(skeleton)
            monstros.add(skeleton)
        
        if skeleto.rect.x == 1200:
            pontos -= 1
    
    #Condições de Game Over
    if pontos < -5:
        break

    colisao_player = sprite.spritecollide(player, monstros, True, sprite.collide_mask)
    if colisao_player:
        break
                       
    sprite_player.draw(JANELA)
    npcs.draw(JANELA)
    monstros.draw(JANELA)

    interacao.controlador(spear_grup,VELOCIDADE=50 ,player = player)
    interacao.textoscomfundo(f"PONTOS: {pontos}", 1000, 100)

    sprite_player.update()
    npcs.update()
    monstros.update()
    pygame.display.flip() 

#fase_21()