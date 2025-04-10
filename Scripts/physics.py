import pygame 
from main import SCREEN_HEIGHT 

class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, x, y, gravity=0.5):
        super().__init__()
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = gravity
        self.max_fall_speed = 10  # Define max fall speed
        self.on_ground = False

        self.speed = 5  # Define player speed

    def handle_gravity(self):
        self.velocity_y += self.gravity

    def handle_collisions(self, tiles):
        # Handling vertical movement (Y-axis)
        self.rect.y += self.velocity_y
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.velocity_y > 0:  # Falling
                    self.rect.bottom = tile.rect.top  # Place the player on top of the tile
                    self.velocity_y = 0  # Stop downward movement
                    self.on_ground = True  # Mark as on the ground
                elif self.velocity_y < 0:  # Moving up (e.g., jumping)
                    self.rect.top = tile.rect.bottom  # Place the player below the tile
                    self.velocity_y = 0  # Stop upward movement

        # Handling horizontal movement (X-axis)
        self.rect.x += self.velocity_x
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                if self.velocity_x > 0:  # Moving right
                    self.rect.right = tile.rect.left  # Prevent player from going through the tile
                    self.velocity_x = 0  # Stop rightward movement
                elif self.velocity_x < 0:  # Moving left
                    self.rect.left = tile.rect.right  # Prevent player from going through the tile
                    self.velocity_x = 0  # Stop leftward movement

        # Check if player is falling below the screen
            self.rect.bottom = SCREEN_HEIGHT  # Ensure player doesn't fall below screen
            self.velocity_y = 0  # Stop downward movement

        # Check if player is above the screen (if needed)
        if self.rect.top < 0:
            self.rect.top = 0  # Align the player's top edge with the top of the screen
            self.velocity_y = 0  # Stop upward movement
