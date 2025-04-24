import pygame
import sys
from Scripts.game import GameStateManager
from Scripts.player import Player

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feraz")
clock = pygame.time.Clock()
gsm = GameStateManager(screen)

#Main Function, game loop calling the main class, update, and draw functions
def main():
    running = True
    #Handle Events
    while running:
        events = pygame.event.get()  # Get events here
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        gsm.handle_events(events)
        gsm.update_logic()
        screen.fill(0, 0, 0)
        gsm.update_graphics()
        Player.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()   
    sys.exit()
    
if __name__ == "__main__":
    main()