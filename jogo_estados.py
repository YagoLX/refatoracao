import pygame
import random
from fundo import Fundo
from eventos import Eventos
from colisao import Colisao
from interface import Interface
from elementos import *
from estados import Jogando

class Jogo:

    def __init__(self):

        """
        Função que inicializa o pygame, define a resolução da tela,
        caption, e desabilita o mouse.
        """
        pygame.init()

        self.tela = pygame.display.set_mode((800, 600))  # tamanho da tela
        self.tam_tela = self.tela.get_size()

        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Viagem Espacial')

        self.run = True
        self.interface = Interface()

        #Pontuação
        self.pontuacao = 0
        self.o_passados = 0
        self.velocidade_obstaculo = 7

        #Tamanho dos obstaculos
        self.largura_o = 130
        self.altura_o = 130

        #Posição dos obstaculos
        self.xo = random.randrange(125, 660)
        self.yo = -500
        self.tipo_obstaculo = 0

        #Background e comandos
        self.background = Fundo()
        self.eventos = Eventos(372, 475)

        # posição fixa vertical do jogador
        self.x = 372
        self.y = 475
        self.jogador = Jogador(self.x, self.y)

        #Obstaculos
        self.obstaculos = Obstaculos()
        self.obstaculos.renderizar(self.tipo_obstaculo)

        self.clock = pygame.time.Clock()

        # estado inicial da máquina de estados
        self.estado = Jogando(self)
 

    def trocar_estado(self, novo_estado):
        self.estado = novo_estado

    def loop(self):  

        # assim iniciamos o loop principal do programa
        while self.run:
            dt = self.clock.tick(90)/1000.0

            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.run = False
            
            print (self.estado)
            # delega tudo ao estado atual
            self.estado.processar_eventos(eventos)
            self.estado.atualizar(dt)
            self.estado.desenhar(self.tela)

            # atualizando a tela
            pygame.display.update()
            self.clock.tick(2000)

        pygame.quit()
        # while self.run
    # loop()
# Game:   