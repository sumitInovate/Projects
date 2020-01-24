import random


def main():
    roll_again="yes"
    while roll_again=="yes" or roll_again=="y" or roll_again=="Yes" or roll_again=="Y":
        dice1=0
        dice2=0
   
        dice1=dice_roll()
        dice2=dice_roll()
        roll_again= input("\nRoll the dice again? (y/n)")
        
def dice_roll():
    diceRoll=random.randint(1, 6)
    if diceRoll==1:
        print("----------")
        print("|        |")
        print("|   o    |")
        print("|        |")
        print("----------")
    if diceRoll==2:
        print("----------")
        print("|        |")
        print("| o   o  |")
        print("|        |")
        print("----------")
    if diceRoll==3:
        print("----------")
        print("|     o  |")
        print("|   o    |")
        print("| o      |")
        print("----------")
    if diceRoll==4:
        print("----------")
        print("| o   o  |")
        print("|        |")
        print("| o   o  |")
        print("----------")
    if diceRoll==5:
        print("----------")
        print("| o   o  |")
        print("|   o    |")
        print("| o   o  |")
        print("----------")
    if diceRoll==6:
        print("----------")
        print("| o   o  |")
        print("| o   o  |")
        print("| o   o  |")
        print("----------")
        
    return diceRoll


main()
