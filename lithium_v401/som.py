import pygame
import os

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_sound = os.path.join(pasta_principal, 'sound')


#SFX
menu_som = pygame.mixer.Sound(os.path.join(pasta_sound, 'menu.wav'))
esc_som = pygame.mixer.Sound(os.path.join(pasta_sound, 'menu2.wav'))
enter_som = pygame.mixer.Sound(os.path.join(pasta_sound, 'startgame.wav'))
startfase_som = pygame.mixer.Sound(os.path.join(pasta_sound, 'save.wav'))



#SFX BACKGROUND
#menu_som = pygame.mixer.music.load(os.path.join(pasta_sound, 'menu.wav'))
#start_som = pygame.mixer.music.load(os.path.join(pasta_sound, 'startgame.wav'))