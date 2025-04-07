import pygame
import sys

# Game settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAME_RATE = 60

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feraz-ICS4U-Game")
game_clock = pygame.time.Clock()

def game_loop():
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                is_running = False

        # Fill the screen with a background color
        window.fill((30, 30, 30))  # Dark gray background

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        game_clock.tick(FRAME_RATE)

if __name__ == "__main__":
    game_loop()
    pygame.quit()
    sys.exit()
