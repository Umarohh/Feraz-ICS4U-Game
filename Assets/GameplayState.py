from Scripts.game import GameState
from Scripts.player import Player
from Scripts.enemy import Enemy

class GameplayState(GameState):
    def __init__(self, screen):
        super().__init__(screen)
        self.player = Player()
        self.enemy = Enemy()

    def update_logic(self):
        self.player.update()
        self.enemy.update()

    def update_graphics(self, surface):
        surface.fill((20, 20, 20))  # Optional: clear screen
        self.player.draw(surface)
        self.enemy.draw(surface)

    def handle_event(self, event):
        self.player.handle_input(event)
