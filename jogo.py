import pygame
import random
from fundo import Fundo
from eventos import Eventos
from colisao import Colisao
from interface import Interface
from elementos import *

class Jogo:
    tela = None
    tam_tela = None
    run = True
    background = None
    jogador = None
    hazard_1 = hazard_2 = hazard_3 = hazard_4 = hazard_5 = None
    eventos = Eventos(372,475)
    interface = None
    obstaculos = Obstaculos()

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

        self.interface = Interface()
 
    def loop(self):
        pontuacao = 0
        o_passados = 0

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_obstaculo = 7

        tipo_obstaculo = 0
        self.obstaculos.renderizar(tipo_obstaculo)
        xo = random.randrange(125, 660)
        yo = -500

        # Info Hazard
        largura_o = 130 #55
        altura_o = 130 #120

        # Criar o Plano de fundo
        self.background = Fundo()

        # Posicao do Player
        x = 372
        y = 475

        # Criar o Player
        self.jogador = Jogador(x, y)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 0

        # assim iniciamos o loop principal do programa
        while self.run:

            dt = clock.tick(90)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            #controle do jogador
            self.eventos.controle()
            x = self.eventos.atualizar()

            #atualizacao do fundo
            self.background.update(dt)
            self.background.draw(self.tela)

            # Mostrar Player
            self.jogador.draw(self.tela, self.eventos.x, y)

            # Mostrar score
            self.interface.pontuacao(self.tela, o_passados, pontuacao)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > 760 - 92 or x < 40 + 5:
                self.interface.msg_colisao("lateral", self.tela)
                self.loop()
                self.run = False

            # loop que redesenha continuamente a posicao
            yo = yo + velocidade_obstaculo
            self.obstaculos.draw(self.tela,xo,yo)

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if yo > 600:
                yo = 0 - altura_o
                xo = random.randrange(125, 650 - altura_o)
                tipo_obstaculo = random.randint(0, 4)
                # determinando quantos hazard passaram e a pontuação
                o_passados += 1
                pontuacao = o_passados * 10
                self.obstaculos.renderizar(tipo_obstaculo)

            # restrições para o game over
            if y < yo + altura_o:
                if x > xo or x > xo - 56:
                    if x < xo + largura_o or x < xo - 56:
                        self.interface.msg_colisao("perdeu", self.tela) ##convém colocar na classe colisao
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()
# Game:   