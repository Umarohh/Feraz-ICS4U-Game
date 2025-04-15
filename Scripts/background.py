import pygame
import os

# Initialize pygame
pygame.init()

# Set up the game screen with new resolution
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer - Forest Level")

# Colors
WHITE = (255, 255, 255)

# Load background images for parallax scrolling
def load_background_images():
    bg_far = pygame.image.load(os.path.join("assets", "bg_far.png"))
    bg_mid = pygame.image.load(os.path.join("assets", "bg_mid.png"))
    bg_near = pygame.image.load(os.path.join("assets", "bg_near.png"))
    return bg_far, bg_mid, bg_near

# Set initial positions for scrolling
bg_pos_far = 0
bg_pos_mid = 0
bg_pos_near = 0

# Speed of parallax scrolling
parallax_speed_far = 0.2
parallax_speed_mid = 0.5
parallax_speed_near = 1

# Environmental effects (clouds)
class Cloud:
    def load_clouds():
        cloud1 = pygame.image.load(os.path.join("assets", "cloud1.png"))
        cloud2 = pygame.image.load(os.path.join("assets", "cloud2.png"))
        return [cloud1, cloud2]

    cloud_positions = [(100, 50), (400, 100)]

# Function to render background with parallax effect
def render_background(bg_far, bg_mid, bg_near):
    global bg_pos_far, bg_pos_mid, bg_pos_near

    # Far background (slowest scrolling)
    bg_pos_far -= parallax_speed_far
    if bg_pos_far <= -bg_far.get_width():
        bg_pos_far = 0
    screen.blit(bg_far, (bg_pos_far, 0))
    screen.blit(bg_far, (bg_pos_far + bg_far.get_width(), 0))

    # Middle background (medium scrolling)
    bg_pos_mid -= parallax_speed_mid
    if bg_pos_mid <= -bg_mid.get_width():
        bg_pos_mid = 0
    screen.blit(bg_mid, (bg_pos_mid, 0))
    screen.blit(bg_mid, (bg_pos_mid + bg_mid.get_width(), 0))

    # Near background (fastest scrolling)
    bg_pos_near -= parallax_speed_near
    if bg_pos_near <= -bg_near.get_width():
        bg_pos_near = 0
    screen.blit(bg_near, (bg_pos_near, 0))
    screen.blit(bg_near, (bg_pos_near + bg_near.get_width(), 0))

    # Render clouds with simple parallax effect
    for i, cloud in enumerate(clouds):
        cloud_x, cloud_y = cloud_positions[i]
        cloud_x -= parallax_speed_far  # Clouds move slower than the near background
        if cloud_x < -cloud.get_width():
            cloud_x = WIDTH
        cloud_positions[i] = (cloud_x, cloud_y)
        screen.blit(cloud, (cloud_x, cloud_y))
