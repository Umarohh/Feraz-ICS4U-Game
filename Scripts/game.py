import pygame
from pygame.locals import *
from Scripts.levels import LevelManager  # Import LevelManager

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
        self.level_manager = LevelManager(screen)  # Create an instance of LevelManager, to be called when in game

    def update_logic(self):
        """Update game logic based on current game state"""
        if self.state == MAIN_MENU:
            self.show_main_menu()
        elif self.state == IN_GAME:
             self.level_manager.update_logic()  # Calls to level_manager in levels.py to update level logic
        elif self.state == PAUSE:
            self.show_pause_screen()
        elif self.state == GAME_OVER:
            self.show_game_over()

    def update_graphics(self):
        """Update game graphics based on current game state"""
        if self.state == MAIN_MENU:
            self.draw_main_menu()
        elif self.state == IN_GAME:
            self.level_manager.update_graphics()  # Calls to level_manager in levels.py to update level graphics
        elif self.state == PAUSE:
            self.draw_pause_screen()
        elif self.state == GAME_OVER:
            self.draw_game_over()

    # Menu State Functions
    def show_main_menu(self):
        """Menu Logic"""
        if keys[pygame.K_RETURN]:
            self.state = IN_GAME


    def draw_main_menu(self):
        """Menu Graphics"""
        title_image = pygame.image.load("Assets/title_screen.jpeg").convert()
        title_image = pygame.transform.scale(title_image, self.screen.get_size())
        self.screen.blit(title_image, (0, 0))

    def show_pause_screen(self):
        """Pause Logic"""
        pass

    def draw_pause_screen(self):
        """Pause Graphics"""
        pass

    def show_game_over(self):
        """Game Over Logic"""
        pass
    
    def draw_game_over(self):
        """Game Over Graphics"""
        pass
