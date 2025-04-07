import pygame
from player import Player

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets
forest_background = pygame.image.load("assets/forest_background.png")
forest_background = pygame.transform.scale(forest_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Platform settings
PLATFORM_COLOR = (139, 69, 19)
platforms = [
    pygame.Rect(200, 500, 200, 20),
    pygame.Rect(500, 400, 200, 20),
    pygame.Rect(800, 300, 200, 20),
]

def draw_tutorial_text(screen, font):
    tutorial_texts = [
        "Use LEFT and RIGHT arrows to move.",
        "Press SPACE to jump.",
        "Press UP while in air to climb walls.",
        "Hold LEFT SHIFT to dash.",
        "Press 'A' to attack enemies.",
    ]
    for i, text in enumerate(tutorial_texts):
        label = font.render(text, True, BLACK)
        screen.blit(label, (50, 50 + i * 30))

def level1():
    player = Player(100, SCREEN_HEIGHT - 150)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(forest_background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                player.attack()

        # Move the player
        player.move()

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(screen, PLATFORM_COLOR, platform)

        # Draw tutorial text
        draw_tutorial_text(screen, font)

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Run Level 1
if __name__ == "__main__":
    level1()
