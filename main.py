import pygame
import sys
from Scripts.game import GameState
from Scripts.player import Player
from Scripts.player import Player, ShieldType

# In game loop:
keys = pygame.key.get_pressed()
if keys[pygame.K_q]:
    Player.activate_shield(ShieldType.ACTIVE)
if keys[pygame.K_e]:
    Player.activate_shield(ShieldType.PASSIVE)

Player.update_shield()
Player.update()
Player.draw_shield_bar(screen) # type: ignore

#Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60

#Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize Player
player = Player()
pygame.display.set_caption("Feraz")
clock = pygame.time.Clock()
game = GameState(screen)

#Main Function, game loop calling the main class, update, and draw functions
def main():
    running = True
    #Handle Events
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update_logic()
        game.update_graphics()
        Player.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()   
    sys.exit()
player.update_shield()
player.update()
player.draw_shield_bar(screen)

weapon = weapon() # type: ignore

# Input check (in event loop or key press check)
keys = pygame.key.get_pressed()
if keys[pygame.K_q]:
    weapon.activate_shield(ShieldType.ACTIVE)
if keys[pygame.K_e]:
    weapon.activate_shield(ShieldType.PASSIVE)

# Update
weapon.update()

# Draw ability bar
weapon.draw_ability_bar(screen)

# Define enemy object
from Scripts.enemy import Enemy  # Ensure the Enemy class is imported

enemy = Enemy()  # Initialize the enemy object correctly

# Handle contact
result = weapon.handle_contact(enemy)  # where enemy is an object with take_damage()
if result == "damaged":
    print("Enemy hit!")
elif result == "phased":
    print("Player phased through enemy.")
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    
    player.handle_mouse_input(event)  # Handle left-click shield activation

    
if __name__ == "__main__":
    main()
