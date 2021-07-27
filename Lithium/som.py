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
fire = pygame.mixer.Sound(os.path.join(pasta_sound, 'fire.wav'))
trap = pygame.mixer.Sound(os.path.join(pasta_sound, 'trap.wav'))
skeleton = pygame.mixer.Sound(os.path.join(pasta_sound, 'skeleton.wav'))
skeleton_die = pygame.mixer.Sound(os.path.join(pasta_sound, 'die_skeleton.wav'))
hit_spider = pygame.mixer.Sound(os.path.join(pasta_sound, 'hit_spider.wav'))
fire_hit = pygame.mixer.Sound(os.path.join(pasta_sound, 'fire_hit.wav'))
morreu = pygame.mixer.Sound(os.path.join(pasta_sound, 'morreu.wav'))

#SFX BACKGROUND
fase21 = pygame.mixer.music.load(os.path.join(pasta_sound, 'fase21.wav'))
fase22 = pygame.mixer.music.load(os.path.join(pasta_sound, 'fase22.wav'))