import os
import pygame
from pygame import display, sprite, image, transform,draw,mixer
from pygame import rect
from pygame.locals import*
from random import randrange
import construir
import imagem


pygame.init()

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'sprites')
pasta_sons = os.path.join(pasta_principal, 'musica')

#Variavéis
FONTE1 = pygame.font.SysFont("Chiller", 40, True, False)

enter = 0
m = 1

'''O controle importado do arquivo interacao, recebe a velocidade de movimentação, a flag que o funcionamento dos controles,e o objeto a ser controlado nesse caso o player'''

def controlador(grupo, VELOCIDADE = 10, FLAG_CONTROL = True, player = object, FLAG_TEXTO = True, max_caixas = 4):

    global enter, m

    grupo.draw(display.get_surface())
    grupo.update()


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            XeY = pygame.mouse.get_pos()
            print(XeY)
            
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Cordenação de movimentos na tela

        if FLAG_CONTROL:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.rect.y += VELOCIDADE
                    player.movimento(n=0)
                    
    

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.rect.x -= VELOCIDADE
                    player.movimento(n=1)
                    
                    

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.rect.x += VELOCIDADE
                    player.movimento(n=2)
                    
                    

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.rect.y -= VELOCIDADE
                    player.movimento(n=3)
                    

                if event.key == pygame.K_SPACE:
                    
                    trap = construir.Trap(player, 0)                                                        
                    grupo.add(trap)
                    
                
                #Controladores de dialógos
                if FLAG_TEXTO:

                    if event.key == pygame.K_RETURN:
                        enter += 1

                    if event.key == pygame.K_BACKSPACE:
                        enter -= 1
                else:
                    enter = 0

                if enter == 3:

                    if event.key == pygame.K_ESCAPE:
                        print("Estágio 2")
                    
                    elif event.key == pygame.K_SPACE:
                        print("Estágio 2.1")

        else:
            player.rect.x = 733
            player.rect.y = 662
        
    if enter < 0 or enter > max_caixas:
        enter = 0
    
    
        
def n_enters():
    global enter
    return enter

def textoscomfundo(msg='', x = 680, y = 600):
    #pygame.draw.rect(display.get_surface(), (0, 0, 0), (650, 580, 600, 400))
    texte_render = FONTE1.render(msg, True, (255,255,255))
    display.get_surface().blit(texte_render, (x, y))
