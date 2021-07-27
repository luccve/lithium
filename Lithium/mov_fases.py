#imports
import pygame
import os
import fases
import imagem
import construir
import som
from pygame import display
from pygame.locals import*


pygame.init()

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'sprites')
pasta_sons = os.path.join(pasta_principal, 'musica')

#Variavéis
enter = 0
m = 1

#SFX


'''Todas funcoes de movimentação, recebe a velocidade de movimentação, a flag que o funcionamento dos controles,e o objeto a ser controlado nesse caso o player'''

def movfase1(VELOCIDADE = 10, FLAG_CONTROL = True, player = object, FLAG_TEXTO = True, max_caixas = 4):

    global enter


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
                        fases.fase_22()
                    
                    elif event.key == pygame.K_SPACE:
                        fases.fase_21()

        else:
            player.rect.x = 733
            player.rect.y = 662
        
    if enter < 0 or enter > max_caixas:
        enter = 0
    
  
def movfase21(grupo, VELOCIDADE = 10, FLAG_CONTROL = True, player = object, FLAG_TEXTO = True, max_caixas = 4):

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
                    som.trap.set_volume(0.15)
                    som.trap.play()
                    
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


def movfase22(grupo, VELOCIDADE = 10, FLAG_CONTROL = True, player = object, FLAG_TEXTO = True, max_caixas = 4):

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
                    som.fire.set_volume(0.25)
                    som.fire.play()
                    spear = construir.Projetil(player, imagem.fire_img, 52, 55, 4, -3)                                               
                    grupo.add(spear)
                    
                
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

