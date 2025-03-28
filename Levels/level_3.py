import pygame
from Levels.level_dependancies import Level

class Level3(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__, so screen and completed are set

    def update(self):
        """Level 3 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def draw(self):
        """Render Level 3"""
        pass
