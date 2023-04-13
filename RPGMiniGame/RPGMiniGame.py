import sys
import Classes.Character as CH
import Classes.FightManager as FM
import Classes.Knight as KN
import Classes.Wizard as WZ
import msvcrt
import os

def main():    
    fightManager = FM.FightManager(ChooseCharacter("your", "Player"), ChooseCharacter("oponent", "AI"))

    fightManager.start_finghting()

def ChooseCharacter(str, controlBy):
    while(True):        
        os.system('cls')

        res = input(f"Choose {str} character, knight(k) or wizard(w): ")

        if(res == "k" or res == "K"):
            return KN.Knight(EnterStregthForCharacter(), controlBy)
        elif (res == "w" or res == "W"):
            return WZ.Wizard(EnterStregthForCharacter(), controlBy)
        else: 
            print("Incorrect value. Try again")
            msvcrt.getch()

def EnterStregthForCharacter():
    while(True):        
        os.system('cls')

        res = int(input(f"Enter stregth for character (1 - 100): "))

        if(1 <= res <= 100):
            return res
        else: 
            print("Incorrect value. Try again")
            msvcrt.getch()

main()
    