import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        self.image.fill((200, 50, 50))  # Changed color for distinction
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.hitbox = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 30, 30)
        self.health = 5  # Increased health for variation
        self.is_active = True
        self.attack_timer = 0
        self.movement_speed = 3  # Adjusted speed
        self.start_position = (x, y)
        self.direction = pygame.math.Vector2(0, 0)
        self.knockback = False
        self.knockback_duration = 0
        self.respawn_time = 90  # Increased respawn delay

    def update(self, player):
        self.hitbox.topleft = (self.rect.x + 5, self.rect.y + 5)
        
        if self.hitbox.colliderect(player.rect) and self.is_active:
            self.receive_damage()

        if self.knockback:
            self.knockback_duration += 1
            if self.knockback_duration >= self.respawn_time:
                self.reset_enemy()
        else:
            self.follow_player(player)

    def follow_player(self, player):
        """Move towards the player in a straight line."""
        target = pygame.math.Vector2(player.rect.center)
        current = pygame.math.Vector2(self.rect.center)
        movement = target - current
        if movement.length() > 0:
            movement = movement.normalize() * self.movement_speed
        self.direction = movement
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y

    def receive_damage(self):
        """Reduce health and handle knockback."""
        if self.health > 0:
            self.health -= 1
            print(f"Enemy damaged! Health left: {self.health}")
            self.activate_knockback()
        
        if self.health <= 0:
            self.knockback = True
            print("Enemy defeated!")

    def activate_knockback(self):
        """Temporarily disable the enemy."""
        self.knockback = True
        self.direction = pygame.math.Vector2(0, 0)
        print("Enemy knocked back!")

    def reset_enemy(self):
        """Reset the enemy to its starting position and state."""
        self.rect.topleft = self.start_position
        self.health = 5
        self.knockback = False
        self.knockback_duration = 0
        print("Enemy reset and ready!")

    def attack(self):
        """Simulate an attack."""
        if self.is_active:
            print("Enemy attacks!")
            # Add attack logic or animations here
        else:
            print("Enemy is not active and cannot attack.") 
            