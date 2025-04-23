import pygame 
from main import SCREEN_HEIGHT 

class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity=0.5):
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0
        self.gravity = gravity
        self.max_fall_speed = 10  # Define max fall speed
        self.on_ground = False

    def handle_gravity(self):
        if not self.on_ground:  # Only apply gravity if not on the ground
            self.velocity_y += self.gravity
            if self.velocity_y > self.max_fall_speed:  # Max fall speed
                self.velocity_y = self.max_fall_speed

def handle_collisions(self, tiles):
    # Vertical movement
    self.rect.y += self.y_velocity
    self.is_on_ground = False  # Reset, will be set to True if collision happens

    for tile in tiles:
        if self.rect.colliderect(tile.rect):
            if self.y_velocity > 0:  # Falling
                self.rect.bottom = tile.rect.top
                self.y_velocity = 0
                self.is_on_ground = True
            elif self.y_velocity < 0:  # Jumping
                self.rect.top = tile.rect.bottom
                self.y_velocity = 0

    # Horizontal movement
    self.rect.x += self.x_velocity

    for tile in tiles:
        if self.rect.colliderect(tile.rect):
            if self.x_velocity > 0:  # Moving right
                self.rect.right = tile.rect.left
                self.x_velocity = 0
            elif self.x_velocity < 0:  # Moving left
                self.rect.left = tile.rect.right
                self.x_velocity = 0