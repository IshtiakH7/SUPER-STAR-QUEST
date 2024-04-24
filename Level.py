import pygame.display
from Settings import *


class Level1:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.fill('blue')