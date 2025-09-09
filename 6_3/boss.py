import random
from enemy import Enemy

class Dragon(Enemy):
    def wing_slap(self, power):
        self.attack_power = power
    
    def boss_health(self, health):
        self.health = health
    
    def fire_hit(self):
        self.attack_power = random.randint[20,100]

    def weak_point(self, spot):
        if spot == "ankle":
            self.health = 0
        