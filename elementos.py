import pygame
import random
from arquivos import CarregarArquivos

class Elemento:
    imagem = None

    def draw(self, tela, x, y):
        tela.blit(self.imagem, (x, y))

class Jogador(Elemento):

    def __init__(self, x = None, y= None):
        self.imagem = None
        self.CarregarArquivos = CarregarArquivos() #Para acessar o dicionário centralizado (composição)
        player_fig = self.CarregarArquivos.imagem("player")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.imagem = player_fig
        self.x = x
        self.y = y
    # __init__()

class Obstaculos(Elemento):
    
    def __init__(self):
        self.CarregarArquivos = CarregarArquivos() #Para acessar o dicionário centralizado (composição)
        self.chaves = ["nave",
                        "satelite",
                        "cometa",
                        "planeta",
                        "ameaca"]
        self.xo = None
        self.yo = None
        self.imagem = None

    def criar(self):
        if self.yo > 600:
            self.yo = 0 - 130
            self.xo = random.randrange(125, 650 - 130)
            tipo_obstaculo = random.randint(0, 4)

            # determinando quantos hazard passaram e a pontuação
            o_passados += 1
            pontuacao = o_passados * 10

    def renderizar(self, chave):
        self.imagem = self.CarregarArquivos.imagem(self.chaves[chave])
        self.imagem.convert()
        self.imagem = pygame.transform.scale(self.imagem, (130, 130))

    