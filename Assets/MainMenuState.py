import sys
import pygame
from Scripts.game import GameState
from Scripts.ui import Button

class MainMenuState(GameState):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            Button((350, 300, 200, 50), "Start Game", self.start_game),
            Button((350, 370, 200, 50), "Quit", self.quit_game)
        ]

    def start_game(self):
        # Switch to gameplay state
        print("Starting game...")

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update_logic(self):
        # Handle input and logic for the main menu (e.g., button clicks)
        pass

    def update_graphics(self, surface):
        surface.fill((0, 0, 0))  # Fill screen with black
        for button in self.buttons:
            button.draw(surface)  # Draw buttons

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)
