import time
import colorama
from colorama import *


while True:
    # Prompt the user to enter a number between 1 and 10 or 'q' to quit
    number = input(Fore.GREEN + "Choose a number between 1 and 10 and I will try to guess it (q to quit)>>> ")

    # Print "Guessing..." and wait for 3 seconds
    print(Fore.GREEN + "Guessing... ", end="", flush=True)
    time.sleep(3)

    # Define the answer function to print the chosen number
    def answer():
        print(Fore.GREEN + f"You chose {number}")

    # Check the user's input and call the answer function if valid
    if number == "1":
        answer()
    elif number == "2":
        answer()
    elif number == "3":
        answer()
    elif number == "4":
        answer()
    elif number == "5":
        answer()
    elif number == "6":
        answer()
    elif number == "7":
        answer()
    elif number == "8":
        answer()
    elif number == "9":
        answer()
    elif number == "10":
        answer()
    elif number == "q":
        # Exit the loop and end the program
        break
    else:
        # Print an error message for invalid input
        print(Fore.RED + "Invalid input")
