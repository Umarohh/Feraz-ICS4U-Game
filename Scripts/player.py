import pygame
import os
# from main import SCREEN_HEIGHT  # Removed as it is not accessed
from Scripts.physcs import PhysicsObject


# I have to still import and manage tiles

class Player(pygame.sprite.Sprite, PhysicsObject):         # Player class inherits from pygame.sprite.Sprite
    def __init__(self, x, y):
        super().__init__(x, y, gravity=0.5)  # Just pass x, y, and gravity to PhysicsObject
        '''Init Objects'''
        self.load_images()  # Load all animations
        self.image = self.idle_frames[0]  # Initialize with the first idle frame
        self.rect = self.image.get_rect(center=(x, y))
        '''Init Animation Variables'''
        self.current_frame = 0  # Track the current frame
        self.frame_timer = 0  # Timer to control animation speed
        self.current_animation = "idle"  # Initialize current animation
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
        self.jumping_facing_frames = self.load_animation("assets/player", "jumping_facing", 2)  # 1 frame for jumping facing
        self.falling_frames = self.load_animation("assets/player", "falling", 1)  # 1 frame for falling
        # Store all animations in a dictionary
        self.animations = {
            "idle": self.idle_frames,
            "walk": self.walking_frames,
            "sprint": self.sprinting_frames,
            "jump": self.jumping_frames,
            "jump_direction": self.jumping_facing_frames,
            "fall": self.falling_frames
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
        if keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
            self.sprint_right()
        if keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT]:
            self.sprint_left()
        
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump_right()

        if keys[pygame.K_LEFT] and keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump_left()
      

    def idle(self):
        # Placeholder for idle behavior
        self.set_animation("idle")

    def walk_left(self):
        # Placeholder for walking left behavior
        self.x_velocity = -5  # Example speed
        self.set_animation("walk")
        self.image = pygame.transform.flip(self.walking_frames[self.current_frame], True, False)
        self.rect = self.image.get_rect(center=self.rect.center)  # Update rect position

    def walk_right(self):
        # Placeholder for walking right behavior
        self.x_velocity = 5
        self.set_animation("walk")

    def jump(self):
        # Placeholder for jumping behavior
        self.y_velocity = -10
        self.set_animation("jump")

    def jump_left(self):
        # Placeholder for jumping left behavior
        self.x_velocity = -5
        self.y_velocity = -10
        self.set_animation("jump_direction")
        self.image = pygame.transform.flip(self.jumping_facing_frames[self.current_frame], True, False)
        self.rect = self.image.get_rect(center=self.rect.center)

    def jump_right(self):
        # Placeholder for jumping right behavior
        self.x_velocity = 5
        self.y_velocity = -10
        self.set_animation("jump_direction")

    def sprint_left(self):
        # Placeholder for sprinting left behavior
        self.x_velocity = -10
        self.set_animation("sprint")
        self.image = pygame.transform.flip(self.sprinting_frames[self.current_frame], True, False)
        self.rect = self.image.get_rect(center=self.rect.center)  # Update rect position

    def sprint_right(self):   
        self.x_velocity = 10
        self.set_animation("sprint")

    def handle_movement(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

    def update(self):
        tiles = []  # Ensure tiles is defined
        self.handle_input()
        self.handle_gravity()
        self.handle_movement()
        self.handle_collisions(tiles)
        self.update_animation()  # Update animation frame based on the current animation
