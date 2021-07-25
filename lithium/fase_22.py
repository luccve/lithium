#def fase_21():

#combat aranha ou cobra

from pygame import sprite
from pygame.constants import KEYDOWN, K_ESCAPE, K_r, QUIT
from pygame.display import list_modes
import restart
import mov_fase22
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
speed = 120 #FPS
mov = 3 #VELOCIDADE DO EIXO Y DOS MONSTROS
passou = 0 #CONTADOR DE MONSTROS QUE PASSARAM
FLAG_TERMINOU_D2 = False

#Grupos
sprite_player = sprite.Group()
trap_group = sprite.Group()#O grupo será usado pelo controlador para desenhar as setas
textos = sprite.Group()
bossAranha =  sprite.Group()
poisonAranha = sprite.Group()
spear_grupo = sprite.Group()

    

#Objetos
player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
aranha =  construir.Aranha(245, 0,mov)
d2 = construir.Textos(640, 360, imagem.dialogo_2_img, 2)
poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)



#Adicionando 

sprite_player.add(player)
bossAranha.add(aranha)
poisonAranha.add(poison)
textos.add(d2)



while True:
    #Desenhando
    FPS.tick(speed)
    JANELA.fill((0, 0, 0))

    mov_fase22.controlador(spear_grupo,VELOCIDADE=50 ,player = player, FLAG_TEXTO=True, max_caixas=1)

    n = mov_fase22.n_enters()

    d2.caixa(n)

    textos.draw(JANELA)

    if n > 0:
        FLAG_TERMINOU_D2 = True
        textos.remove(d2)


    if FLAG_TERMINOU_D2: 

        #Tipos de Colisão
        colisao_aranha = pygame.sprite.spritecollide(player, bossAranha, False, pygame.sprite.collide_mask)
        colisao_poison = pygame.sprite.spritecollide(player, poisonAranha, False, pygame.sprite.collide_mask)

        #Colisões do fire
        colisao_fire1 = pygame.sprite.spritecollide(aranha, spear_grupo, False, pygame.sprite.collide_mask)

        #Condições de Colisão
        if colisao_fire1:
            pontos += 1
            if pontos == 100:
                bossAranha.empty()
                poisonAranha.empty()

        #Condições de Restart
        if colisao_aranha:
            restart.gameover(JANELA,poisonAranha,player)
            pontos = 0
        if colisao_poison:
            restart.gameover(JANELA,poisonAranha, player)
            pontos = 0

        #Inteligência de ataque da Aranha
        if pontos < 100:
            if aranha.rect.centery == player.rect.centery or aranha.rect.centery == player.rect.centery+randint(1,100) or aranha.rect.centery == player.rect.centery - randint(1, 100):
                poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)
                poisonAranha.add(poison)

        if poison.rect.x > 1280:
            poisonAranha.remove(poison)
        

        sprite_player.draw(JANELA)
        bossAranha.draw(JANELA)
        spear_grupo.draw(JANELA)
        poisonAranha.draw(JANELA)

        if pontos < 100:
            interacao.textoscomfundo(f"Vida Restante: {abs((pontos/100*100)-100):.2f}%", 800, 50)

        sprite_player.update()
        bossAranha.update()
        poisonAranha.update()
        spear_grupo.update()

    pygame.display.flip() 
