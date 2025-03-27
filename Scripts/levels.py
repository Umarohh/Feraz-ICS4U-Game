import pygame
from levels.level_1 import Level1  # Import level 1 Class


class LevelManager:
    def __init__(self, screen):
        self.screen = screen
        self.current_level = None  # No level loaded at start
    
    def load_level(self, level):
        self.current_level = level

    def update(self):
        self.current_level.update()

    def draw(self):
        self.current_level.draw()