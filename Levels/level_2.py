import pygame
from Levels.level_dependancies import Level

class Level2(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__, so screen and not completed are set

    def update_logic(self):
        """Level 2 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def update_graphics(self):
        """Level 2 Graphics"""
        pass

    def check_completion_condition(self):
        """Check if the level is completed"""
        # Placeholder for actual completion logic
        # For example, check if a certain condition is met in the game
        return False

 