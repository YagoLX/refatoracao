# Código para refatoração - Viagem Espacial
from obstaculo import Obstaculo
from jogador import Jogador
from jogo import Jogo
from fundo import Fundo
import pygame
import random
import time

def main():
    # Cria o objeto game e chama o loop básico
    game = Jogo("resolution", "fullscreen")
    game.loop()
# main()

# Chama a função main
##Precisa disso? nao é só rodar a main?
if __name__ == '__main__':
    main()