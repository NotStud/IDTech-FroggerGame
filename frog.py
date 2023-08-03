import pygame
import sys
sys.path.append('https://replit.com/@NotStudioGaming/FrogGame-2#Frog.py')

from frog import Frog

class Frog(pygame.sprite.Sprite):

    # Define constant values
    IMAGE = pygame.image.load('ChainSawDog.png')
    STARTING_POSITION = (300, 490)
    SIZE = (20, 10)

    # Creates a Frog object
    def __init__(self):

        # sprite set up
        super().__init__()
        self.image = Frog.IMAGE

        # rectangle frog
        self.rect = pygame.Rect((0, 0), Frog.SIZE)
        self.rect.center = Frog.STARTING_POSITION
      
    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Frog.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= Frog.SCREEN_DIM[1] - 20:
            self.rect.centery += Frog.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Frog.MOVE_DIST

    def move_right(self):
        if self.rect.right <= Frog.SCREEN_DIM[0] - 20:
            self.rect.centerx += Frog.MOVE_DIST