from abc import ABC, abstractmethod
from eventos import Eventos
import pygame
import random
from fundo import Fundo
from eventos import Eventos
from colisao import Colisao
from interface import Interface
from elementos import *


class EstadoJogo(ABC):
    def __init__(self, jogo):
        self.jogo = jogo

    @abstractmethod
    def processar_eventos(self, eventos): ...
    @abstractmethod
    def atualizar(self, dt): ...
    @abstractmethod
    def desenhar(self, tela): ...


class Jogando(EstadoJogo):
    def processar_eventos(self, eventos):
        #controle do jogador
            self.jogo.eventos.controle()
            self.jogo.x = self.jogo.eventos.atualizar()

    def atualizar(self, dt):
        # loop que redesenha continuamente a posicao
        self.jogo.background.update(dt)


        self.jogo.yo = self.jogo.yo + self.jogo.velocidade_obstaculo

        if self.jogo.x > 760 - 92 or self.jogo.x < 40 + 5:
                self.jogo.trocar_estado(ColidiuParede(self.jogo))
                return #jogo não acaba


        # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
        if self.jogo.yo > 600:
            self.jogo.yo = 0 - self.jogo.altura_o
            self.jogo.xo = random.randrange(125, 650 - self.jogo.altura_o)
            self.jogo.tipo_obstaculo = random.randint(0, 4)
            # determinando quantos hazard passaram e a pontuação
            self.jogo.o_passados += 1
            self.jogo.pontuacao = self.jogo.o_passados * 10
            self.jogo.obstaculos.renderizar(self.jogo.tipo_obstaculo)



        # restrições para o game over
        if self.jogo.y < self.jogo.yo + self.jogo.altura_o:
            if self.jogo.x > self.jogo.xo or self.jogo.x > self.jogo.xo - 56:
                if self.jogo.x < self.jogo.xo + self.jogo.largura_o or self.jogo.x < self.jogo.xo - 56:
                    self.jogo.trocar_estado(ColidiuObjeto(self.jogo))
                    return #na proxima vai trocar a bool
        

    def desenhar(self, tela):
            
        #atualizacao do fundo

        self.jogo.background.draw(tela)
        self.jogo.obstaculos.draw(tela,self.jogo.xo,self.jogo.yo)

        # Mostrar Player
        self.jogo.jogador.draw(tela, self.jogo.eventos.x, self.jogo.y)

        # Mostrar score
        self.jogo.interface.pontuacao(tela, self.jogo.o_passados, self.jogo.pontuacao)


class ColidiuParede(EstadoJogo):
    # jogo continua: reposiciona/limita a nave e volta a jogar
    def processar_eventos(self, eventos):
        pass

    def atualizar(self, dt):

        self.jogo.trocar_estado(Jogando(self.jogo))

    def desenhar(self, tela):
        self.jogo.interface.msg_colisao("lateral", tela)


class ColidiuObjeto(EstadoJogo):
    # fim de jogo
    def processar_eventos(self, eventos):
        pass

    def atualizar(self, dt):
        self.jogo.run = False

    def desenhar(self, tela):
        self.jogo.interface.msg_colisao("perdeu", tela)