'''Mini Activities:'''

#1: Create a function called sum that takes in NO parameters. Instead, ask the user for two numbers and add those two numbers and return their sum
# def sum():
#     userInput1 = int(input("Choose your first random number:"))
#     userInput2 = int(input("Choose your second random number:"))
#     return userInput1 + userInput2

# print(sum())

## You could condense this by using a tuple:

# def sum():
#     (userInput1, userInput2) = ( int(input("Choose your first random number:")) , int(input("Choose your second random number:")) )
#     return userInput1 + userInput2 
# print(sum())



#2: I own a nightclub and need to make sure the people coming in are at least 21. My club runs on a trust basis. Therefore, if you say you are 21 or over, return true or else return false:

# def legalAge():
#     age = int(input("What is your age:"))
#     if age >= 21:
#         print("Have a great time!")
#     else:
#         print("You are not old enough to legally party")
        

# legalAge()


#3: Create a function that plays rock paper scissors with you:
    # - You are to ask the user for INPUT

# import random

# def rPScissors():
#     userInput = int(input("Lets play Rock, Paper, Scissors. Choose 1 for Rock, 2 for Paper, or 3 for Scissors:")) #user input is an integer
#     if userInput == 1:
#         print("You chose Rock")
#     elif userInput == 2:
#         print("You chose Paper")
#     elif userInput == 3:
#         print("You chose Scissors")
    
#     randNum = random.randrange(1,4)
#     print(f"randNum = {randNum}")
#     # print(type(randNum))
#     if randNum == 1:
#         print("You chose Rock")
#     elif randNum == 2:
#         print("You chose Paper")
#     elif randNum == 3:
#         print("You chose Scissors")

#     if userInput == randNum:
#         print("We tied")
#     elif userInput == 1 and randNum == 2: #rock vs paper
#         print("Paper eats Rock. Ha! I win!")
#     elif userInput == 2 and randNum == 3: #paper vs scissors
#         print("Scissors cut Paper. Ha! I win!")
#     elif userInput == 3 and randNum == 1: #scissors vs rock
#         print("Rock crushes Scissors. Ha! I win!")
#     else:
#         print("You beat me this time...")

# rPScissors()


'''Dakota's solutions'''
#  import random
# # Activity 10.3 Create a function that plays rock paper scissors with you...
# # You are to ask to user for input
# # If the user inputs "Rock" -> "scissors" will lose, and 'Paper' will win
# # If the user inputs 'Paper' -> 'Rock' will lose, and 'Scissor' will win
# # If the user inputs 'Scissors' -> 'paper' will lose, and 'Rock' will win
# def rockPaperScissors():
#   userInput = input("Please take a guess ").lower().replace(' ', '')
#   computerPick = ""
#   computerNum = random.randrange(1, 4)
#   # Logic for computer taking it's guess
#   if(computerNum == 1):
#     computerPick = 'rock'
#   if(computerNum == 2):
#     computerPick = 'paper'
#   if(computerNum == 3):
#     computerPick = 'scissors'
#   # Logic for actually playing
#   if(userInput == 'rock' and computerPick == 'paper'):
#     print(f"You lose, {computerPick} beats {userInput}")
#   elif(userInput == 'paper' and computerPick == 'scissors'):
#     print(f'You lose, {computerPick} beat {userInput}')
#   elif(userInput == 'scissors' and computerPick == 'rock'):
#     print(f'You lose, {computerPick} beats {userInput}')
#   elif(userInput == computerPick):
#     print("You guessed the same, try again")
#   else:
#     print(f"You win! {userInput} beats {computerPick}") 
# # rockPaperScissors()
# 
# 
# 
# def rockPaperScissors2():
#   dictOfGuesses = {
#     '1' : 'rock',
#     '2' : 'paper',
#     '3' : 'scissors'
#   }
#   userInput = input('Input your guess ').lower().replace(' ', '')
#   # print(userInput)
#   computerNum = random.randrange(1, 4)
#   computerNumToString = str(computerNum)
#   computerGuess = dictOfGuesses[computerNumToString]
#   # print(computerGuess)
#   if(userInput == 'rock' and computerGuess == 'paper'):
#     print(f"You lose, {computerGuess} beats {userInput}")
#   elif(userInput == 'paper' and computerGuess == 'scissors'):
#     print(f'You lose, {computerGuess} beats {userInput}')
#   elif(userInput == 'scissors' and computerGuess == 'rock'):
#     print(f'You lose, {computerGuess} beats {userInput}')
#   elif(userInput == computerGuess):
#     print("You guessed the same, try again")
#   else:
#     print(f"You win! {userInput} beats {computerGuess}") 
# # rockPaperScissors2()
# 
# 
# 
# def rockPaperScissors3():
#   myGuess = input('Input your guess ').lower().replace(' ', '')
#   computerOptions = ['rock', 'paper', 'scissors']
#   computerGuess = random.choice(computerOptions)
#   if(myGuess == 'rock' and computerGuess == 'paper'):
#     print(f"You lose, {computerGuess} beats {myGuess}")
#   elif(myGuess == 'paper' and computerGuess == 'scissors'):
#     print(f'You lose, {computerGuess} beats {myGuess}')
#   elif(myGuess == 'scissors' and computerGuess == 'rock'):
#     print(f'You lose, {computerGuess} beats {myGuess}')
#   elif(myGuess == computerGuess):
#     print("You guessed the same, try again")
#   else:
#     print(f"You win! {myGuess} beats {computerGuess}") 
#   # print(computerGuess)
# rockPaperScissors3()







''' Module for mathematical statistics available with Python 3.4 or later. This is a CORE module. '''

import statistics


#Creating a set of numeric data to work with:

example = [1, 4, 3, 6, 8, 9]

#Recall the module method: <Module.moduleMethod()

#To calculate the mean of the items in a list:

# mean = statistics.mean(example) #returns a decimal value aka a "Float"

# print(mean)
# print(type(mean))

# median = statistics.median(example) #returns a decimal value aka a "Float"
# #sorts list, then if list has an odd number of values, then it chooses the middle value. If it has an even amount of values, it returns the average of the two middle values. 
# print(median)
# print(type(median))

# hMedian = statistics.median_high(example)
# #sorts list, then if list has an odd number of values, then it chooses the  highest middle value. If it has an even amount of values, it returns the average of the two middle values. 
# print(hMedian)

# lMedian = statistics.median_low(example)
# print(lMedian)

#Standard Deviation

grades = [85, 97, 65, 87, 56, 78, 99]

deviation = statistics.stdev(grades)
#This subtracts the mean from each test score to find their deviation. The deviations are squared and then the squares are added together. Then divide the sum by one less than the total number of exam scores. Take the square root of that number to get the standard deviation. S
print(grades)
print(deviation)


# 

