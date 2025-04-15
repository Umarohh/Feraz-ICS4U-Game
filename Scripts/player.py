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
# Shield System
        self.shield_type = None
        self.shield_active = False
        self.shield_duration = 3  # seconds
        self.shield_cooldown = 5  # seconds
        self.shield_last_activated = 0
        self.shield_start_time = 0
        self.shield_end_time = 0

            
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
def activate_shield(self, shield_type):
    current_time = time.time()
    if current_time - self.shield_last_activated < self.shield_cooldown:
        return False  # Cooldown not finished

    self.shield_type = shield_type
    self.shield_active = True
    self.shield_start_time = current_time
    self.shield_end_time = current_time + self.shield_duration
    self.shield_last_activated = current_time
    return True

def update_shield(self):
    if self.shield_active and time.time() > self.shield_end_time:
        self.shield_active = False
        self.shield_type = None

def is_attack_active(self):
    return self.shield_active and self.shield_type == ShieldType.ACTIVE

def is_phase_active(self):
    return self.shield_active and self.shield_type == ShieldType.PASSIVE

def handle_contact(self, target):
    if self.is_attack_active():
        if hasattr(target, 'take_damage'):
            target.take_damage()
        return "damaged"
    elif self.is_phase_active():
        return "phased"
    return "normal"
    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.jump_left()
            if keys[pygame.K_LSHIFT]:
                self.sprint_left()
            else:
                 self.walk_left()
    
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                self.jump_right()
            
            else:
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
    
    def handle_mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            self.activate_shield(ShieldType.PASSIVE)

    def draw_shield_bar(self, surface):
        bar_width = 120
        bar_height = 10
        x, y = 20, surface.get_height() - 30

        pygame.draw.rect(surface, (50, 50, 50), (x, y, bar_width, bar_height))

        current_time = time.time()
        if self.shield_active:
            remaining = self.shield_end_time - current_time
            percent = max(0, min(1, remaining / self.shield_duration))
            color = (0, 200, 255) if self.shield_type == ShieldType.ACTIVE else (200, 100, 255)
            pygame.draw.rect(surface, color, (x, y, int(bar_width * percent), bar_height))
        else:
            cooldown_remaining = self.shield_cooldown - (current_time - self.shield_last_activated)
            if cooldown_remaining > 0:
                percent = max(0, min(1, cooldown_remaining / self.shield_cooldown))
                pygame.draw.rect(surface, (100, 100, 100), (x, y, int(bar_width * percent), bar_height))


    def update(self):
        tiles = []  # Ensure tiles is defined
        self.handle_input()
        self.handle_gravity()
        self.handle_movement()
        self.handle_collisions(tiles)
        self.update_animation()  # Update animation frame based on the current animation
