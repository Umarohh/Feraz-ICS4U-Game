import pygame
from main import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.camera = pygame.Rect(0, 0, self.width, self.height)
        self.camera_pos = pygame.Vector2(0, 0)


    def apply(self, entity):
        """Moves the entity's rect to the correct position relative to the camera"""
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """Update the camera position to follow the target (e.g., player) with smoothness"""
        target_rect = target.rect
        x = -target_rect.centerx + int(self.width / 2)
        y = -target_rect.centery + int(self.height / 2)

        # Keep the camera within level bounds
        x = min(0, x)  # Don't let camera move left
        y = min(0, y)  # Don't let camera move up

        # Prevent camera from scrolling past the right/bottom of the level
        x = max(-(self.width - target.rect.width), x)
        y = max(-(self.height - target.rect.height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)

        # Smooth the camera movement (ease the transition)
        self.camera_pos.x += (self.camera.x - self.camera_pos.x) * 0.1
        self.camera_pos.y += (self.camera.y - self.camera_pos.y) * 0.1

        self.camera.topleft = self.camera_pos.x, self.camera_pos.y

