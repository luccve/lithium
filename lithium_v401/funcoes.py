import os
import pygame
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

'''O controle importado do arquivo interacao, recebe a velocidade de movimentação, a flag que o funcionamento dos controles,e o objeto a ser controlado nesse caso o player'''



def texto(msg='', x = 680, y = 600,fonte='arial', tamanho=40):
    #pygame.draw.rect(display.get_surface(), (0, 0, 0), (650, 580, 600, 400))
    FONTE1 = pygame.font.SysFont(fonte, tamanho, True, False)
    texte_render = FONTE1.render(msg, True, (255,255,255))
    display.get_surface().blit(texte_render, (x, y))

def gameover(screen,grupo,player,die=True):
    
    while die:
            screen.fill((0,0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        grupo.empty()
                        player.rect.x = 1100
                        player.rect.y = 360
                        
                        die = False
                        
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()

            
            texto('Game Over! Pressione a tecla R para jogar novamente.',100,100)
            texto('Pressione a tecla ESC para jogar sair do jogo.',300,300)         
            pygame.display.update()

