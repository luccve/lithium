import pygame
import imagem
import som
import fases
from pygame.locals import *
from sys import exit


LARGURA = 1280
ALTURA = 720
FPS = 30

selecao = 0
intro = 0
fase = 1

#Music
menusom = som.menu_som
menusom2 = som.esc_som
enter_menu = som.enter_som
save = som.startfase_som

menusom.set_volume(0.1)
menusom2.set_volume(0.1)
enter_menu.set_volume(0.1)
save.set_volume(0.25)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((LARGURA, ALTURA), 0, 32)
botao_enter = False


def tela():
    return screen.fill((0, 0, 0))

def instrucoes():
        
    flag_instrucoes = True
    while flag_instrucoes:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    flag_instrucoes = False
              
        screen.blit(imagem.instrucoes_img, (0, 0))
        pygame.display.update()

def stage():
    global fase
    
    flag_fase = True
    while flag_fase:
        tela()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    fase=0
                    flag_fase = False
                if event.key == K_LEFT or event.key == K_a:
                    fase-=1
                    menusom2.play()
                if event.key == K_RIGHT or event.key == K_d:
                    fase+=1
                    menusom2.play()
                if event.key == K_RETURN:
                    save.play()
                    if fase == 1:
                        fases.fase_1()
                    if fase == 2:
                        fases.fase_21()
                    if fase == 3:
                        fases.fase_22()
        
        #Implementação da fase 
        if fase > 3:
            fase = 1
        if fase < 1:
            fase = 3   
        if fase == 1:
            tela()
            screen.blit(imagem.stage1, (0, 0))

        if fase == 2:
            tela()
            screen.blit(imagem.stage2, (0, 0))

        if fase == 3:
            tela()
            screen.blit(imagem.stage3, (0, 0))
        pygame.display.flip()

def f_creditos():

    creditos_menu = True
    while creditos_menu:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    creditos_menu = False
        screen.blit(imagem.creditos_img, (0, 0))
        pygame.display.update()


def events():
    global selecao,intro,fase
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_s or event.key == K_DOWN:
                menusom.play()
                selecao += 1
            if event.key == K_w or event.key == K_UP:
                selecao -= 1
                menusom.play()
            if event.key == K_ESCAPE:
                menusom.play()
                pygame.quit()
                exit()
            if event.key == K_SPACE or event.key == K_RETURN:
                intro +=1
                
                if selecao == 1:#Novo jogo
                    enter_menu.play()
                    fases.fase_1()
                if selecao == 2:#Creditos
                    enter_menu.play()
                    f_creditos()
                if selecao == 3:#Instruções
                    enter_menu.play()
                    instrucoes()
                if selecao == 4:#Fases
                    enter_menu.play()
                    stage()

                if selecao == 5:#Configurações
                    pass
                    '''Em construção'''
                if selecao == 6:#Sair
                    pygame.quit()
                    exit()

def menu():
    global selecao
    if intro == 0:
        
        tela()
        screen.blit(imagem.creditos_img, (0, 0))
    else:
        if selecao == 1:

            tela()

            screen.blit(imagem.menu1, (0, 0))

        if selecao == 2:

            tela()

            screen.blit(imagem.menu2, (0, 0))

        if selecao == 3:

            tela()

            screen.blit(imagem.menu3, (0, 0))

        if selecao == 4:

            tela()

            screen.blit(imagem.menu4, (0, 0))

        if selecao == 5:

            tela()
            screen.blit(imagem.menu5, (0, 0))

        if selecao == 6:
            tela()
            screen.blit(imagem.menu6, (0, 0))


        if selecao < 1:
            selecao = 6

        if selecao >= 7:
            selecao = 1

        

while True:
    tela()
    
    events()
    menu()

    pygame.display.flip()
