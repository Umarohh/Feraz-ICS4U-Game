import sys
import time
import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

# Game States
MAIN_MENU = "main_menu"
GAMEPLAY = "gameplay"
PAUSE_MENU = "pause_menu"

# Button class
class Button:
    def __init__(self, x, y, width, height, text, font, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.callback = callback
        self.bg_color = (100, 100, 100)
        self.text_color = (255, 255, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

# GameStateManager class
class GameStateManager:
    def __init__(self, screen):
        self.screen = screen
        self.state = MAIN_MENU  # Start with the main menu
        self.states = {
            MAIN_MENU: MainMenu(self),
            GAMEPLAY: GamePlay(self),
            PAUSE_MENU: PauseMenu(self)
        }

    def change_state(self, new_state):
        self.state = new_state
        self.states[self.state].reset()

    def update(self):
        self.states[self.state].update()

    def draw(self):
        self.states[self.state].draw(self.screen)

# Base State Class (all other states will inherit from this)
class GameStateBase:
    def __init__(self, manager):
        self.manager = manager

    def update(self):
        raise NotImplementedError

    def draw(self, surface):
        raise NotImplementedError

    def reset(self):
        pass

# Main Menu State
class MainMenu(GameStateBase):
    def __init__(self, manager):
        super().__init__(manager)
        self.font = pygame.font.SysFont("Arial", 50)
        self.buttons = []
        self.add_button("Start Game", self.start_game)
        self.add_button("Quit", self.quit_game)

    def add_button(self, text, callback):
        button_width = 300
        button_height = 60
        x = (SCREEN_WIDTH - button_width) // 2
        y = SCREEN_HEIGHT // 3 + len(self.buttons) * (button_height + 20)
        button = Button(x, y, button_width, button_height, text, self.font, callback)
        self.buttons.append(button)

    def start_game(self):
        self.manager.change_state(GAMEPLAY)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            for button in self.buttons:
                button.handle_event(event)

    def draw(self, surface):
        surface.fill((50, 50, 50))
        for button in self.buttons:
            button.draw(surface)

# Gameplay State
class GamePlay(GameStateBase):
    def __init__(self, manager):
        super().__init__(manager)
        self.player = Player()
        self.enemy = Enemy()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.change_state(MAIN_MENU)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:  # Pause on 'P'
                self.manager.change_state(PAUSE_MENU)

        # Add gameplay logic (e.g., player movement, collisions)
        self.player.update()
        self.enemy.update()

    def draw(self, surface):
        surface.fill((0, 0, 0))  # Clear screen with black
        self.player.draw(surface)
        self.enemy.draw(surface)

    def reset(self):
        self.player = Player()  # Reset player and enemy if needed

# Pause Menu State
class PauseMenu(GameStateBase):
    def __init__(self, manager):
        super().__init__(manager)
        self.font = pygame.font.SysFont("Arial", 50)
        self.buttons = []
        self.add_button("Resume", self.resume_game)
        self.add_button("Quit to Main Menu", self.quit_to_main_menu)

    def add_button(self, text, callback):
        button_width = 300
        button_height = 60
        x = (SCREEN_WIDTH - button_width) // 2
        y = SCREEN_HEIGHT // 3 + len(self.buttons) * (button_height + 20)
        button = Button(x, y, button_width, button_height, text, self.font, callback)
        self.buttons.append(button)

    def resume_game(self):
        self.manager.change_state(GAMEPLAY)

    def quit_to_main_menu(self):
        self.manager.change_state(MAIN_MENU)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.manager.change_state(MAIN_MENU)

            for button in self.buttons:
                button.handle_event(event)

    def draw(self, surface):
        surface.fill((50, 50, 50))
        for button in self.buttons:
            button.draw(surface)

# ShieldType definition
class ShieldType:
    ACTIVE = "ACTIVE"
    PASSIVE = "PASSIVE"

# Player and Enemy classes (simplified for illustration)
class Player:
    def __init__(self):
        self.shield_type = ShieldType.PASSIVE
        self.shield_active = False
        self.shield_end_time = 0
        self.shield_duration = 5  # Example duration in seconds

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, 50))

    def draw_shield_bar(self, surface):
        bar_width = 120
        bar_height = 10
        x, y = 20, surface.get_height() - 30

        pygame.draw.rect(surface, (50, 50, 50), (x, y, bar_width, bar_height))
        color = (0, 200, 255) if self.shield_type == "ACTIVE" else (200, 100, 255)
        current_time = time.time()
        if self.shield_active:
            remaining = self.shield_end_time - current_time
            percent = max(0, min(1, remaining / self.shield_duration))
            pygame.draw.rect(surface, color, (x, y, int(bar_width * percent), bar_height))
        else:
            cooldown_remaining = 5 - (current_time - self.shield_end_time)
            if cooldown_remaining > 0:
                percent = max(0, min(1, cooldown_remaining / 5))
                pygame.draw.rect(surface, (100, 100, 100), (x, y, int(bar_width * percent), bar_height))

class Enemy:
    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2, 50, 50))

# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Feraz")
    clock = pygame.time.Clock()

    game_manager = GameStateManager(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass events to the current game state
            game_manager.states[game_manager.state].handle_event(event)

        game_manager.update()
        game_manager.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
