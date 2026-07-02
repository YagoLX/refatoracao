import pygame
import os

class CarregarArquivos:

    def __init__(self, pasta_base = "Images"):
        self.pasta_base = pasta_base
        self.imagens = {}
        self.carregar_tudo()



    def concatenar(self, nome_arquivo):
        caminho = os.path.join(self.pasta_base, nome_arquivo)
        return pygame.image.load(caminho)



    def carregar_tudo(self):
        self.imagens = {
            "ameaca": self.concatenar("background.png"),
            "background": self.concatenar("background.png"),
            "cometa": self.concatenar("cometa.png"),
            "game_over": self.concatenar("Game_Over.png"),
            "margin_1": self.concatenar("margin_1.png"),
            "margin_2": self.concatenar("margin_2.png"),
            "nave": self.concatenar("nave.png"),
            "player": self.concatenar("player.png"),
            "planeta": self.concatenar("planeta.png"),
            "satelite": self.concatenar("satelite.png"),
        }

    #Função utilizada para carregar uma imagem a partir da chave definida acima no dicionário
    def imagem(self, nome):
        return self.imagens[nome]