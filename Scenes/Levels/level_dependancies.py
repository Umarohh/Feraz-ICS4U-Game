import pygame

class Level:
    def __init__(self, screen, camera_x):
        """Initialize the parent level class"""
        self.screen = screen
        self.completed = False  # Track if the level is completed
        self.camera_x = camera_x
        self.bg_layer_1 = None
        self.bg_layer_2 = None
        self.bg_layer_3 = None
        self.bg_layer_4 = None
        self.bg_layer_5 = None


        self.bg_layer_1_speed = 0.1
        self.bg_layer_2_speed = 0.3
        self.bg_layer_3_speed = 0.5
        self.bg_layer_4_speed = 0.7
        self.bg_layer_5_speed = 1.1


    def check_completion_condition(self): # Ensures all levels have a completion condition regardless of specific update method
        pass 
       
    def is_completed(self):
        """Return whether the level is completed to outside classes such as level_manager"""
        return self.completed
    
    def update(self):   
        """Ensures all levels update regardless of specific update method"""
        pass

    def draw(self): 
        """Ensures all levels render regardless of specific update method"""
        pass

    def load_backgrounds(self, bg_layer_1_path, bg_layer_2_path, bg_layer_3_path, bg_layer_4_path, bg_layer_5_path):
        """Load background images for all layers"""
        self.bg_layer_1 = pygame.image.load(bg_layer_1_path).convert()
        self.bg_layer_2 = pygame.image.load(bg_layer_2_path).convert()
        self.bg_layer_3 = pygame.image.load(bg_layer_3_path).convert()
        self.bg_layer_4 = pygame.image.load(bg_layer_4_path).convert()
        self.bg_layer_5 = pygame.image.load(bg_layer_5_path).convert()

    def render_parallax(self, screen, camera_x):
        """Render parallax layers based on the camera position"""
        screen.blit(self.bg_layer_1, (camera_x * self.bg_layer_1_speed, 0))
        screen.blit(self.bg_layer_2, (camera_x * self.bg_layer_2_speed, 0))
        screen.blit(self.bg_layer_3, (camera_x * self.bg_layer_3_speed, 0))
        screen.blit(self.bg_layer_4, (camera_x * self.bg_layer_4_speed, 0))
        screen.blit(self.bg_layer_5, (camera_x * self.bg_layer_5_speed, 0))
