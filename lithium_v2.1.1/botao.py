import pygame
from pygame.constants import MOUSEBUTTONDOWN

screen = pygame.display.set_mode((1280,720))

ponto_0_x = 640
ponto_0_y = 360

BRANCO = (255,255,255)

largura_rect = 20
altura_rect = 20
mouse = 0
while True:
    pygame.draw.rect(screen,BRANCO,(ponto_0_x,ponto_0_y,largura_rect,altura_rect))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            x = mouse[0]
            y = mouse[1]
            
            if x < ponto_0_x + largura_rect and x > ponto_0_x and y < ponto_0_y + altura_rect and y > ponto_0_y:
                print('Deu certo')
            
            
            
    



    pygame.display.flip()