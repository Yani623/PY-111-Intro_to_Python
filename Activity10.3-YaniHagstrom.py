# Create a function that plays rock paper scissors with you:
#     - You are to ask the user for INPUT

import random

def rPScissors():
    userInput = int(input("Lets play Rock, Paper, Scissors. Choose 1 for Rock, 2 for Paper, or 3 for Scissors:")) #user input is an integer
    if userInput == 1:
        print("You chose Rock")
    elif userInput == 2:
        print("You chose Paper")
    elif userInput == 3:
        print("You chose Scissors")
    
    randNum = random.randrange(1,4)
    print(f"randNum = {randNum}")
    # print(type(randNum))
    if randNum == 1:
        print("You chose Rock")
    elif randNum == 2:
        print("You chose Paper")
    elif randNum == 3:
        print("You chose Scissors")

    if userInput == randNum:
        print("We tied")
    elif userInput == 1 and randNum == 2: #rock vs paper
        print("Paper eats Rock. Ha! I win!")
    elif userInput == 2 and randNum == 3: #paper vs scissors
        print("Scissors cut Paper. Ha! I win!")
    elif userInput == 3 and randNum == 1: #scissors vs rock
        print("Rock crushes Scissors. Ha! I win!")
    else:
        print("You beat me this time...")

rPScissors()

