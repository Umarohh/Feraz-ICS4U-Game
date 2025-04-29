import pygame
from Levels.level_dependancies import Level
from Scripts.tile import Tile
from Scripts.tile import Tilemap

class Level1(Level):
    def __init__(self, screen, camera, player):
        super().__init__(screen)  # Calls Level's __init__, so screen and not completed are set
        self.tilemap = Tilemap()
        self.tilemap.load_from_file("Assets/Levels/Level1/Map/level_1_tilemap.txt")
        self.load_backgrounds("Assets/Levels/Level1/Background/sky_moon.png", 
                               "Assets/Levels/Level1/Background/clouds.png", 
                               "Assets/Levels/Level1/Background/back_trees.png",
                               "Assets/Levels/Level1/Background/middle_trees.png",
                               "Assets/Levels/Level1/Background/front_trees.png")

    def update_logic(self):
        """Level 1 logic"""
        if self.check_completion_condition():  
            self.completed = True  # Mark level as completed
        self.tilemap.update()

    def update_graphics(self):
        """Level 1 Graphics"""
        self.screen.blit(self.player.image, self.player.rect)
        self.tilemap.render(self.screen)
        camera_x = self.camera.camera.x  # Access camera position directly
        self.render_parallax(self.screen, camera_x)  # Render parallax background layers

    def check_completion_condition(self):
        """Check if the level is completed"""
        # Placeholder for actual completion logic
        # For example, check if a certain condition is met in the game
        return False