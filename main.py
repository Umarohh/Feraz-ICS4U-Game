import pygame
import sys
from Scripts.ui import GameStateManager  # Import GameStateManager
from Scripts.states.GameplayState import GameplayState
from Scripts.states.MainMenuState import MainMenuState

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feraz")
clock = pygame.time.Clock()

# Initialize the game state manager
game_manager = GameStateManager(screen)

# Add states
game_manager.add_state("main_menu", MainMenuState(screen))
game_manager.add_state("gameplay", GameplayState(screen))

# Set initial state
game_manager.change_state("main_menu")

# Main Game Loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass events to the current game state
            game_manager.handle_event(event)

        # Update the current game state logic
        game_manager.update()

        # Draw the current game state graphics
        game_manager.draw(screen)

        # Update the display and control frame rate
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
