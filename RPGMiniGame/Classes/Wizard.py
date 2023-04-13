import random
import Classes.Character as CH

class Wizard(CH.Character):
    def attack_fireball(self, targetPlayer):
        super().attack(targetPlayer, 40, 40, 60, "a fireball")

    def attack_energy_wave(self, targetPlayer):
        super().attack(targetPlayer, 90, 10, 15, "an energy wave")

    def __init__(self, stregth, controlBy):
        super().__init__(stregth, controlBy)
    
    def display_action_list(self):
        print("1. (40%/40 - 60 HP) Attack with a fireball")
        print("2. (90%/10 - 15 HP) Attack with an energy wave")

        super().display_action_list()

    def execute_action(self, res, target):
        if(res == 1):
            self.attack_fireball(target)
        elif(res == 2):
            self.attack_energy_wave(target)
        else:
            super().execute_action(res, target)