import random

def roll_dice():
    print("Rolling the dice...")
    dice_number = random.randint(1, 6)

    
    if dice_number == 1:
        print("---------")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print("---------")
    elif dice_number == 2:
        print("---------")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print("---------")
    elif dice_number == 3:
        print("---------")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print("---------")
    elif dice_number == 4:
        print("---------")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print("---------")
    elif dice_number == 5:
        print("---------")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print("---------")
    elif dice_number == 6:
        print("---------")
        print("| •   • |")
        print("| •   • |")
        print("| •   • |")
        print("---------")

    return dice_number

def main():
    response = "y"

    while response.lower() == "y":
        dice_result = roll_dice()
        response = input("Do you want to roll the dice again? (y/n): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()