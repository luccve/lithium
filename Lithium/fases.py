import pygame
import funcoes
import som
from random import randint
from pygame import display, sprite
from pygame.locals import*
import construir
import imagem
import mov_fases
pygame.init()


def fase_1():
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
            n = mov_fases.n_enters()#Está retornando os valores quando clicado enter

            dialogo1.caixa(n)

            textos.add(dialogo1)
            textos.draw(JANELA)

        else:
            FLAG_TEXTO = False

        mov_fases.movfase1(VELOCIDADE, FLAG_CONTROL, player, FLAG_TEXTO , max_caixas = 3)


        player_sprite.update()
        textos.update()
        fundo_sprites.update()
        npcs_sprites.update()

        display.flip()  

def fase_21():
    #som
    pygame.mixer.music.set_volume(0.25)
    som.fase21
    
    pygame.mixer.music.play(-1)
    #tela
    screen = (1280,720)
    JANELA = pygame.display.set_mode(screen,0,32)
    pygame.display.set_caption('Lithium')
    FPS = pygame.time.Clock()


    #Constantes
    x_init_player = 1100
    y_init_player = 360
    lista_skeleton = list()
    pontos = 0 #CONTADOR DE MONSTROS QUE MORRERAM
    speed = 60 #FPS
    mov = 3 #VELOCIDADE DO EIXO X DOS MONSTROS
    passou = 0 #CONTADOR DE MONSTROS QUE PASSARAM
    FLAG_TERMINOU_D2 = False

    #Grupos
    fundo_grup = sprite.Group()
    monstros = pygame.sprite.Group()
    sprite_player = pygame.sprite.Group()
    npcs = pygame.sprite.Group()
    trap_group = pygame.sprite.Group()#O grupo será usado pelo controlador para desenhar as setas
    textos = sprite.Group()
    

    #Criando aleatoríamente 6 esqueletos
    for i in range(6):
        skeleton = construir.Monster(0, 0)
        lista_skeleton.append(skeleton)
        monstros.add(skeleton)
        

    #Objetos
    player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
    nicolau = construir.NPC(1100, 300, 0, imagem.npc_img)
    d2 = construir.Textos(640, 360, imagem.dialogo_2_img, 2)
    background = construir.Ambiente(640, 360, imagem.background2)


    #Adicionando objetos ao grupo

    sprite_player.add(player)
    npcs.add(nicolau)
    textos.add(d2)
    fundo_grup.add(background)


    #Game
    while True:
        
        FPS.tick(speed)
        JANELA.fill((0, 0, 0))
        fundo_grup.draw(JANELA)

        mov_fases.movfase21(trap_group,VELOCIDADE=50 ,player = player, FLAG_TEXTO=True, max_caixas=1)

        n = mov_fases.n_enters()

        d2.caixa(n)

        
        textos.draw(JANELA)

        if n > 0:
            FLAG_TERMINOU_D2 = True
            textos.remove(d2)

        #O jogo começa depois do start inicial
        if FLAG_TERMINOU_D2:
            for skeleto in lista_skeleton:

                colisao_trap_monstro = pygame.sprite.spritecollide(skeleto, trap_group, True, pygame.sprite.collide_mask)

                if colisao_trap_monstro:
                    som.skeleton_die.set_volume(0.1)
                    som.skeleton_die.play()
                    pontos += 1
                    
                    #Realocando objetos da memoria
                    monstros.remove(skeleto)
                    lista_skeleton.remove(skeleto)

                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)
                
                if skeleto.rect.x == 1200:
                    
                    passou+=1

            #Desenhando objetos
            sprite_player.draw(JANELA)
            npcs.draw(JANELA)
            monstros.draw(JANELA)
        

            #Aumentando a dificuldade
            if pontos >= 20:
                mov = 6
            if pontos >= 50:
                mov = 10
 

            #Avisos
            funcoes.texto(f"PONTOS: {pontos}", 1000, 50)
            funcoes.texto(f'Já passaram {passou} de 11 Esqueletos. Para Game Over!.',150,20,fonte='arial',tamanho=22)

            #Condições de Game Over
            if passou > 10:
                pontos=0
                passou=0
                monstros.empty()
                lista_skeleton = []

                funcoes.gameover(JANELA,trap_group,player) 

                '''Função restart'''

                #Recontruindo os esquelestos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            colisao_player_monstro = pygame.sprite.spritecollide(player, monstros, True, pygame.sprite.collide_mask)

            if colisao_player_monstro:
                
                pontos = 0
                passou = 0
                monstros.empty()
                lista_skeleton = []

                funcoes.gameover(JANELA, trap_group, player)

                '''Função restart'''

                #Recontruindo os esquelestos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            #Condição de vitória 
            if pontos > 100:
                pontos = 0
                passou = 0
                trap_group.empty()
                monstros.empty()
                lista_skeleton= []

                funcoes.victory(player)

                #Recontruindo os esqueletos
                for c in range(6):
                    skeleton = construir.Monster(0, 0)
                    lista_skeleton.append(skeleton)
                    monstros.add(skeleton)


            #Atualizando objetos dando movimentação
            sprite_player.update()
            npcs.update()
            monstros.update(mov)

        #Atualizando
        pygame.display.flip() 

def fase_22():
    #som de fundo
    pygame.mixer.music.set_volume(0.25)
    som.fase22
    pygame.mixer.music.play(-1)


    #tela

    screen = (1280,720)
    JANELA = pygame.display.set_mode(screen,0,32)
    pygame.display.set_caption('Lithium')
    FPS = pygame.time.Clock()


    #Constantes
    x_init_player = 1100
    y_init_player = 360
    
    pontos = 0 #CONTADOR DE MONSTROS QUE MORRERAM
    speed = 120 #FPS
    mov = 3 #VELOCIDADE DO EIXO Y DOS MONSTROS
    
    FLAG_TERMINOU_D2 = False

    #Grupos
    sprite_player = sprite.Group()
    textos = sprite.Group()
    bossAranha =  sprite.Group()
    poisonAranha = sprite.Group()
    spear_grupo = sprite.Group()
    fundo_grup = sprite.Group()

        

    #Objetos
    player = construir.Player(x_init_player,y_init_player, 1, imagem.sprite_enya)
    aranha =  construir.Aranha(245, 0,mov)
    d2 = construir.Textos(640, 360, imagem.dialogo_2_img, 2)
    poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)
    background = construir.Ambiente(640, 360, imagem.background3)


    #Adicionando 

    sprite_player.add(player)
    bossAranha.add(aranha)
    poisonAranha.add(poison)
    textos.add(d2)
    fundo_grup.add(background)



    while True:
        
        #Desenhando
        FPS.tick(speed)
        JANELA.fill((0, 0, 0))
        fundo_grup.draw(JANELA)

        mov_fases.movfase22(spear_grupo,VELOCIDADE=50 ,player = player, FLAG_TEXTO=True, max_caixas=1)

        n = mov_fases.n_enters()

        d2.caixa(n)

        textos.draw(JANELA)

        if n > 0:
            FLAG_TERMINOU_D2 = True
            textos.remove(d2)


        if FLAG_TERMINOU_D2: 

            #Colisoes da aranha com o player
            colisao_aranha = pygame.sprite.spritecollide(player, bossAranha, False, pygame.sprite.collide_mask)
            colisao_poison = pygame.sprite.spritecollide(player, poisonAranha, False, pygame.sprite.collide_mask)

            #Colisões do ataque do player com a aranha
            colisao_fire1 = pygame.sprite.spritecollide(aranha, spear_grupo, True, pygame.sprite.collide_mask)

            #Reduzindo a vida da aranha
            if colisao_fire1:
                pontos += 10
                som.fire_hit.set_volume(0.15)
                som.fire_hit.play()    
            #Condições de Restart
            if colisao_aranha:
                funcoes.gameover(JANELA,poisonAranha,player)
                pontos = 0
                spear_grupo.empty()
            if colisao_poison:
                funcoes.gameover(JANELA,poisonAranha, player)
                pontos = 0
                spear_grupo.empty()

            #Inteligência de ataque da Aranha
            if pontos < 100:
                if aranha.rect.centery == player.rect.centery or aranha.rect.centery == player.rect.centery+randint(1,100) or aranha.rect.centery == player.rect.centery - randint(1, 100):
                    poison = construir.Projetil(aranha, imagem.aranhaPoison, 18, 20, 4, 3)
                    poisonAranha.add(poison)
                    som.hit_spider.set_volume(0.1)
                    som.hit_spider.play()
                    
            #Remover objetos para otimizar a memória
            if poison.rect.x > 1280:
                poisonAranha.remove(poison)
            

            sprite_player.draw(JANELA)
            bossAranha.draw(JANELA)
            spear_grupo.draw(JANELA)
            poisonAranha.draw(JANELA)

            if pontos <= 25 and pontos >0:
                JANELA.blit(imagem.vida4,(500,50))
                #funcoes.texto(f"{int(abs((pontos/100*100)-100))}%", 750, 50,tamanho=30)
            if pontos <= 50 and pontos > 25:
                JANELA.blit(imagem.vida3,(500,50))
                
            if pontos <= 75 and pontos > 50:
                JANELA.blit(imagem.vida2,(500,50))
                
            if pontos <= 99 and pontos > 75:
                JANELA.blit(imagem.vida1,(500,50))

            #tela de vitória
            if pontos > 100:
                poisonAranha.empty()
                spear_grupo.empty()
                funcoes.victory(player)
                pontos = 0
                
            
            sprite_player.update()
            bossAranha.update()
            poisonAranha.update()
            spear_grupo.update()

        pygame.display.flip() 


