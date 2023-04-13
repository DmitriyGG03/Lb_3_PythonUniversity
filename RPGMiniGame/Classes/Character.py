import random

class Character:

    def __init__(self, strength, controlBy):
        self.__controlBy = controlBy
        self.__health = 100    
        self.__strength = strength       

    @property
    def controlBy(self):
        return self.__controlBy

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        if 1 <= strength <= 100:
            self.__strength = strength
        else:            
            raise Exception("Strength must be beatween 1 and 100")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health > 100:
            self.__health = 100
        elif health < 0:
            self.__health = 0
        else:
            self.__health = health

    def attack(self, targetPlayer, winValue, minDamage, maxDamage, str):
        if (random.randint(1, 100) <= winValue):
            damage = (self.strength / 100) * random.randint(minDamage,maxDamage)
            targetPlayer.health -= damage
            print(f"{self.controlBy} attacked {targetPlayer.controlBy} with {str} and dealt {damage} damage")            
        else: 
            print(f"{self.controlBy} missed")

    def attack_foot(self, targetPlayer):
        self.attack(targetPlayer, 50, 20, 30, "a foot")

    def heal(self):
        health = random.randint(10, 30)
        self.health += health
        print(f"{self.controlBy} recovered {health} health")

    def display_action_list(self):
        print("3. (50%/20 - 30 HP) Kick with the foot")
        print("4. (Add 10 - 30 HP) Heal yourself")

    def execute_action(self, res, targerPlayer):
        if(res == 3):
            return self.attack_foot(targerPlayer)
        elif(res == 4):
            return self.heal()










