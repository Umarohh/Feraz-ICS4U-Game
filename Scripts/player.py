import pygame
import os
from Scripts.physics import PhysicsObject
import time

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
        self.sprint = False  # Initialize sprint variable
        self.jump_force = 10
        self.jump_hold_time = 10       # How long the jump can be held
        self.jump_active = False       # Is the jump being held?
        self.jump_timer = 0            # Countdown timer
        self.max_jumps = 2             # Total jumps (1 normal + 1 double)
        self.jumps_left = self.max_jumps
        self.is_on_ground = False
        self.x_velocity = 0
        self.y_velocity = 0
        self.is_on_ground = True
        self.idle()  # You start as idle
            
    def load_animation(self, folder_path):
        """Loads all image frames from the given folder path"""
        frames = []
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith(".png"):
                path = os.path.join(folder_path, filename)
                image = pygame.image.load(path).convert_alpha()
                frames.append(image)
        return frames

    def load_images(self):
        """Load all animations from their respective folders"""
        self.idle_frames = self.load_animation("assets/player/idle")
        self.walking_frames = self.load_animation("assets/player/walking")
        self.running_frames = self.load_animation("assets/player/running")
        self.sprinting_frames = self.load_animation("assets/player/sprinting")
        self.jumping_frames = self.load_animation("assets/player/jumping")
        self.jumping_facing_frames = self.load_animation("assets/player/jumping_facing")
        self.falling_frames = self.load_animation("assets/player/falling")
        self.falling_facing_frames = self.load_animation("assets/player/falling_facing")

        self.animations = {
            "idle": self.idle_frames,
            "walk": self.walking_frames,
            "run": self.running_frames,
            "sprint": self.sprinting_frames,
            "jump": self.jumping_frames,
            "jump_direction": self.jumping_facing_frames,
            "fall": self.falling_frames,
            "fall_direction": self.falling_facing_frames,
        }
        
    def set_animation(self, name):
        """Switch to a new animation"""
        if name != self.current_animation:
            self.current_animation = name
            self.current_frame = 0
            self.frame_timer = 0
            self.image = self.animations[name][self.current_frame]

        # Get the current frame of the animation
        frame = self.animations[name][self.current_frame]

        # Flip image if moving left (negative x_velocity)
        if self.x_velocity < 0:
            self.image = pygame.transform.flip(frame, True, False)
        else:
            self.image = frame

        # Update the player's rect (position) based on the new image
        self.rect = self.image.get_rect(center=self.rect.center)

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
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
            if not self.jump_active and self.jumps_left > 0:
                self.start_jump()
        # Hold jump (variable height)
        if self.jump_active and (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
            self.continue_jump()
        else:
            self.jump_active = False
        if keys[pygame.K_LSHIFT]:
            self.sprint = True
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
        if self.sprint == True:
            max_speed = -10
            acceleration = -1
        else:      
            max_speed = -5
            acceleration = -0.5
        if self.x_velocity > max_speed:
            self.x_velocity += acceleration

    def move_right(self):
        if self.sprint == True:
            max_speed = 10
            acceleration = 1
        else:      
            max_speed = 5
            acceleration = 0.5
        if self.x_velocity < max_speed:
            self.x_velocity += acceleration

 
    def start_jump(self):
        self.jump_active = True
        self.jump_timer = self.jump_hold_time
        self.y_velocity = -self.jump_force
        self.jumps_left -= 1
        self.set_animation("jump")

    def continue_jump(self):
        if self.jump_timer > 0:
            self.y_velocity = -self.jump_force
            self.jump_timer -= 1
        else:
            self.jump_active = False

    def handle_movement(self):
        self.rect.y += self.x_velocity
        self.rect.x += self.y_velocity

    def choose_movement_animations(self):
        if self.y_velocity < 0:  # Going up (jumping)
            if self.x_velocity != 0:
                self.set_animation("jump_direction")
            else:
                self.set_animation("jump")
        elif self.y_velocity > 0:  # Going down (falling)
            if self.x_velocity != 0:
                self.set_animation("fall_direction")
            else:
                    self.set_animation("fall")
        else:  # On ground
            if self.x_velocity == 0:
                self.set_animation("idle")
            elif self.x_velocity < 2.5:
                self.set_animation("walk")
            elif self.x_velocity < 5:
                self.set_animation("run")
            elif self.x_velocity < 10:
                self.set_animation("sprint")        

    def render(self, screen):
        """Render the player sprite to the screen"""
        screen.blit(self.image, self.rect)  # Draw the player at its current position

    def update(self):
        tiles = []  # Ensure tiles is defined
        self.handle_input()
        self.handle_gravity()
        self.handle_movement()
        self.handle_collisions(tiles)
        self.choose_movement_animations()
        self.update_animation()  # Update animation frame based on the current animation

