import pygame
import random
import time
from arquivos import CarregarArquivos

class Jogador:
    """
    Classe Jogador
    """


    def __init__(self, x = None, y= None):
        self.image = None
        self.CarregarArquivos = CarregarArquivos() #Para acessar o dicionário centralizado (composição)
        player_fig = self.CarregarArquivos.imagem("player")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (90, 90))
        self.image = player_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Player
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Player: