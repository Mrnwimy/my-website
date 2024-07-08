import random
import colorama
from colorama import Fore, Back, Style

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
while True:

    while player not in options:
        player = input(Fore.GREEN + "lets play rock paper scissors >>> ")


        print(f"You <{player}>")
        print(f"Enemy <{computer}>")

        if player == computer:
            print(Fore.YELLOW + "its a tie")
        elif player == "rock" and computer == "scissors":
            print(Fore.GREEN + "you win")
        elif player == "paper" and computer == "rock":
            print(Fore.GREEN + "you win")
        elif player == "scissors" and computer == "paper":
            print(Fore.GREEN + "you win")
        elif player not in options:
            print(Fore.RED + "invalid option")
            break



        else:
            print(Fore.RED + "you lost")