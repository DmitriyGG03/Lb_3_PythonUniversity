from distutils.util import execute
import msvcrt
import os
import random
import sys
import Classes.Character as CH
import Classes.Knight as KN
import Classes.Wizard as WZ
from texttable import Texttable

class FightManager:

    def __init__(self, character1 : CH.Character, character2 : CH.Character):
        self.__fightRound = 0
        self.__character1 = character1
        self.__character2 = character2

    @property
    def fightRound(self):
        self.__fightRound += 1
        return self.__fightRound

    @property
    def character1(self):
        return self.__character1

    @character1.setter
    def character1(self, character1):
        self.__character1 = character1

    @property
    def character2(self):
        return self.__character2

    @character2.setter
    def character2(self, character2):
        self.__character2 = character2   
    
    def start_finghting(self):        
        while (True):
            os.system('cls')

            self.display_warriors_info_table()
            print(f"Current round of combat: {self.fightRound}\n")
            
            print(f"Choose the action you want to do:")
            self.__character1.display_action_list()

            res = input()

            print("\n")

            if (not res.isdigit()) or (not (1 <= int(res) <= 4)):
                print(f"Error. You must enter a number from 1 to 4")
                msvcrt.getch()
                self.__fightRound -= 1
                continue
            if (int(res) == 4 and self.character1.health == 100):
                print(f"You have full health")
                msvcrt.getch()
                self.__fightRound -= 1
                continue

            self.__character1.execute_action(int(res), self.__character2)

            if(self.check_character_win(self.character2)):
                self.win_event(self.character1.controlBy)  

            self.ai_logic()            

            if(self.check_character_win(self.character1)):
                self.win_event(self.character2.controlBy)

            print("\nPress any button to end the round")
            msvcrt.getch()

    def ai_logic(self):
        if (self.character2.health < 50 and random.randint(1, 100) <= 80):
            self.__character2.execute_action(4, self.__character1)
        else:
            self.__character2.execute_action(random.randint(1, 3), self.__character1)


        

            

    def check_character_win(self, character : CH.Character):
        return character.health == 0    
           

    def win_event(self, winnerName):
        print(f"{winnerName} won on the {self.fightRound - 1} round")

        print("\nPress any button to quit the game")
        msvcrt.getch()

        sys.exit()

            
    def display_warriors_info_table(self):
        
        table = Texttable()

        table.set_cols_dtype(['t', 't', 'i', 'i'])
        table.set_cols_valign(['m', 'm', 'm', 'm'])
        table.add_rows(
            [
                ["Character", "Character type", "Strength", "Health"],
                [self.character1.controlBy, "Knight" if isinstance(self.character1, KN.Knight) else "Wizard", self.character1.strength, self.character1.health],
                [self.character2.controlBy, "Knight" if isinstance(self.character2, KN.Knight) else "Wizard", self.character2.strength, self.character2.health]                
            ]
        )
        print(table.draw())


