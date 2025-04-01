from Levels.level_1 import Level1  # Import level 1 class from file
from Levels.level_2 import Level2  # Import level 2 class from file
from Levels.level_3 import Level3  # Import level 3 class from file
from Levels.level_dependancies import Level

class LevelManager:
    """Class to manage the order and updating of levels of the game"""
    def __init__(self, screen):
        self.screen = screen
        self.levels = [Level1(screen), Level2(screen), Level3(screen)]  # Chronological order of levels
        self.current_level_index = 0  # Start at level 1
        self.current_level = self.levels[self.current_level_index]  # The level is the currently indexed level
    
    def load_next_level(self):
        """Advance to the next level if available"""
        if self.current_level_index < len(self.levels) - 1: # If there is a next level
            self.current_level_index += 1 # Increment the level number in the index
            self.current_level = self.levels[self.current_level_index] # The current level is the currently indexed level
        else: 
            pass

    def update_logic (self):  
        """In game update logic"""
        if self.current_level:
            self.current_level.update_graphics() # Update logic depending on current level

        if self.current_level.is_completed(): 
            self.load_next_level() # If the current level is completed, load the next level

    def update_graphics(self): 
        """In game rendering logic"""
        if self.current_level:
            self.current_level.update_logic() # Update graphics depending on current level

