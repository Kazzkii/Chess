import pygame

from menu import Menu
from game import Game
from constants import *



class Program:
    def __init__(self):

        self.menu = Menu()
        self.game = Game()

        self.currentState = self.menu


    def switchStates(self):

        if self.menu.isPlay():
            self.currentState = self.game

        elif self.game.isGameOver():
            self.currentState = self.menu

    def update(self):

        self.menu.update()


        self.switchStates()

    def drawCanvas(self):
        self.currentState.drawCanvas()



def main():
    program = Program()
    run = True
    clock = pygame.time.Clock()
    

    
    while run :
        
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        program.drawCanvas()
        program.update()
    


    pygame.quit()

if __name__ == '__main__':

    main()