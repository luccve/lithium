import pygame
from pygame.constants import KEYDOWN, K_ESCAPE, K_r, QUIT
import interacao   

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

            interacao.textoscomfundo('O esqueleto lhe atingiu.') 
            interacao.textoscomfundo('Game Over! Pressione a tecla R para jogar novamente.',100,100)
            interacao.textoscomfundo('Pressione a tecla ESC para jogar sair do jogo.',300,300)         
            pygame.display.update()


def gameover2(screen, player, die=True):

    while die:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    player.rect.x = 1100
                    player.rect.y = 360

                    die = False

                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

        interacao.textoscomfundo('O esqueleto lhe atingiu.')
        interacao.textoscomfundo(
            'Game Over! Pressione a tecla R para jogar novamente.', 100, 100)
        interacao.textoscomfundo(
            'Pressione a tecla ESC para jogar sair do jogo.', 300, 300)
        pygame.display.update()
