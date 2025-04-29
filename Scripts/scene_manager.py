from Levels.level_1 import Level1  # Import level 1 class from file
from Levels.level_2 import Level2  # Import level 2 class from file
from Levels.level_3 import Level3  # Import level 3 class from file
from Cutscenes.cutscene_1 import Cutscene1  # Import Cutscene 1 class from file
from Cutscenes.cutscene_2 import Cutscene2  # Import Cutscene 2 class from file
from Cutscenes.cutscene_3 import Cutscene3  # Import Cutscene 3 class from file
from Levels.level_dependancies import Level
from Scripts.camera import Camera
from Scripts.tile import Tile
from Scripts.tile import Tilemap
from Scripts.player import Player

class SceneManager:
    """Class to manage the order and updating of levels of the game"""
    def __init__(self, screen):
        self.screen = screen
        self.scenes = [Cutscene1(self.screen), Level1(self.screen, self.camera, self.player), Level2(self.screen, self.camera, self.player), Cutscene2(self.screen), Level3(self.screen, self.camera, self.player), Cutscene3(self.screen)]  # Chronological order of levels
        self.current_scene_index = 1  # Start at Level 1
        self.current_scene = self.scenes[self.current_scene_index]  # The scene is the currently indexed scene
        self.camera = Camera() # Create a camera object
        self.player = Player(100, 100)

    def load_next_scene(self):
        """Advance to the next level if available"""
        if self.current_scene_index < len(self.scenes) - 1: # If there is a next level
            self.current_scene_index += 1 # Increment the level number in the index
            self.current_scene = self.scenes[self.current_scene_index] # The current level is the currently indexed level
        else: 
            pass

    def update_logic (self):  
        """In game update logic"""

        if self.current_scene:
            self.current_scene.update_logic() # Update graphics depending on current level
        if self.current_scene.is_completed(): 
            self.load_next_scene() # If the current level is completed, load the next level
        if isinstance(self.current_scene, Level):
            self.camera.update(self.player)  # Update camera position based on player
            self.player.update

    
        if self.scene_manager.is_finished():
            self.game_state_manager.change_state("game_over")

    def update_graphics(self): 
        """In game rendering logic"""
        if self.current_scene:
            self.current_scene.update_graphics() # Update logic depending on current level
        if isinstance(self.current_scene, Level):
            self.player.render(self.screen)

