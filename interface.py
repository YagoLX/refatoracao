import pygame
import time

class Interface:
    def __init__(self):
        self.my_font = pygame.font.Font("Fonts/Fonte4.ttf", 100)
    

    def msg_colisao(self, tipo, tela):
        bateu_lateral = self.my_font.render("COLISÃO!", 0,(255, 255, 255))
        bateu = self.my_font.render("GAME OVER!", 0, (255, 0, 0))

        if(tipo == "perdeu"):
            tela.blit(bateu, (80, 200))
            pygame.display.update()
            time.sleep(3)
        else:
            tela.blit(bateu_lateral, (80, 200))
            pygame.display.update()
            time.sleep(3)
        
    def pontuacao(self, tela, o_passados, pontos):
        font = pygame.font.SysFont(None, 35)
        passou = font.render("Passou: " + str(o_passados), True, (255, 255, 128))
        pontos = font.render("Score: " + str(pontos), True, (253, 231, 32))
        tela.blit(passou, (0, 50))
        tela.blit(pontos, (0, 100))