import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = random.randint(10,30)
    

    def strike(self):
         return random.randint(1, self.attack_power)
    
    def receive_damage(self, damage):
        if (self.health > 0) and (self.health - damage > -1):
            protection = random.randint(0,50)
            if protection >= 45:
                self.health -= (damage * 0.5)
            else:
                self.health -= damage
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0