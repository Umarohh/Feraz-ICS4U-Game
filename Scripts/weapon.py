class Weapon:
    def __init__(self, name, damage, range, attack_speed, ammo_capacity):
        self.name = name  # Weapon name (e.g., "Pistol", "Rifle")
        self.damage = damage  # Damage dealt by the weapon
        self.range = range  # Range of the weapon (e.g., how far a projectile travels)
        self.attack_speed = attack_speed  # Speed at which attacks can be fired (attacks per second)
        self.ammo_capacity = ammo_capacity  # Maximum ammo capacity of the weapon
        self.current_ammo = ammo_capacity  # Current ammo in the weapon (starts full)

    def attack(self):
        """
        Simulates the attack behavior of the weapon. 
        This method should be called when the player fires the weapon.
        """
        if self.current_ammo > 0:
            self.current_ammo -= 1
            print(f"{self.name} fired! Damage: {self.damage}, Ammo left: {self.current_ammo}")
        else:
            print(f"{self.name} is out of ammo!")
    
    def reload(self):
        """
        Simulates reloading the weapon.
        """
        self.current_ammo = self.ammo_capacity
        print(f"{self.name} reloaded! Ammo: {self.current_ammo}")

    def is_out_of_ammo(self):
        """
        Returns whether the weapon is out of ammo.
        """
        return self.current_ammo <= 0


# Define different weapons
class Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Pistol", damage=10, range=100, attack_speed=1.5, ammo_capacity=12)


class Shotgun(Weapon):
    def __init__(self):
        super().__init__(name="Shotgun", damage=30, range=50, attack_speed=0.8, ammo_capacity=6)


class Rifle(Weapon):
    def __init__(self):
        super().__init__(name="Rifle", damage=20, range=150, attack_speed=2.0, ammo_capacity=30)


class RocketLauncher(Weapon):
    def __init__(self):
        super().__init__(name="Rocket Launcher", damage=100, range=200, attack_speed=0.5, ammo_capacity=4)


class LaserGun(Weapon):
    def __init__(self):
        super().__init__(name="Laser Gun", damage=15, range=200, attack_speed=3.0, ammo_capacity=50)


# Example usage:
if __name__ == "__main__":
    # Create a list of weapons
    weapons = [Pistol(), Shotgun(), Rifle(), RocketLauncher(), LaserGun()]

    # Simulate using the weapons
    for weapon in weapons:
        print(f"\nUsing {weapon.name}...")
        weapon.attack()  # Fire the weapon
        weapon.attack()  # Fire again
        print(f"Is out of ammo? {weapon.is_out_of_ammo()}")  # Check if out of ammo
        weapon.reload()  # Reload
        weapon.attack()  # Fire after reloading
        print(f"Is out of ammo? {weapon.is_out_of_ammo()}")
        # Fire until out of ammo
        while not weapon.is_out_of_ammo():
            weapon.attack()
        print(f"Is out of ammo? {weapon.is_out_of_ammo()}")
        weapon.reload()
        print(f"Is out of ammo? {weapon.is_out_of_ammo()}")
        print(f"Ammo after reloading: {weapon.current_ammo}")
        print("-" * 30)
        # End of weapon usage simulation
        print(f"Finished using {weapon.name}.")