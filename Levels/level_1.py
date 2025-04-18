import pygame
from Levels.level_dependancies import Level
from Scripts.player import Player

class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__, so screen and not completed are set

    def update_logic(self):
        """Level 1 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def update_graphics(self):
        """Level 1 Graphics"""
        self.screen.fill((0, 0, 0))  # Clear the screen first
        self.screen.blit(self.player.image, self.player.rect)

    def check_completion_condition(self):
        """Check if the level is completed"""
        # Placeholder for actual completion logic
        # For example, check if a certain condition is met in the game
        return False
    
    