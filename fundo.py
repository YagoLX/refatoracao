import pygame
import random
import time

class Fundo:
    """
    Esta classe define o Plano de Fundo do jogo
    """

    def __init__(self):
        self.image = None
        self.margin_left = None
        self.margin_right = None
        self.image = self._carregar_imagem("Images/background.png")
        self.margin_left= self._carregar_imagem("Images/margin_1.png", (60, 600))

        self. margin_right = self._carregar_imagem("Images/margin_2.png", (60,600))
    # __init__()
    
    def update(self, dt):
        pass
    # update()
    def _carregar_imagem(self, caminho, tamanho = None):
        imagem = pygame.image.load(caminho)
        imagem = imagem.convert()

        if tamanho:
            imagem = pygame.transform.scale(imagem,tamanho)
        
        return imagem


    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (740, 0))
    # draw()
    def _desenhar_repetido(self, tela, imagem, x, y):
    # Desenha a imagem atual e as que ficam abaixo
        for deslocamento in range(0, 3001, 600):
            tela.blit(imagem, (x, y + deslocamento))

    # Desenha as que ficam acima
        for deslocamento in range(-600, -4801, -600):
            tela.blit(imagem, (x, y + deslocamento))
        
    # Define posições do Plano de Fundo para criar o movimento

    ##Da pra gente converter tudo em uma função só e simplicar tudo com um loop.
    def mover (self, screen, movL_x, movL_y, movR_x, movR_y):

        #movimento background
        self._desenhar_repetido(screen, self.image, movL_x, movL_y)

        # movimento margem esquerda
        self._desenhar_repetido(screen, self.margin_left, movL_x, movL_y)

        # movimento margem direita
        self._desenhar_repetido(screen, self.margin_right, movR_x, movR_y)
    # move()
# Background:
