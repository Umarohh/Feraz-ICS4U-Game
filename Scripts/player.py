import pygame
import os
from main import SCREEN_HEIGHT 
# I have to still import and manage tiles

class Player(pygame.sprite.Sprite):         # Player class inherits from pygame.sprite.Sprite
    def __init__(self, x, y):
        super().__init__()
        self.load_images()  # Load all animations
        self.image = self.idle_frames[0]  # Initialize with the first idle frame
        self.rect = self.image.get_rect(center=(x, y))
        self.current_frame = 0  # Track the current frame
        self.frame_timer = 0  # Timer to control animation speed
        self.current_animation = "idle"  # Initialize current animation
        self.velocity_x = 0  # Initialize horizontal velocity
        self.velocity_y = 0  # Initialize vertical velocity
        self.on_ground = False  # Initialize ground state
        self.speed = 5  # Define player speed
        self.idle()  # You start as idle
            
    def load_animation(self, folder_path, animation_name, frame_count):
        """Loads the animation frames from the specified folder"""
        frames = []
        for i in range(1, frame_count + 1):
            path = os.path.join(folder_path, f"{animation_name}_{i}.png")
            image = pygame.image.load(path).convert_alpha()  # Load the image and keep transparency
            frames.append(image)
        return frames

    def load_images(self):
        """Load all animations from assets folder"""
        self.idle_frames = self.load_animation("assets/player", "idle", 4)
        self.walking_frames = self.load_animation("assets/player", "walking", 6)
        self.sprinting_frames = self.load_animation("assets/player", "sprinting", 6)
        self.jumping_frames = self.load_animation("assets/player", "jumping", 1)  # 1 frame for jumping
        self.falling_frames = self.load_animation("assets/player", "falling", 1)  # 1 frame for falling
         # Store all animations in a dictionary
        self.animations = {
            "idle": self.idle_frames,
            "walk": self.walking_frames,
            "sprint": self.sprinting_frames,
            "jump": self.jumping_frames,
            "fall": self.falling_frames,
            }
    
    def set_animation(self, name):
       """Switch to a new animation"""
       if name != self.current_animation:
            self.current_animation = name
            self.current_frame = 0
            self.frame_timer = 0
            self.image = self.animations[name][self.current_frame]

    def update_animation(self):
        """Update the current animation frame"""
        self.frame_timer += 1

        # Change frame every 5 game loops (adjust for speed)
        if self.frame_timer > 5:
            self.frame_timer = 0
            self.current_frame += 1

            # Loop back to the first frame if we've reached the end of the animation
            if self.current_frame >= len(self.animations[self.current_animation]):
                self.current_frame = 0

            # Set the image to the next frame
            self.image = self.animations[self.current_animation][self.current_frame]


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
      
    def handle_gravity(self):
        GRAVITY = 0.5  # Define GRAVITY constant
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

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
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0  # Stop downward movement

        # Check if player is above the screen (if needed)
        if self.rect.top < 0:
            self.rect.top = 0  # Align the player's top edge with the top of the screen
            self.velocity_y = 0  # Stop upward movement

    def idle(self):
        # Placeholder for idle behavior
        self.set_animation("idle")

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
        pass

    def update(self):
        tiles = []  # Ensure tiles is defined
        self.handle_input()
        self.handle_gravity()
        self.handle_collisions(tiles)
        self.update_animation()  # Update animation frame based on the current animation
