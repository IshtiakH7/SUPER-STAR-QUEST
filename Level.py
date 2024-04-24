import pygame.display

from Settings import *

class Level1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.fill('gray')