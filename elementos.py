import pygame
import random

class Elemento:
    imagem = None

    def draw(self, tela, x, y):
        tela.blit(self.imagem, (x, y))

class Jogador(Elemento):

    def __init__(self, x = None, y= None):
        self.imagem = None
        player_fig = pygame.image.load("Images/player.png")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.imagem = player_fig
        self.x = x
        self.y = y
    # __init__()

class Obstaculos(Elemento):
    xo = None
    yo = None
    imagem = None

    imagens = ["Images/nave.png",
               "Images/satelite.png",
               "Images/cometa.png",
               "Images/planeta.png",
               "Images/ameaca.png"]
 
    def criar(self):
        if self.yo > 600:
            self.yo = 0 - 130
            self.xo = random.randrange(125, 650 - 130)
            tipo_obstaculo = random.randint(0, 4)

            # determinando quantos hazard passaram e a pontuação
            o_passados += 1
            pontuacao = o_passados * 10

    def renderizar(self, tipo):
        self.imagem = pygame.image.load(self.imagens[tipo])
        self.imagem.convert()
        self.imagem = pygame.transform.scale(self.imagem, (130, 130))

    