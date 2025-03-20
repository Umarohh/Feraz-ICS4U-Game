import pygame
import sys

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feraz-ICS4U-GAME")
clock = pygame.time.Clock(FPS)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
