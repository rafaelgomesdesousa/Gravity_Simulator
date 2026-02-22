import math

#   Constante Gravitacional
g=9
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
