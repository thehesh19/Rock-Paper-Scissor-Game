from os import system
from random import randint
from sys import exit


class rockpaperscissors:
    def __init__(me):
        me.choices = "rock", "paper", "scissors"
        me.winplayer = 0
        me.wincomputer = 0
    def spacesize(me, length=50):
        return '-' * length
    def move(me):
        while True:
            try:
                option = int(input('Choose an option between Rock (1), Paper (2), Scissors (3): '))
                if 1 <= option <= 3:
                    break
                else:
                    print('You can only enter a number between 1 and 3.')    
            except ValueError:
                print('The value entered is invalid. You can only enter numeric values.')
        return option
    def move2(me):
        return randint(1,3)
    def winnercheck(me):
        if me.winplayer == me.wincomputer:
            return 'Tie.'
        elif me.winplayer > me.wincomputer:
            return 'You won the set.'
        else:
            return 'Computer wins the set.'
    def _play(me):
        times = int(input("How many times would you like to play?: "))
        for i in range(times):
            player = me.move()
            computer = me.move2()
            print(f"You chose {me.choices[player-1]}.")
            print(f"The computer chose {me.choices[computer-1]}.")
            if player == computer:
                print('Tie.\n')
                print(me.spacesize(), '\n')
            elif (player-computer) % 3 == 1:
                print('You won.\n')
                print(me.spacesize(), '\n')
                me.winplayer += 1
            else:
                print('You lost.\n')
                print(me.spacesize(), '\n')
                me.wincomputer += 1
        print(me.winnercheck())
        input("To return to the main menu, press a key.")
        system("CLS")
        me.main()

    def main(me, length=100):
        while True:
            try:
                print('-' * length, '\n')
                print('''
                █▀█ █▀█ █▀▀ █▄▀ ░   █▀█ ▄▀█ █▀█ █▀▀ █▀█ ░   █▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
                █▀▄ █▄█ █▄▄ █░█ █   █▀▀ █▀█ █▀▀ ██▄ █▀▄ █   ▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█                                                   
                '''.center(10))
                print('-' * length, '\n')
                print('1. Play'.center(length))
                print('2. Instructions'.center(length))
                print('3. Exit'.center(length))
                choice = int(input('\nEnter an option: '))
            except ValueError:
                print('The value entered is incorrect. Only numbers can be entered.')

            if choice == 1:
                system("CLS")
                me._play()
                break
            elif choice == 2:
                system("CLS")
                print("  Instructions for Rock, Paper, Scissors: ")
                print("- Rock wins over scissors (because rock smashes scissors).")
                print("- Scissors wins over paper (because scissors cut paper).")
                print("- Paper wins over rock (because paper covers rock).")
                print("- If both players show the same sign, it's a tie.\n")
                input("Press a key to return to the main menu...")
                system("CLS")
            elif choice == 3:
                exit()
            else:
                print("You have entered a number that isn't in the list.")
                system("CLS")
            
if __name__ == '__main__':
    game = rockpaperscissors()
    game.main()