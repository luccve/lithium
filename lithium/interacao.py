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
enter = 0

'''O controle importado do arquivo interacao, recebe a velocidade de movimentação, a flag que o funcionamento dos controles,e o objeto a ser controlado nesse caso o player'''

def controlador(VELOCIDADE_PLAYER, FLAG_CONTROL, player, n_caixas = 3):
    global enter

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

                
                if event.key == pygame.K_1:
                    enter += 1

                if event.key == pygame.K_2:
                    enter -= 1

        else:
            player.rect.x = 733
            player.rect.y = 662
        
    if enter < 0 or enter > n_caixas:
        enter = 0
        
def n_enters():
    global enter
    return enter


