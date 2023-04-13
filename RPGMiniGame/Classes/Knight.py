import random
import Classes.Character as CH

class Knight(CH.Character):
    def attack_sword(self, targetPlayer): 
        super().attack(targetPlayer, 60, 20, 40, "a sword")
        

    def attack_shield(self, targetPlayer):
        super().attack(targetPlayer, 75, 10, 20, "a shield")

    def __init__(self, stregth, controlBy):
        super().__init__(stregth, controlBy)

    def display_action_list(self):
        print("1. (60%/20 - 40 HP) Strike with a sword")
        print("2. (75%/10 - 20 HP) Strike with a shield")

        super().display_action_list()

    def execute_action(self, res, target):
        if(res == 1):
            self.attack_sword(target)
        elif(res == 2):
            self.attack_shield(target)
        else:
            super().execute_action(res, target)
 




