import pygame
import sys
import game

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feraz")
clock = pygame.time.Clock()


#Main Function, game loop calling the main class, update, and draw functions
def main():
    running = True
    #Handle Events
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        GameState.update_logic()
        GameState.update_graphics()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()   
    sys.exit()
    
if __name__ == "__main__":
    main()
