import pygame
import random
import time
from jogador import Jogador
from obstaculo import Obstaculos
from fundo import Fundo
from eventos import Eventos
from colisao import Colisao
from interface import Interface

class Jogo:
    tela = None
    tam_tela = None
    run = True
    background = None
    player = None
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

    def elements_update(self, dt):
        self.background.update(dt)

    def elements_draw(self):
        self.background.draw(self.tela)

    # Desenha o Player
    def draw_player (self, x, y):
        self.player.draw (self.tela, x, y)
 
    # Desenha Hazard
    # def draw_hazard (self, hzrd, x, y):
    #     match hzrd:
    #         case 0:
    #             self.hazard_1.draw(self.tela, x, y)
    #         case 1:
    #             self.hazard_2.draw(self.tela, x, y)
    #         case 2:
    #             self.hazard_3.draw(self.tela, x, y)
    #         case 3:
    #             self.hazard_4.draw(self.tela, x, y)
    #         case 4:
    #             self.hazard_5.draw(self.tela, x, y)

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.mover (self.tela, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)

    # Informa a quantidade de hazard que passaram e a Pontuação

    def loop(self):
        pontuacao = 0
        o_passados = 0

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_background = 5
        velocidade_obstaculo = 7

        tipo_obstaculo = 0
        self.obstaculos.renderizar(tipo_obstaculo)
        xo = random.randrange(125, 660)
        yo = -500

        # Info Hazard
        h_width = 130 #55
        h_height = 130 #120

        # movimento da margem esquerda
        movL_x = 0
        movL_y = 0

        # movimento da margem direita
        movR_x = 740
        movR_y = 0

        # Criar o Plano de fundo
        self.background = Fundo()

        # Posicao do Player
        x = 372
        y = 475

        # Criar o Player
        self.player = Jogador(x, y)

        # # Criar Harzard_1
        # self.hazard_1 = Obstaculos("Images/nave.png", xo, yo)

        # # Criar Harzard_2
        # self.hazard_2 = Obstaculos("Images/satelite.png", xo, yo)

        # # Criar Harzard_3
        # self.hazard_3 = Obstaculos("Images/cometa.png", xo, yo)

        # # Criar Harzard_4
        # self.hazard_4 = Obstaculos("Images/planeta.png", xo, yo)

        # # Criar Harzard_5
        # self.hazard_5 = Obstaculos("Images/ameaca.png", xo, yo)

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = 16

        # assim iniciamos o loop principal do programa
        while self.run:

            clock.tick(1000 / dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.eventos.controle()
            x = self.eventos.atualizar()

            # Atualiza Elementos
            self.elements_update(dt)

            # Desenha o background buffer
            self.elements_draw()

            # adiciona movimento ao background

            self.move_background (movL_x, movL_y, movR_x, movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > 640 and movR_y > 640:
                movL_y -= 640
                movR_y -= 640

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover

            # Mostrar Player
            self.draw_player(self.eventos.x, y)

            # Mostrar score
            self.interface.pontuacao(self.tela, o_passados, pontuacao)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            if x > 760 - 92 or x < 40 + 5:
                self.interface.msg_colisao("lateral", self.tela)
                self.loop()
                self.run = False

            # loop que redesenha continuamente a posicao
            yo = yo + velocidade_obstaculo/4
            # self.draw_hazard(tipo_obstaculo, xo, yo)
            self.obstaculos.draw(self.tela,xo,yo)
            yo = yo + velocidade_obstaculo

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if yo > 600:
                yo = 0 - h_height
                xo = random.randrange(125, 650 - h_height)
                tipo_obstaculo = random.randint(0, 4)
                # determinando quantos hazard passaram e a pontuação
                o_passados += 1
                pontuacao = o_passados * 10
                self.obstaculos.renderizar(tipo_obstaculo)

            # restrições para o game over
            if y < yo + h_height:
                if x > xo or x > xo - 56:
                    if x < xo + h_width or x < xo - 56:
                        self.interface.msg_colisao("perdeu", self.tela)
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()
# Game:   