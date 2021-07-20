import os
import pygame
from pygame import display, sprite, image, transform,draw,mixer
from pygame.locals import*
from random import randrange

pygame.init()

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'sprites')
pasta_sons = os.path.join(pasta_principal, 'musica')

#Variavéis
FONTE1 = pygame.font.SysFont("Arial", 20, True, False)

'''O controle importado do arquivo interacao, recebe a velocidade de movimentação, a flag que o funcionamento dos controles,e o objeto a ser controlado nesse caso o player'''

def controlador(VELOCIDADE_PLAYER, FLAG_CONTROL, player):
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            XeY = pygame.mouse.get_pos()
            print(XeY)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if FLAG_CONTROL:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.rect.y += VELOCIDADE_PLAYER
                    player.movimento(n=0)

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.rect.x -= VELOCIDADE_PLAYER
                    player.movimento(n=1)

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.rect.x += VELOCIDADE_PLAYER
                    player.movimento(n=2)

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.rect.y -= VELOCIDADE_PLAYER
                    player.movimento(n=3)
        else:
            player.rect.x = 733
            player.rect.y = 662


def textoscomfundo(msg='', x = 680, y = 600):
    pygame.draw.rect(display.get_surface(), (0, 0, 0), (650, 580, 600, 400))
    texte_render = FONTE1.render(msg, True, (255,255,255))
    display.get_surface().blit(texte_render, (x, y))


def only_txt(JANELA,txt="", x_text=680, y_text=630):
    FONTE = pygame.font.SysFont('arial', 20, True, False)
    msg = txt
    render = FONTE.render(msg, True, (255, 255, 255))
    JANELA.blit(render, (x_text, y_text))
