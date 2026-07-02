import pygame

class Colisao:
    def __init__(self,x, y, xo, yo):
        self.x = x
        self.y = y
        self.xo = xo
        self.yo = yo

    def verifica_colisao(self):
        
        if self.x > 760 - 92 or self.x < 40 + 5:
            self.screen.blit(self.render_text_bateulateral, (80, 200))
            pygame.display.update()  # atualizar a tela
            time.sleep(3)
            self.loop()
            self.run = False
        
    