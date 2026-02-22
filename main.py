import pygame
from estrutura_corpos import Corpo
from funcoes import *

    
pygame.init()
screen=pygame.display.set_mode((1200,800))

width=screen.get_width()
heigth=screen.get_height()

meio_x=width/2
meio_y=heigth/2


running=True

#m1=Corpo('Sol',posicao_x=meio_x,posicao_y=meio_y,velocidade_x=0,velocidade_y=0,massa=10000,raio=15,cor= 'yellow')


lista_corpos=[]
qtd_corpos=len(lista_corpos)

corpos_para_remover=[]

buracos_negros=[]

clock = pygame.time.Clock()


carregando=False
massa_temp=0.1
raio_temp=0.1
pos_click=(0,0)

pos_click_out=(0,0)

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            pos_click=event.pos
            x=pos_click[0]
            y=pos_click[1]
            carregando=True

        if event.type==pygame.MOUSEBUTTONUP:
            pos_click_out=event.pos
            x2=pos_click_out[0]
            y2=pos_click_out[1]

            vx=(x2-x)*0.01
            vy=(y2-y)*0.01

            carregando=False
            lista_corpos.append(Corpo('Corpo_Celeste', x, y, vx, vy, massa_temp, raio_temp, random_cor()))
            massa_temp=1
            raio_temp=1

    if carregando==True:
        massa_temp+=0.1
        raio_temp+=0.1

        pygame.draw.circle(screen,(100, 100, 100), (pos_click[0],pos_click[1]),raio_temp)


    for corpo in lista_corpos:
        if corpo.raio>150:
            buracos_negros.append(corpo)


    for corpo in buracos_negros:
            corpo.cor='black'
            corpo.raio=10
            corpo.massa=10000
            pygame.draw.circle(screen,(255, 255, 255), (corpo.posicao_x,corpo.posicao_y),corpo.raio+2)

            

    for corpo in lista_corpos:
        ax_tot=0
        ay_tot=0

        for outro in lista_corpos:
            if corpo!=outro:
                ax,ay=gravitacao_Universal(corpo, outro)
                ax_tot+=ax
                ay_tot+=ay

                dist_x, dist_y, r=distancia(corpo,outro)

                if r<(corpo.raio+outro.raio):
                    if(corpo.raio>=outro.raio):

                        #corpo.massa+=outro.massa
                        #corpo.raio+=outro.raio
                        corpo.massa+=0.2
                        corpo.raio+=0.2

                        outro.massa-=0.2
                        outro.raio-=0.2

                        if(outro.raio<=3):
                            corpos_para_remover.append(outro)

                    else:
                        #outro.massa+=corpo.massa
                        #outro.raio+=corpo.raio
                        outro.massa+=0.2
                        outro.raio+=0.2

                        corpo.massa-=0.2
                        corpo.raio-=0.2

                        if(corpo.raio<=3):
                            corpos_para_remover.append(corpo)
                    
        for c in corpos_para_remover:
            if c in lista_corpos:
                lista_corpos.remove(c)


        corpo.atualizar_vel(ax_tot, ay_tot)

    for i in lista_corpos:
        """ if i.raio<10 and i.raio>5:
            i.cor='blue'
        elif (i.raio>=10 and i.raio<=50):
            i.cor='orange'
        elif(i.raio>50 and i.raio<=75):
            i.cor='red'
        elif(i.raio>75 and i.raio<=100):
            i.cor=(193, 145, 0)
        elif(i.raio>100):
            i.cor='yellow' """
        
        i.criar_Corpo(screen)

    

    pygame.display.flip()

pygame.quit()