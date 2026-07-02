import pygame

class Eventos:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.mudar_x = 0
        self.velocidade = 3

    def controle(self):

        self.mudar_x = 0

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.mudar_x = -self.velocidade

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.mudar_x = self.velocidade
    
    def atualizar(self):
        self.x += self.mudar_x
        return self.x