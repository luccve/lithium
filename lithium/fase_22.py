#combat aranha ou cobra

from pygame import sprite
from pygame import display
from pygame.constants import KEYDOWN, K_ESCAPE, K_r, QUIT
from pygame.display import list_modes
import mov_fases
import construir
import imagem
import pygame
import funcoes
from random import randint


pygame.init()


def fase_22():
    #tela

    screen = (1280,720)
    JANELA = pygame.display.set_mode(screen,0,32)
    pygame.display.set_caption('Lithium')
    FPS = pygame.time.Clock()


    #Constantes
    x_init_player = 1100
    y_init_player = 360
    
    pontos = 0 #CONTADOR DE MONSTROS QUE MORRERAM
    speed = 120 #FPS
    mov = 3 #VELOCIDADE DO EIXO Y DOS MONSTROS
    
    FLAG_TERMINOU_D2 = False

    #Grupos
    sprite_player = sprite.Group()
    textos = sprite.Group()
    bossAranha =  sprite.Group()
    poisonAranha = sprite.Group()
    spear_grupo = sprite.Group()
    fundo_grup = sprite.Group()

        

    #Objetos
    player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
    aranha =  construir.Aranha(245, 0,mov)
    d2 = construir.Textos(640, 360, imagem.dialogo_2_img, 2)
    poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)
    background = construir.Ambiente(640, 360, imagem.background3)


    #Adicionando 

    sprite_player.add(player)
    bossAranha.add(aranha)
    poisonAranha.add(poison)
    textos.add(d2)
    fundo_grup.add(background)



    while True:
        #Desenhando
        FPS.tick(speed)
        JANELA.fill((0, 0, 0))
        fundo_grup.draw(JANELA)

        mov_fases.movfase22(spear_grupo,VELOCIDADE=50 ,player = player, FLAG_TEXTO=True, max_caixas=1)

        n = mov_fases.n_enters()

        d2.caixa(n)

        textos.draw(JANELA)

        if n > 0:
            FLAG_TERMINOU_D2 = True
            textos.remove(d2)


        if FLAG_TERMINOU_D2: 

            #Colisoes da aranha com o player
            colisao_aranha = pygame.sprite.spritecollide(player, bossAranha, False, pygame.sprite.collide_mask)
            colisao_poison = pygame.sprite.spritecollide(player, poisonAranha, False, pygame.sprite.collide_mask)

            #Colisões do ataque do player com a aranha
            colisao_fire1 = pygame.sprite.spritecollide(aranha, spear_grupo, True, pygame.sprite.collide_mask)

            #Condições de vitória
            if colisao_fire1:
                pontos += 10
                if pontos == 100:
                    bossAranha.empty()
                    poisonAranha.empty()
                    #display.get_surface().blit(imagem.backgroundVictory, (0,0))

            #Condições de Restart
            if colisao_aranha:
                funcoes.gameover(JANELA,poisonAranha,player)
                pontos = 0
                spear_grupo.empty()
            if colisao_poison:
                funcoes.gameover(JANELA,poisonAranha, player)
                pontos = 0
                spear_grupo.empty()

            #Inteligência de ataque da Aranha
            if pontos < 100:
                if aranha.rect.centery == player.rect.centery or aranha.rect.centery == player.rect.centery+randint(1,100) or aranha.rect.centery == player.rect.centery - randint(1, 100):
                    poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)
                    poisonAranha.add(poison)
                    
            #Remover objetos para otimizar a memória
            if poison.rect.x > 1280:
                poisonAranha.remove(poison)
            

            sprite_player.draw(JANELA)
            bossAranha.draw(JANELA)
            spear_grupo.draw(JANELA)
            poisonAranha.draw(JANELA)

            if pontos <= 25 and pontos >0:
                JANELA.blit(imagem.vida4,(500,50))
                #funcoes.texto(f"{int(abs((pontos/100*100)-100))}%", 750, 50,tamanho=30)
            if pontos <= 50 and pontos > 25:
                JANELA.blit(imagem.vida3,(500,50))
                
            if pontos <= 75 and pontos > 50:
                JANELA.blit(imagem.vida2,(500,50))
                
            if pontos <= 99 and pontos > 75:
                JANELA.blit(imagem.vida1,(500,50))
                
            
            sprite_player.update()
            bossAranha.update()
            poisonAranha.update()
            spear_grupo.update()

        pygame.display.flip() 

