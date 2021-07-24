import os
import pygame
from pygame import display, sprite, image, transform
from pygame.locals import*


pygame.init()

#Diretórios
pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'sprites')

'''OBS: Deve-se definir um display exatemente igual ao do jogo para que as imagens possa ser
impotadas de maneira proporcional evitando erros'''

#Display
TELA = (1280, 720)
display.set_caption('Lithium')
JANELA = display.set_mode(TELA,0,32)
FPS = pygame.time.Clock()


#imagens
sprite_enya = image.load(os.path.join(pasta_imagens, 'enya.png')).convert_alpha()
sprite_enya.set_colorkey([0, 250, 0])

fundo_img = image.load(os.path.join(pasta_imagens, 'grama.png')).convert_alpha()
fundo_img.set_colorkey([0, 0, 0])

vertice_img = image.load(os.path.join(pasta_imagens, 'vertice.png')).convert_alpha()
vertice_img.set_colorkey([0, 0, 0])

npc_img = image.load(os.path.join(pasta_imagens, 'npc.png')).convert_alpha()
npc_img.set_colorkey([0, 0, 0])

pinheiro_img = image.load(os.path.join(pasta_imagens, 'pinheiro.png')).convert_alpha()
npc_img.set_colorkey([0, 0, 0])

portao_img = image.load(os.path.join(pasta_imagens, 'portão.png')).convert_alpha()

arbusto_img = image.load(os.path.join(pasta_imagens, 'arbusto.png')).convert_alpha()

dialogo_1_img = image.load(os.path.join(pasta_imagens, 'd1.png')).convert_alpha()

dialogo_2_img = image.load(os.path.join(pasta_imagens, 'd2.png')).convert_alpha()

skeleto_walk = image.load(os.path.join(pasta_imagens, 'Skeleton.png')).convert_alpha()
skeleto_walk.set_colorkey([0, 0, 0])

skeleto_dead = image.load(os.path.join(pasta_imagens, 'Skeletondead.png')).convert_alpha()

skeleto_hit = image.load(os.path.join(pasta_imagens, 'Skeletonhit.png')).convert_alpha()

spearL = image.load(os.path.join(pasta_imagens, 'SpearL.png')).convert_alpha()
spearR = image.load(os.path.join(pasta_imagens, 'SpearR.png')).convert_alpha()
spearT = image.load(os.path.join(pasta_imagens, 'SpearT.png')).convert_alpha()
spearB = image.load(os.path.join(pasta_imagens, 'SpearB.png')).convert_alpha()

trap = image.load(os.path.join(pasta_imagens, 'Trap.png')).convert_alpha()
npc_img.set_colorkey([255, 255, 255])