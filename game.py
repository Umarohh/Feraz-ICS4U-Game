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
        self.state = MAIN_MENU  # the game starts in the main menu

    def update_logic(self):
        # Update game logic based on current game state
        if self.state == MAIN_MENU:
            self.show_main_menu()
        elif self.state == IN_GAME:
            self.play_game()
        elif self.state == PAUSE:
            self.show_pause_screen()
        elif self.state == GAME_OVER:
            self.show_game_over()

    def update_graphics(self):
        # Update game graphics based on current game state.
        if self.state == MAIN_MENU:
            self.draw_main_menu()
        elif self.state == IN_GAME:
            self.draw_game()
        elif self.state == PAUSE:
            self.draw_pause_screen()
        elif self.state == GAME_OVER:
            self.draw_game_over()

    # Functions for each state
    def show_main_menu(self):
        """main menu logic"""
        pass

    def draw_main_menu(self):
        """main menu graphics"""
        pass

    def play_game(self):
        """Main game loop logic."""
        pass

    def show_pause_screen(self):
        """Display the pause screen."""
        pass

    def show_game_over(self):
        """Display the game over screen."""
        pass

    def draw_game(self):
        """Draw the game level."""
        pass

    def draw_pause_screen(self):
        """Draw the pause screen."""
        pass

    def draw_game_over(self):
        """Draw the game over screen."""
        pass
