import math
import random
import pygame


random.randint(0,255)

def random_cor():
    cor=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    return cor

#   Constante Gravitacional
g=21
epsilon=100

def distancia(m1,m2):
    dx = m2.posicao_x - m1.posicao_x
    dy = m2.posicao_y - m1.posicao_y

    r=math.sqrt(dx**2+dy**2)
    r = max(r, 0.01)

    return dx, dy, r

def gravitacao_Universal(m1, m2):
    dx, dy, r=distancia(m1,m2)

    forca_total=g*(m1.massa*m2.massa)/(r**2+epsilon)

    forca_x=forca_total*(dx/r)
    forca_y=forca_total*(dy/r)

    ax1=forca_x/m1.massa
    ay1=forca_y/m1.massa

    return ax1, ay1




def criar_botoes(screen, width, height, x, y, color, text):
    pos_mouse=pygame.mouse.get_pos()
    rect_botao = pygame.Rect(x, y, width, height)

    rect_botao_borda = pygame.Rect(x, y, width+2, height+2)
    pygame.draw.rect(screen, 'white', rect_botao_borda, width)

    pygame.draw.rect(screen, color, rect_botao, width+2)

    fonte=pygame.font.Font(None, 32)
    img_texto=fonte.render(text, True, (255, 255, 255))

    rect_texto = img_texto.get_rect(center=rect_botao.center)
    screen.blit(img_texto, rect_texto)

    return rect_botao


