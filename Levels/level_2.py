import pygame
from Levels.level_dependancies import Level


class Level2(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__

    def update(self):
        """Level 2 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def draw(self):
        """Render Level 2"""
        pass

 