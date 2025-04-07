import pygame
import os
from main import SCREEN_HEIGHT 
# I have to still import and manage tiles

class Player(pygame.sprite.Sprite):         # Player class inherits from pygame.sprite.Sprite
    def __init__(self, x, y):
        super().__init__()                  # Inheritance 
        self.rect = self.image.get_rect(center=(x, y))
        self.load_images()
        self.image = self.idle_frames[0]


    def load_images(self):
        num_idle_frames = len([filename for filename in os.listdir('assets') if filename.startswith('idle_')])
        self.idle_frames = [pygame.image.load(f'assets/idle_{i}.png') for i in range(1, num_idle_frames + 1)]

        num_walking_frames = len([filename for filename in os.listdir('assets') if filename.startswith('walking_')])
        self.walking_frames = [pygame.image.load(f'assets/walking_{i}.png') for i in range(1, num_walking_frames + 1)]
        
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.walk_left()
        if keys[pygame.K_RIGHT]:
            self.walk_right()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump()
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
            self.sprint_right()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]:
            self.sprint_left()
        else:
            self.idle()

    def handle_gravity(self):
        GRAVITY = 0.5  # Define GRAVITY constant
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

    def handle_collisions(self):
        self.rect.bottom = SCREEN_HEIGHT
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
        if self.rect.top < 0:
            tiles = []  # Define tiles as an empty list or populate it with tile objects
        for tile in tiles:
            self.velocity_y = 0
            '''Y axis collision'''
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.velocity.y > 0:     # Falling                        
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                elif self.velocity.y < 0:  # Jumping
                    self.rect.top = tile.rect.bottom
                    self.velocity.y = 0

            '''X axis collision'''
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.velocity.x > 0:     # Moving right
                    self.rect.right = tile.rect.left                        
                    self.velocity.x = 0
                elif self.velocity.x < 0:  # Moving Left
                    self.rect.left = tile.rect.right
                    self.velocity.x = 0
    
    def idle(self):
        # Placeholder for idle behavior
        pass

    def walk_left(self):
        # Placeholder for walking left behavior
        pass

    def walk_right(self):
        # Placeholder for walking right behavior
        pass

    def jump(self):
        # Placeholder for jumping behavior
        pass

    def sprint_left(self):
        # Placeholder for sprinting left behavior
        pass

    def sprint_right(self):
        # Placeholder for sprinting right behavior
        pass    

    def update(self):
        # Placeholder for update logic
        pass