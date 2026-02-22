import pygame

class Corpo:
    def __init__(self, nome, posicao_x, posicao_y,velocidade_x,velocidade_y ,massa, raio, cor):
        self.nome=nome
        self.posicao_x=posicao_x
        self.posicao_y=posicao_y
        self.massa=massa
        self.velocidade_x=velocidade_x
        self.velocidade_y=velocidade_y
        self.raio=raio
        self.cor=cor

    def atualizar_vel(self, aceleracao_x, aceleracao_y):
        self.velocidade_x+=aceleracao_x
        self.velocidade_y+=aceleracao_y

        self.posicao_x+=self.velocidade_x
        self.posicao_y+=self.velocidade_y

    def criar_Corpo(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.posicao_x), int(self.posicao_y)), self.raio)
