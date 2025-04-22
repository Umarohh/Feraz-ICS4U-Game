import pygame
import os
# from main import SCREEN_HEIGHT  # Removed as it is not accessed
from Scripts.physics import PhysicsObject
import time

class ShieldType:
    ACTIVE = 'active'
    PASSIVE = 'passive'


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
        self.idle_frames = self.load_animation("assets/player", "idle", 1)
        self.walking_frames = self.load_animation("assets/player", "running", 1)
        self.running_frames = self.load_animation("assets/player", "running", 1)
        self.sprinting_frames = self.load_animation("assets/player", "running", 1)
        self.jumping_frames = self.load_animation("assets/player", "jumping", 1)  # 1 frame for jumping
        self.jumping_facing_frames = self.load_animation("assets/player", "jumping_facing", 1)  # 1 frame for jumping facing
        self.falling_frames = self.load_animation("assets/player", "falling", 1)  # 1 frame for falling
        # Store all animations in a dictionary

        self.animations = {
            "idle": self.idle_frames,
            "walk": self.walking_frames,
            "run": self.running_frames,
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

    def handle_input(self, event):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]: 
            self.move_right()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE] and not self.jump_active and self.is_on_ground == True:
            self.jump()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE] and self.maximum_jumps > 0 and self.is_on_ground == False:
            self.double_jump()
        if keys[pygame.K_LSHIFT]:
            sprint = True
        else:
            self.idle()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    
    def idle(self):
            # Smooth deceleration
        if self.x_velocity > 0:
            self.x_velocity -= 1
        elif self.x_velocity < 0:
            self.velocity_x += 1
        else:
            self.x_velocity = 0
          
    def move_left(self):
        # Walking Left Logic
        if sprint == True:
            max_speed = -10
            acceleration = -1
        else:      
            max_speed = -5
            acceleration = -0.5
        if self.x_velocity > max_speed:
            self.x_velocity += acceleration

    def move_right(self):
     if sprint == True:
            max_speed = 10
            acceleration = 1
        else:      
            max_speed = 5
            acceleration = 0.5
        if self.x_velocity < max_speed:
            self.x_velocity += acceleration

 
    def jump(self):
        if not self.jump_active and self.jumps_left > 0:
            self.jump_active = True
            self.jump_hold_time = 0
            self.jumps_left -= 1
            self.y_velocity = -self.jump_force
            self.set_animation("jump")

    def handle_movement(self):
        self.rect.y += self.x_velocity
        self.rect.x += self.y_velocity

    def choose_movement_animations(self):
        pass

    def update(self):
        tiles = []  # Ensure tiles is defined
        self.handle_input()
        self.handle_gravity()
        self.handle_movement()
        self.handle_collisions(tiles)
        self.choose_movement_animations
        self.update_animation()  # Update animation frame based on the current animation

