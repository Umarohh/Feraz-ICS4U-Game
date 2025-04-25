import pygame

TILE_SIZE = 32  # Set a constant tile size

# You can preload tile images globally or through a function if you prefer
TILE_IMAGES = {
    1: pygame.image.load('placeholder.png').convert_alpha(),     # Ground tile
    2: pygame.image.load('placeholder2.png').convert_alpha(),    # Platform tile
    # Add more types as needed
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type):
        super().__init__()

        self.tile_type = tile_type
        self.image = TILE_IMAGES.get(tile_type)
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))

    def update(self):
        # Optional: Add animation, effects, or tile-specific logic
        pass

class Tilemap:
    def __init__(self, map_data):
        self.map_data = map_data
        self.tiles = pygame.sprite.Group()
        self.create_tiles()
    
    def _parse_file(self, file_path):
        """Read the file and return map data as a 2D array."""
        map_data = []
        with open(file_path, 'r') as file:
            for line in file:
                # Convert each line to a list of integers, where each represents a tile
                map_data.append([int(x) for x in line.strip().split()])
        return map_data

    def create_tiles(self, map_data):
        """Create tiles based on 2D map data."""
        for y, row in enumerate(map_data):
            for x, tile_type in enumerate(row):
                if tile_type != 0:  # Only create a tile if it is not empty (0)
                    tile = Tile(x, y, tile_type)  # Create a Tile instance
                    self.tiles.add(tile)  # Add the tile to the group

    def load_from_file(self, file_path):
        """Load the tilemap from a text file."""
        self.tiles.empty()  # Clear any existing tiles
        map_data = self._parse_file(file_path)
        self.create_tiles(map_data)  # Create tiles based on parsed data
        
    def update(self):
        """Update all tiles."""
        self.tiles.update()

    def render(self, screen):
        """Render the tilemap."""
        self.tiles.draw(screen)