import pygame
from constants import settings


pygame.font.init()

class Button(object):

    def __init__(self, size, pos, text):
    

        self.size = size
        self.pos = pos
        self.myfont = pygame.font.SysFont('Arial', 30)
        self.textSurface = self.myfont.render(text, False, (0, 0, 0))

        self.rect = pygame.Rect((self.pos[0]-self.size[0]//2, self.pos[1]-self.size[1]//2),
                                                            (self.size[0], self.size[1]))

    def isClicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
    



    def drawButton(self):
        white = (255, 255, 255)
        x = self.textSurface.get_rect().width/2
        y = self.textSurface.get_rect().height/2
        pygame.draw.rect(settings.WIN, white, self.rect)
        settings.WIN.blit(self.textSurface,(self.pos[0]-x, self.pos[1]-y))

        



