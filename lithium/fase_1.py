import pygame
from pygame import display, sprite, image, transform, mixer, draw
from pygame import rect
from pygame.locals import*
from random import randrange
import construir
import interacao
import imagem

pygame.init()

'''
imagems 
-> O arquivo imagem fica resposável por ser um banco de todas as imagens dentro do jogo

construir
-> O arquivo contruir importa todas as classes contruturas necessárias naquela fase especifica do jogo

interacao
-> Esse arquivo guarda todas as nossas funcaoes que forem ser necessarias ao longo das fases do jogo

'''

#Display
LARGURA = 1280
ALTURA = 720
TELA = (1280, 720)
display.set_caption('Lithium')
JANELA = display.set_mode(TELA,0,32)
FPS = pygame.time.Clock()

#Constates
VELOCIDADE = 15
x_init_player = 604
y_init_player = 360
FLAG_CONTROL = True
FLAG_TEXTO = False



#Objetos
fundo = construir.Ambiente((LARGURA/2), (ALTURA/2), imagem.fundo_img)
portao = construir.Ambiente(312,218, imagem.portao_img)
pinheiro = construir.Ambiente(1024, 450, imagem.pinheiro_img)
arbusto = construir.Ambiente(1024, 200, imagem.arbusto_img)
player = construir.Player(x_init_player, y_init_player, 0, imagem.sprite_enya)
nicolau = construir.NPC(301, 314, 0, imagem.npc_img)
dialogo1 = construir.Textos(640, 600, imagem.dialogo_1_img, 4)


#teste com fundo


#Formando os Grupos
fundo_sprites = sprite.Group()
frente_sprites = sprite.Group()
textos = sprite.Group()
npcs_sprites = sprite.Group()
player_sprite = sprite.Group()


#Adicionando aos grupos
fundo_sprites.add(fundo)
frente_sprites.add(portao)
frente_sprites.add(pinheiro)
frente_sprites.add(arbusto)


player_sprite.add(player)
npcs_sprites.add(nicolau)


while True:
    FPS.tick(60)
    JANELA.fill((0, 0, 0))
    
    #Definido colisões
    colisao_npc = sprite.spritecollide(nicolau, player_sprite, False, pygame.sprite.collide_mask)
    

    #Objetos na tela divididos por grupos
    
    fundo_sprites.draw(JANELA)
    player_sprite.draw(JANELA)
    npcs_sprites.draw(JANELA)
    frente_sprites.draw(JANELA)
    

    if colisao_npc:

        FLAG_TEXTO = True
        n = interacao.n_enters()#Está retornando os valores quando clicado enter

        dialogo1.caixa(n)

        textos.add(dialogo1)
        textos.draw(JANELA)

    else:
        FLAG_TEXTO = False

    interacao.controlador(VELOCIDADE, FLAG_CONTROL, player, FLAG_TEXTO , max_caixas = 3)


    player_sprite.update()
    textos.update()
    fundo_sprites.update()
    npcs_sprites.update()

    display.flip()  
