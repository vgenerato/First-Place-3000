#Criadores:
#Victor Gonzaga Generato - 31843409
#Krizhan Wesley - 31896839



import pygame, os, sys, math, time

#variaveis set
pygame.init()
screen = pygame.display.set_mode((852,480))
pygame.display.set_caption("First Place 3000")
screen.fill((0, 0, 0))

#variaveis de imagens
bg_menu = pygame.image.load('bg_menu.jpg')
cred = pygame.image.load('bg_creditos.jpg')
instr = pygame.image.load('bg_instrucoes.jpg')
rank = pygame.image.load('bg_ranking.jpg')
veiculos = pygame.image.load('bg_veiculos.jpg')
carro_1 = pygame.image.load("carro_1.png")
carro_2 = pygame.image.load("carro_2.png")
carro_3 = pygame.image.load("carro_3.png")
moto_1 = pygame.image.load("moto_1.png")
moto_2 = pygame.image.load("moto_2.png")
bicicleta = pygame.image.load("bicicleta.png")
caminhao = pygame.image.load("caminhao.png")
explosion = pygame.image.load("explosion.png")


#variaveis de cores
azul = (0,0,255)
vermelho = (255,0,0)
branco = (255,255,255)
rua = (100, 100, 100, 255)
cerca  = (255, 5, 5, 255)
chegada = (255, 255, 5, 255)

#outras variaves
x=0
y=0
w = 1057
z = 657
cont_pista = 1
cont = 0
a = 1
rank_1 = 0
rank_2 = 0
pista = []
player_1 = ''
player_2 = ''
pos_1 = [0,0,0,0]
pos_2 = [0,0,0,0]
font = pygame.font.SysFont('Comic Sans MS', 30)

def menu():
    pygame.mixer.music.load("music_menu.mp3")
    pygame.mixer.music.play()
    intro = True
    while intro:
        for event in pygame.event.get():
            #print (event)
            screen.blit(bg_menu, (x,y))
            pygame.display.flip()
            #créditos
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 837> event.pos[0] > 753 and 462 > event.pos[1] > 429:
                    creditos()
            #instruções
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 486> event.pos[0] > 353 and 434 > event.pos[1] > 390:
                    instrucoes()
            #Ranking
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 495> event.pos[0] > 343 and 362 > event.pos[1] > 324:
                    ranking()

            #Iniciar
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 468> event.pos[0] > 376 and 297 > event.pos[1] > 225:
                    iniciar()

            #Sair
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 40> event.pos[1] > 5 and 848 > event.pos[0] > 790:
                    pygame.quit()
                    sys.exit()
        


def creditos():
    intro = True
    while intro:
        screen.blit(cred,(x,y))
        pygame.display.flip()
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 97 > event.pos[0] > 5 and 54 > event.pos[1] > 8:
                    menu()

def instrucoes():
    intro = True
    while intro:
        screen.blit(instr,(x,y))
        pygame.display.flip()
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 97 > event.pos[0] > 5 and 54 > event.pos[1] > 8:
                    menu()
def ranking():
    global rank_1
    global rank_2
    rank_1_text = font.render('SETAS: ' + str(rank_1), False, azul)
    rank_2_text = font.render('WASD: ' + str(rank_2), False, azul)
    intro = True
    while intro:
        screen.blit(rank,(x,y))
        screen.blit(rank_1_text,(290,223))
        screen.blit(rank_2_text,(290,290))
        pygame.display.flip()
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 97 > event.pos[0] > 5 and 54 > event.pos[1] > 8:
                    menu()
                if 483 > event.pos[0] > 332 and 444 > event.pos[1] > 411:
                    rank_1 = 0
                    rank_2 = 0
                    rank_1_text = font.render('SETAS: ' + str(rank_1), False, azul)
                    rank_2_text = font.render('WASD: ' + str(rank_2), False, azul)
                    screen.blit(rank,(x,y))
                    screen.blit(rank_1_text,(290,223))
                    screen.blit(rank_2_text,(290,290))
                    pygame.display.flip()


def jogar():
    global a
    global cont_pista
    global cont
    global pista
    global rank_1
    global rank_2
    global music
    
    janela = pygame.display.set_mode((w, z))
    janela.fill(branco)
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music_jogo.mp3")
    pygame.mixer.music.play()
    

    #Coloca imagens das pistas em uma lista
    while a == 1:
        try:
            exec("pista.append(pygame.image.load('pista_"+ str(cont_pista) + ".png'))")
        except:
            a = 0
        cont_pista += 1
    
    #cria retangulos representandos os carros
    pl_1 = pygame.Rect(76, 113, 41, 28)
    pl_2 = pygame.Rect(76, 153, 41, 28)

    ####Player 1
    
    pres_1 = "false"
    pres_1_l = "false"
    pres_1_r = "false"
    pres_1_b = "false"
    
    aceleracao_1 = 0
    angulo_1 = 0
    dest_1 = 0
    count_dest_1 = 0
    
    ####Player 2
    pres_2 = "false"
    pres_2_l = "false"
    pres_2_r = "false"
    pres_2_b = "false"
    
    aceleracao_2 = 0
    angulo_2 = 0
    dest_2 = 0
    count_dest_2 = 0
    
    max_ac = 8
    angulo_troca = 4
    
    clock = pygame.time.Clock()
    fps = 144
    time_ = 0

     
    x = 1
    while x == 1:
        #Posiciona carro1
        if count_dest_1 == 1:
            pl_1.left = 76
            pl_1.top = 113
        #Posiciona carro2
        if count_dest_2 == 1:
            pl_2.left = 76
            pl_2.top = 153

        # Player 1
        if count_dest_1 == 0:
            #Calcula velocidade e angulo do carro1
            if pres_1 == "true" and aceleracao_1 < max_ac:
                aceleracao_1 += 0.25
            if pres_1_b == "true":
                aceleracao_1 -= 0.25
            
            if pres_1_l == "true" and aceleracao_1 > 2:
                angulo_1 -= angulo_troca
            elif pres_1_l == "true" and aceleracao_1 < -2:
                angulo_1 += angulo_troca
                
            if pres_1_r == "true" and aceleracao_1 > 2:
                angulo_1 += angulo_troca
            elif pres_1_r == "true" and aceleracao_1 < -2:
                angulo_1 -= angulo_troca


            if pres_1 == "false" and aceleracao_1 > 0:
                aceleracao_1 -= 0.25
            if pres_1_b == "false" and aceleracao_1 < 0:
                aceleracao_1 += 0.25

            #Calcula o espaço seguinte
            b_1 = math.cos(math.radians(angulo_1)) * aceleracao_1 
            a_1 = math.sin(math.radians(angulo_1)) * aceleracao_1
            pl_1.left += round(b_1)
            pl_1.top += round(a_1)

            image_1_novo = pygame.transform.rotate((player_1), angulo_1*-1)

        else:
            count_dest_1 -= 1

    # Player 2
        if count_dest_2 == 0:
            if pres_2 == "true" and aceleracao_2 < max_ac:
                    aceleracao_2 += 0.25
            if pres_2_b == "true":
                    aceleracao_2 -= 0.25

            if pres_2_l == "true" and aceleracao_2 > 2:
                    angulo_2 -= angulo_troca
            elif pres_2_l == "true" and aceleracao_2 < -2:
                    angulo_2 += angulo_troca
            
            if pres_2_r == "true" and aceleracao_2 > 2:
                    angulo_2 += angulo_troca
            elif pres_2_r == "true" and aceleracao_2 < -2:
                    angulo_2 -= angulo_troca


            if pres_2 == "false" and aceleracao_2 > 0:
                    aceleracao_2 -= 0.25
            if pres_2_b == "false" and aceleracao_2 < 0:
                    aceleracao_2 += 0.25    

            b_2 = math.cos(math.radians(angulo_2)) * aceleracao_2
            a_2 = math.sin(math.radians(angulo_2)) * aceleracao_2
            pl_2.left += round(b_2)
            pl_2.top += round(a_2)

            image_2_novo = pygame.transform.rotate((player_2), angulo_2*-1)

        else:
            count_dest_2 -=1

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                #Volta do menu
                if 97 > event.pos[0] > 5 and 54 > event.pos[1] > 8:
                    pygame.display.set_mode((852,480))
                    menu()
            #Fecha o jogo caso clique em fechar janela
            if event.type == pygame.QUIT:
                pygame.quit()
                x = 0
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #Muda de pista ao apertar o Enter
                if event.key == pygame.K_RETURN:
                    cont += 1
                    pl_1.left = 76
                    pl_1.top = 113
                    angulo_1 = 0

                    pl_2.left = 76
                    pl_2.top = 153
                    angulo_2 = 0
                    
                    if cont >= len(pista):
                        cont = 0                    


                #Seta como True caso aperte as teclas em questão             
                if event.key == pygame.K_UP:
                    pres_1 = "true"
                if event.key == pygame.K_LEFT:
                    pres_1_l = "true"
                if event.key == pygame.K_RIGHT:
                    pres_1_r = "true"
                if event.key == pygame.K_DOWN:
                    pres_1_b = "true"

                if event.key == pygame.K_w:
                    pres_2 = "true"
                if event.key == pygame.K_a:
                    pres_2_l = "true"
                if event.key == pygame.K_d:
                    pres_2_r = "true"
                if event.key == pygame.K_s:
                    pres_2_b = "true"

            #seta como false caso solte as teclas em questão
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pres_1 = "false"
                if event.key == pygame.K_LEFT:
                    pres_1_l = "false"
                if event.key == pygame.K_RIGHT:
                    pres_1_r = "false"
                if event.key == pygame.K_DOWN:
                    pres_1_b = "false"

                if event.key == pygame.K_w:
                    pres_2 = "false"
                if event.key == pygame.K_a:
                    pres_2_l = "false"
                if event.key == pygame.K_d:
                    pres_2_r = "false"
                if event.key == pygame.K_s:
                    pres_2_b = "false"

                    
        #carrega a imagem da pista na tela
        janela.fill((0, 0, 0))
        janela.blit(pista[cont], (0, 0))

        if count_dest_1 == 0:
            try:
                #seta velocidade caso esteja na rua
                if not janela.get_at((pl_1.left + 10, pl_1.top + 10)) == rua:
                    if aceleracao_1 > 3:
                        aceleracao_1 = 2
                    if aceleracao_1 < -3:
                        aceleracao_1 = -2
                #seta explosao caso o carro bata na cerca
                if janela.get_at((pl_1.left + 10, pl_1.top + 10)) == cerca:
                    dest_1 = 1
                #seta explosao caso o carro bata na linha de chegada
                if janela.get_at((pl_1.left + 10, pl_1.top + 10)) == chegada:
                    dest_1 = 1
                    rank_1 += 1
                    cont += 1
                    if cont >= len(pista):
                        cont = 0

                    
            except:
                dest_1 = 1
                
            if dest_1 == 0:
                janela.blit(image_1_novo, pl_1)
                
        #o carro explode caso saia do limite da tela
        else:
            janela.blit(explosion, pl_1)


        # Player 2 Detecta colisão
        if count_dest_2 == 0:
            try:
                if not janela.get_at((pl_2.left + 10, pl_2.top + 10)) == rua:
                    if aceleracao_2 > 3:
                        aceleracao_2 = 2
                    if aceleracao_2 < -3:
                        aceleracao_2 = -2

                if janela.get_at((pl_2.left + 10, pl_2.top + 10)) == cerca:
                    dest_2 = 1

                if janela.get_at((pl_2.left + 10, pl_2.top + 10)) == chegada:
                    dest_2 = 1
                    rank_2 += 1
                    cont += 1
                    if cont >= len(pista):
                        cont = 0

            except:
                dest_2 = 1
        
            if dest_2 == 0:
                janela.blit(image_2_novo, pl_2)

        else:
            janela.blit(explosion, pl_2)

        #Carrega o carro novamente
        if dest_1 == 1:
            janela.blit(explosion, pl_1)
            pygame.display.update()
            dest_1 = 0
            angulo_1 = 0
            count_dest_1 = 25
            pl_1.left = 76
            pl_1.top = 113
            pl_2.left = 76
            pl_2.top = 153
            angulo_2 = 0
                

        if dest_2 == 1:
            janela.blit(explosion, pl_2)
            pygame.display.update()
            dest_2 = 0
            angulo_2 = 0
            count_dest_2 = 25
            pl_1.left = 76
            pl_1.top = 113
            pl_2.left = 76
            pl_2.top = 153
            angulo_1 = 0
           
        pygame.display.update()

        clock.tick(fps)
    

def iniciar():
    global pos_1
    global pos_2
    global player_1
    global player_2
    intro = True
    while intro:
        screen.blit(veiculos,(x,y))
        pygame.draw.rect(screen,azul,pos_1,4)
        pygame.draw.rect(screen,vermelho,pos_2,4)
        for event in pygame.event.get():
            #print (event)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if 97 > event.pos[0] > 5 and 54 > event.pos[1] > 8:
                    menu()
                #Player 1 carro 1
                if 178 > event.pos[0] > 100 and 248 > event.pos[1] > 202:
                    pos_1 = [100,202,78,46]
                    player_1 = carro_1
                #Player 1 caminhao
                if 285 > event.pos[0] > 205 and 245 > event.pos[1] > 200 :
                    pos_1 = [205,200,80,45]
                    player_1 = caminhao
                #Player 1 carro 2
                if 392 > event.pos[0] > 316 and 240 > event.pos[1] > 207 :
                    pos_1 = [316,207,76,40]
                    player_1 = carro_2
                #Player 1 carro 3
                if 177 > event.pos[0] > 104 and 337 > event.pos[1] > 301 :
                    pos_1 = [104,301,73,36]
                    player_1 = carro_3
                #Player 1 moto
                if 284 > event.pos[0] > 209 and 343 > event.pos[1] > 302 :
                    pos_1 = [209,302,75,41]
                    player_1 = moto_1
                #Player 1 bike
                if 389 > event.pos[0] > 318 and 340 > event.pos[1] > 292 :
                    pos_1 = [318,292,71,48]
                    player_1 = bicicleta
                #Player 1 scooter
                if 286 > event.pos[0] > 213 and 426 > event.pos[1] > 377 :
                    pos_1 = [213,377,73,50]
                    player_1 = moto_2
                #Player 2 carro 1
                if 534 > event.pos[0] > 457 and 240 > event.pos[1] > 207 :
                    pos_2 = [455,205,80,38]
                    player_2 = carro_1
                #Player 2 caminhao
                if 641 > event.pos[0] > 564 and 245 > event.pos[1] > 203 :
                    pos_2 = [564,203,80,46]
                    player_2 = caminhao
                #Player 2 carro 2
                if 749 > event.pos[0] > 677 and 241 > event.pos[1] > 208 :
                    pos_2 = [673,204,76,40]
                    player_2 = carro_2
                #Player 2 carro 3
                if 533 > event.pos[0] > 460 and 336 > event.pos[1] > 303 :
                    pos_2 = [460,303,73,36]
                    player_2 = carro_3
                #Player 2 moto
                if 643 > event.pos[0] > 567 and 343 > event.pos[1] > 300 :
                    pos_2 = [567,300,75,41]
                    player_2 = moto_1
                #Player 2 bike
                if 747 > event.pos[0] > 674 and 341 > event.pos[1] > 296 :
                    pos_2 = [674,296,71,48]
                    player_2 = bicicleta
                #Player 2 scooter
                if 641 > event.pos[0] > 565 and 425 > event.pos[1] > 376 :
                    pos_2 = [565,376,73,50]
                    player_2 = moto_2
                pygame.display.flip()
                if 847 > event.pos[0] > 753 and 474 > event.pos[1] > 433 :
                    if player_2 != '' and player_1 != '':
                        jogar()
                    else:
                        print('ERRO!! escolha um carro.')
    


menu()

exit()

