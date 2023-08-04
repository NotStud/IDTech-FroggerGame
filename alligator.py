import pygame
from log import Log


class Alligator(Log):
    # Define constant values
    IMAGE = pygame.image.load('alligator.png')

    # Creates an Alligator object
    def __init__(self, starting_position: tuple, direction: str):
        super().__init__(starting_position, direction)
        # This line will flip the sprite to face right or left based on the value of self.direction
        self.image = Alligator.IMAGE if self.direction == 'Left' else pygame.transform.flip(Alligator.IMAGE, True, False)