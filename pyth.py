import time
import colorama
from colorama import *

colorama.init(autoreset=True)

def answer(number):
    print(f"You chose {number}")

while True:
    number = input("Choose a number between 1 and 10 and I will try to guess it (q to quit)>>> ")

    print("Guessing... ", end="", flush=True)
    time.sleep(3)

    if number in map(str, range(1, 11)):
        answer(number)
    elif number == "q":
        break
    else:
        print("Invalid input")
