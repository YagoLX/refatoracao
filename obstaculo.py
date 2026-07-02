import pygame
import random
import time
from arquivos import CarregarArquivos


class Obstaculos:
    xo = None
    yo = None
    image = None
    hazard_fig = None

    chaves = ["nave",
             "satelite",
             "cometa",
             "planeta",
             "ameaca"]
 
    def __init__(self):
        self.CarregarArquivos = CarregarArquivos() #Para acessar o dicionário centralizado (composição)

    def criar(self):
        if self.yo > 600:
            self.yo = 0 - 130
            self.xo = random.randrange(125, 650 - 130)
            tipo_obstaculo = random.randint(0, 4)


            # determinando quantos hazard passaram e a pontuação
            o_passados += 1
            pontuacao = o_passados * 10

    def renderizar(self, tipo):
        self.hazard_fig = self.CarregarArquivos.imagem(self.chaves[tipo])
        self.hazard_fig.convert()
        self.hazard_fig = pygame.transform.scale(self.hazard_fig, (130, 130))

    # Desenhar Hazard
    def draw (self, tela, x, y):
        tela.blit(self.hazard_fig, (x, y))

# Hazard:
