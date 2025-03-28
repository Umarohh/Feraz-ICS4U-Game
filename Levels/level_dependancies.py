import pygame

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.completed = False  # Track if the level is completed

    def check_completion_condition(self):
        self.completed = True  # Level is completed if condition is met
       
    def is_completed(self):
        """Return whether the level is completed to outside classes such as level_manager"""
        return self.completed
    
    def update(self):   # not necessary, only for if level# classes do not have their own update method, avoiding an attribute error
        pass

    def draw(self):  # not necessary, only for if level# classes do not have their own draw method, avoiding an attribute error
        pass