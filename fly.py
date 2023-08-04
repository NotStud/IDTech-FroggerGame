import pygame


class Fly(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('fly.png')
    SIZE = (20, 10)
    SCREEN_DIM = 600, 500

    # Creates a Fly object
    def __init__(self, position: tuple):
        # Sprite Information
        super().__init__()
        self.image = Fly.IMAGE
        # Fly Information
        self.rect = pygame.Rect((0, 0), Fly.SIZE)
        self.rect.center = position