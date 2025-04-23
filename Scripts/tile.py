import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.x = x
        self.y = y
        self.tile_type = tile_type
        
        # Load textures for different tile types
        if self.tile_type == 1:  # Ground tile
            self.image = pygame.image.load('ground_tile.png')  # Load ground texture
        elif self.tile_type == 2:  # placeholder tile
            self.image = pygame.image.load('platform_tile.png')  # Load platform texture
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * 32, self.y * 32)  # Position tile on the screen

    def update(self):
        # You can add tile-specific behavior here, like animation or interactions
        pass

class Tilemap:
    def __init__(self, map_data):
        self.map_data = map_data  # The 2D array of tile types
        self.tiles = pygame.sprite.Group()  # This will hold all tile sprites
        
        # Create tiles for the tilemap
        self.create_tiles()

    def create_tiles(self):
        '''I lowkey have no idea how this code works'''
        for y, row in enumerate(self.map_data):
            for x, tile_type in enumerate(row):
                tile = Tile(x, y, tile_type)  
                self.tiles.add(tile) 

    def render(self, screen):
        # Render all tiles
        self.tiles.draw(screen)

    def update(self):
        # Update all tiles (if any tile-specific behavior is needed)
        self.tiles.update()