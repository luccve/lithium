import pygame
from pygame.locals import *
from sys import exit
 

LARGURA = 1280
ALTURA = 720
FPS = 30

selecao = 1

MENU1 = ' Novo Jogo '
MENU2 = ' Creditos  '
MENU3 = ' Instruções'
MENU4 = '   Sair    '

FONTE_MENU = 'kristen itc'
TAMANHO_FONTE = 40
COR_FONTE_SELECIONADA = (255, 0, 0)
COR_FONTE = (255, 255, 255)

MEIOTELA_X = LARGURA/2
MEIOTELA_Y = ALTURA/2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((LARGURA, ALTURA), 0, 32)
botao_enter = False


def tela():
    return screen.fill((0, 0, 0))


def f_creditos():

    font1 = pygame.font.SysFont(FONTE_MENU, 40, True, False)
    msg1 = "Desenvolvido por Estevão Silva e Vinicius Lima"
    txt1 = font1.render(msg1, True, (255, 0, 0))

    font2 = pygame.font.SysFont(FONTE_MENU, 26, True, False)

    msg2 = "Baseado no livro Lithium não publicado da autora Melissa Lacerda @mel_vespertina"
    txt2 = font2.render(msg2, True, (255, 255, 255))

    msg3 = "Música original feito por Rafael Luiz @rafaleohh"
    txt3 = font2.render(msg3, True, (255, 255, 255))

    msg4 = "Pressione Enter pra voltar pro menu"
    txt4 = font2.render(msg4, True, (0, 0, 255))

    creditos_menu = True
    while creditos_menu:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    creditos_menu = False
        screen.blit(txt1, (80, 200))
        screen.blit(txt2, (20, 400))
        screen.blit(txt3, (240, 600))
        screen.blit(txt4, (650, 50))
        pygame.display.update()


def events():
    global selecao
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_s or event.key == K_DOWN:
                selecao += 1
            if event.key == K_w or event.key == K_UP:
                selecao -= 1
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_SPACE or event.key == K_RETURN:
                if selecao == 1:
                    import lithium
                if selecao == 2:
                    f_creditos()

                if selecao == 4:
                    pygame.quit()
                    exit()


def menu():
    global selecao
    if selecao == 1:

        tela()

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        novo_jogo = fonte.render(MENU1, True, COR_FONTE_SELECIONADA)
        screen.blit(novo_jogo, (MEIOTELA_X-50, MEIOTELA_Y-50))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        creditos = fonte.render(MENU2, True, COR_FONTE)
        screen.blit(creditos, (MEIOTELA_X-70, MEIOTELA_Y+20))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        instrucoes = fonte.render(MENU3, True, COR_FONTE)
        screen.blit(instrucoes, (MEIOTELA_X-70, MEIOTELA_Y+90))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        sair = fonte.render(MENU4, True, COR_FONTE)
        screen.blit(sair, (MEIOTELA_X-70, MEIOTELA_Y+160))

    if selecao == 2:

        tela()

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        novo_jogo = fonte.render(MENU1, True, COR_FONTE)
        screen.blit(novo_jogo, (MEIOTELA_X-70, MEIOTELA_Y-50))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        creditos = fonte.render(MENU2, True, COR_FONTE_SELECIONADA)
        screen.blit(creditos, (MEIOTELA_X-50, MEIOTELA_Y+20))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        instrucoes = fonte.render(MENU3, True, COR_FONTE)
        screen.blit(instrucoes, (MEIOTELA_X-70, MEIOTELA_Y+90))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        sair = fonte.render(MENU4, True, COR_FONTE)
        screen.blit(sair, (MEIOTELA_X-70, MEIOTELA_Y+160))

    if selecao == 3:

        tela()

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        novo_jogo = fonte.render(MENU1, True, COR_FONTE)
        screen.blit(novo_jogo, (MEIOTELA_X-70, MEIOTELA_Y-50))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        creditos = fonte.render(MENU2, True, COR_FONTE)
        screen.blit(creditos, (MEIOTELA_X-70, MEIOTELA_Y+20))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        instrucoes = fonte.render(MENU3, True, COR_FONTE_SELECIONADA)
        screen.blit(instrucoes, (MEIOTELA_X-50, MEIOTELA_Y+90))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        sair = fonte.render(MENU4, True, COR_FONTE)
        screen.blit(sair, (MEIOTELA_X-70, MEIOTELA_Y+160))

    if selecao == 4:

        tela()

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        novo_jogo = fonte.render(MENU1, True, COR_FONTE)
        screen.blit(novo_jogo, (MEIOTELA_X-70, MEIOTELA_Y-50))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        creditos = fonte.render(MENU2, True, COR_FONTE)
        screen.blit(creditos, (MEIOTELA_X-70, MEIOTELA_Y+20))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        instrucoes = fonte.render(MENU3, True, COR_FONTE)
        screen.blit(instrucoes, (MEIOTELA_X-70, MEIOTELA_Y+90))

        fonte = pygame.font.SysFont(FONTE_MENU, TAMANHO_FONTE, True, False)
        sair = fonte.render(MENU4, True, COR_FONTE_SELECIONADA)
        screen.blit(sair, (MEIOTELA_X-50, MEIOTELA_Y+160))

    if selecao < 1:
        selecao = 5

    if selecao > 5:
        selecao = 1


while True:

    events()
    menu()

    pygame.display.update()
