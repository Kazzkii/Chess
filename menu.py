import pygame
from constants import *

from button import Button

class Menu(object):

    def __init__(self):

        self.isStart = False

        self.playBtn = Button((200, 50), (settings.WIDTH//2, settings.HEIGHT//2), 'Play')
        pass


    def isPlay(self):

        return self.isStart

    def update(self):
        if self.playBtn.isClicked():
            self.isStart = True



    def drawCanvas(self):
        settings.WIN.fill(color.OFFWHITE)
        pygame.display.set_icon(images.windowIcon)

        #settings.WIN.blit(images.windowMenu, (0, 0))

        self.playBtn.drawButton()

        pygame.display.update()
