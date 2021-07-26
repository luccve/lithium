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

aranhaAtack = image.load(os.path.join(pasta_imagens, 'aranhaAtack.png')).convert_alpha()
aranhaMorte = image.load(os.path.join(pasta_imagens, 'aranhaMorte.png')).convert_alpha()

aranhaPoison =  image.load(os.path.join(pasta_imagens, 'poison.png')).convert_alpha()

fire_img = image.load(os.path.join(pasta_imagens, 'fire.png')).convert_alpha()

instrucoes_img = image.load(os.path.join(pasta_imagens, 'instrucoes.png')).convert_alpha()
creditos_img = image.load(os.path.join(pasta_imagens, 'creditos.png')).convert_alpha()

stage1 = image.load(os.path.join(pasta_imagens, 'stage1.png')).convert_alpha()
stage2 = image.load(os.path.join(pasta_imagens, 'stage2.png')).convert_alpha()
stage3 = image.load(os.path.join(pasta_imagens, 'stage3.png')).convert_alpha()

menu1 = image.load(os.path.join(pasta_imagens, '1.png')).convert_alpha()
menu2 = image.load(os.path.join(pasta_imagens, '2.png')).convert_alpha()
menu3 = image.load(os.path.join(pasta_imagens, '3.png')).convert_alpha()
menu4 = image.load(os.path.join(pasta_imagens, '4.png')).convert_alpha()
menu5 = image.load(os.path.join(pasta_imagens, '5.png')).convert_alpha()
menu6 = image.load(os.path.join(pasta_imagens, '6.png')).convert_alpha()

vida4 = image.load(os.path.join(pasta_imagens, 'vida4.png')).convert_alpha()
vida3 = image.load(os.path.join(pasta_imagens, 'vida3.png')).convert_alpha()
vida2 = image.load(os.path.join(pasta_imagens, 'vida2.png')).convert_alpha()
vida1 = image.load(os.path.join(pasta_imagens, 'vida1.png')).convert_alpha()

background2 =  image.load(os.path.join(pasta_imagens, 'background2.png')).convert_alpha()

background3 = image.load(os.path.join(pasta_imagens, 'background3.png')).convert_alpha()