import pygame
from Levels.level_dependancies import Level


class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__, so screen and completed are set

    def update(self):
        """Level 1 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def draw(self):
        """Render Level 1"""
        pass

    def check_completion_condition(self):
        self.completed = True  # Level is completed if condition is met
       
    def is_completed(self):
        """Return whether the level is completed to outside classes such as level_manager"""
        return self.completed