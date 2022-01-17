import pygame

from constants import *

class Game(object):

    def __init__(self):

        self.isOver = False

        self.size = 625

        self.board = pygame.Rect((settings.WIDTH/2-self.size/2, settings.HEIGHT/2-self.size/2),
                                (self.size, self.size))


    def isGameOver(self):
        return self.isOver

    

    def drawBoard(self):

        pygame.draw.rect(settings.WIN, color.BLACK, self.board, width = 5)

        pass

    def drawCanvas(self):
        settings.WIN.fill((255,255,255))
        pygame.display.set_icon(images.windowIcon)
        self.drawBoard()


        pygame.display.update()
