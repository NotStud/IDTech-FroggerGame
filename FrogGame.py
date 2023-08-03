import pygame

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT, = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption("Frog Game")

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 255)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

while(True):
    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)
    pygame.display.flip()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()