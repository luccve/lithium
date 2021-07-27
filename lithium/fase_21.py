

#combat skeleton

from pygame import sprite
from pygame.constants import KEYDOWN, K_ESCAPE, K_r, QUIT
import mov_fases
import construir
import imagem
import pygame
import funcoes


pygame.init()


def fase_21():
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
    mov = 3 #VELOCIDADE DO EIXO X DOS MONSTROS
    passou = 0 #CONTADOR DE MONSTROS QUE PASSARAM
    FLAG_TERMINOU_D2 = False

    #Grupos
    fundo_grup = sprite.Group()
    monstros = pygame.sprite.Group()
    sprite_player = pygame.sprite.Group()
    npcs = pygame.sprite.Group()
    trap_group = pygame.sprite.Group()#O grupo será usado pelo controlador para desenhar as setas
    textos = sprite.Group()
    

    #Criando aleatoríamente 6 esqueletos
    for i in range(6):
        skeleton = construir.Monster(0, 0)
        lista_skeleton.append(skeleton)
        monstros.add(skeleton)
        

    #Objetos
    player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
    nicolau = construir.NPC(1100, 300, 0, imagem.npc_img)
    d2 = construir.Textos(640, 360, imagem.dialogo_2_img, 2)
    background = construir.Ambiente(640, 360, imagem.background2)


    #Adicionando objetos ao grupo

    sprite_player.add(player)
    npcs.add(nicolau)
    textos.add(d2)
    fundo_grup.add(background)


    #Game
    while True:
        
        FPS.tick(speed)
        JANELA.fill((0, 0, 0))
        fundo_grup.draw(JANELA)

        mov_fases.movfase21(trap_group,VELOCIDADE=50 ,player = player, FLAG_TEXTO=True, max_caixas=1)

        n = mov_fases.n_enters()

        d2.caixa(n)

        
        textos.draw(JANELA)

        if n > 0:
            FLAG_TERMINOU_D2 = True
            textos.remove(d2)

        #O jogo começa depois do start inicial
        if FLAG_TERMINOU_D2:
            for skeleto in lista_skeleton:

                colisao_trap_monstro = pygame.sprite.spritecollide(skeleto, trap_group, True, pygame.sprite.collide_mask)

                if colisao_trap_monstro:
                    
                    pontos += 1
                    
                    #Realocando objetos da memoria
                    monstros.remove(skeleto)
                    lista_skeleton.remove(skeleto)

                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)
                
                if skeleto.rect.x == 1200:
                    
                    passou+=1

            #Desenhando objetos
            sprite_player.draw(JANELA)
            npcs.draw(JANELA)
            monstros.draw(JANELA)
        

            #Aumentando a dificuldade
            if pontos >= 20:
                mov = 6
            if pontos >= 50:
                mov = 10
 

            #Avisos
            funcoes.texto(f"PONTOS: {pontos}", 1000, 50)
            funcoes.texto(f'Já passaram {passou} de 11 Esqueletos. Para Game Over!.',150,20,fonte='arial',tamanho=22)

            #Condições de Game Over
            if passou > 10:
                pontos=0
                passou=0
                monstros.empty()
                lista_skeleton = []

                funcoes.gameover(JANELA,trap_group,player) 

                '''Função restart'''

                #Recontruindo os esquelestos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            colisao_player_monstro = pygame.sprite.spritecollide(player, monstros, True, pygame.sprite.collide_mask)

            if colisao_player_monstro:
                pontos = 0
                passou = 0
                monstros.empty()
                lista_skeleton = []

                funcoes.gameover(JANELA, trap_group, player)

                '''Função restart'''

                #Recontruindo os esquelestos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            #Condição de vitória 
            if pontos > 100:
                pontos = 0
                passou = 0
                trap_group.empty()
                monstros.empty()
                lista_skeleton= []

                funcoes.victory(player)

                #Recontruindo os esqueletos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            #Atualizando objetos dando movimentação
            sprite_player.update()
            npcs.update()
            monstros.update(mov)

        #Atualizando
        pygame.display.flip() 


