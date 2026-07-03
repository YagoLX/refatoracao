import pygame

class Fundo:
    """
    Esta classe define o Plano de Fundo do jogo
    """

    def __init__(self):
        self.image = None
        self.margin_left = None
        self.margin_right = None
        self.velocidade = 200
        self.y = 0
        self.image = self._carregar_imagem("Images/background.png", (800,600))
        self.margin_left= self._carregar_imagem("Images/margin_1.png", (60, 600))

        self. margin_right = self._carregar_imagem("Images/margin_2.png", (60,600))


    def _carregar_imagem(self, caminho, tamanho = None):
        imagem = pygame.image.load(caminho)
        imagem = imagem.convert()

        if tamanho:
            imagem = pygame.transform.scale(imagem,tamanho)
        
        return imagem


    def update(self, dt):
        self.y += self.velocidade*dt

        if self.y >= 600:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.margin_left, (0, self.y))
        screen.blit(self.margin_right, (740, self.y))

        screen.blit(self.image, (0, self.y -600))
        screen.blit(self.margin_left, (0, self.y -600))
        screen.blit(self.margin_right, (740, self.y -600))

