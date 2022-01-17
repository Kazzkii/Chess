import pygame

class settings:
    WIDTH, HEIGHT = 1280, 720
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60

class images:
    windowIcon = pygame.image.load('Assets\Images\icon.png')
    windowMenu = pygame.image.load('Assets\Images\menu.jpg')
    windowMenu = pygame.transform.scale(windowMenu, (1280,720))


class color:

    OFFWHITE = (248, 240, 227)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
