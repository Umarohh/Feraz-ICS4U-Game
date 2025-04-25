import pygame
from Levels.level_dependancies import Level
from Scripts.player import Player
from Scripts.tile import Tile
from Scripts.tile import Tilemap


class Level1(Level):
    def __init__(self, screen):
        super().__init__(screen)  # Calls Level's __init__, so screen and not completed are set
        self.tiles = Tilemap.create_tiles("Assets/Maps/example.txt")

    def update_logic(self):
        """Level 1 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed

    def update_graphics(self):
        """Level 1 Graphics"""
        self.screen.blit(self.player.image, self.player.rect)
        self.tilemap.render(self.screen)

    def check_completion_condition(self):
        """Check if the level is completed"""
        # Placeholder for actual completion logic
        # For example, check if a certain condition is met in the game
        return False
    
    