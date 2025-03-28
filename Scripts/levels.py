from Levels.level_1 import Level1  # Import level 1 class from file
from Levels.level_2 import Level2  # Import level 2 class from file
from Levels.level_3 import Level3  # Import level 3 class from file
from Levels.level_dependancies import Level



class LevelManager:
    def __init__(self, screen):
        self.screen = screen
        self.levels = [Level1(screen), Level2(screen), Level3(screen)]  # List of levels from level classes
        self.current_level_index = 0  # Start at the first in the index
        self.current_level = self.levels[self.current_level_index]  # The level is the level in the current index
    
    def load_next_level(self):
        """Advance to the next level if available"""
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.current_level = self.levels[self.current_level_index]
        else: 
            pass

    def update (self):  # level__manager.update calls each level to update independantly
        if self.current_level:
            self.current_level.update() # level_1.update, level_2.update, etc...

        if self.current_level.is_completed():
            self.load_next_level()

    def draw(self): # level__manager.draw calls each level to render independantly
        if self.current_level:
            self.current_level.draw() # level_1.draw, level_2.draw, etc...

