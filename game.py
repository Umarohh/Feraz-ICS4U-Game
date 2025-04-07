import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Game State Constants
MAIN_MENU = "main_menu"
IN_GAME = "in_game"
PAUSE = "pause"
GAME_OVER = "game_over"

class GameState:
    def __init__(self, screen):
        self.screen = screen
        self.state = MAIN_MENU  # The game starts in the main menu

    def update_logic(self):
        # Update game logic based on the current game state
        if self.state == MAIN_MENU:
            self.show_main_menu()
        elif self.state == IN_GAME:
            self.play_game()
        elif self.state == PAUSE:
            self.show_pause_screen()
        elif self.state == GAME_OVER:
            self.show_game_over()

    def update_graphics(self):
        # Update game graphics based on the current game state
        if self.state == MAIN_MENU:
            self.draw_main_menu()
        elif self.state == IN_GAME:
            self.draw_game()
        elif self.state == PAUSE:
            self.draw_pause_screen()
        elif self.state == GAME_OVER:
            self.draw_game_over()

    # Functions for the menu states
    def show_main_menu(self):
        """Menu Logic"""
        pass

    def draw_main_menu(self):
        """Menu Graphics"""
        pass

    def show_pause_screen(self):
        """Pause Logic"""
        print("Game is paused. Press any key to resume.")

    def draw_pause_screen(self):
        """Pause Graphics"""
        self.screen.fill((50, 50, 50))  # Dark gray background
        print("Drawing pause screen...")

    def show_game_over(self):
        """Game Over Logic"""
        print("Game Over! Returning to main menu.")
        self.state = MAIN_MENU

    def draw_game_over(self):
        """Game Over Graphics"""
        self.screen.fill((100, 0, 0))  # Red background
        print("Drawing game over screen...")

    def play_game(self):
        """Main game loop logic."""
        if hasattr(self, 'level_manager') and self.level_manager:
            self.level_manager.play_game()
        else:
            print("Level manager is not defined!")

    def draw_game(self):
        """Draw the game level."""
        if hasattr(self, 'level_manager') and self.level_manager:
            self.level_manager.draw_game()
        else:
            print("Level manager is not defined!")
