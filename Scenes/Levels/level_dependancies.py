import pygame

class Level:
    def __init__(self, screen):
        """Initialize the parent level class"""
        self.screen = screen
        self.completed = False  # Track if the level is completed

    def check_completion_condition(self): # Ensures all levels have a completion condition regardless of specific update method
        pass 
       
    def is_completed(self):
        """Return whether the level is completed to outside classes such as level_manager"""
        return self.completed
    
    def update(self):   
        """Ensures all levels update regardless of specific update method"""
        pass

    def draw(self): 
        """Ensures all levels render regardless of specific update method"""
        pass