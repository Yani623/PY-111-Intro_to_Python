'''
User Input: '''

# userinput = input("Enter your age:") #this prompts the user to input a value in the terminal and stores the value. 
# print(userinput)

#This returns a string...
#Casting is when you return a data type and wrap it or "cast" it into another. Ex: using the list construct method to change a string into a list. 


# #Range requires an integer. Therefore we need to cast it to make it a number. We do this by using the constructor method of an integer: int()
# age = int(userinput)
# print(age)

# for i in range(age):
#     print(f"Are you {i+1}")

'''
Created arithmetic functions in a file called Example.py
Using this file, we will learn to use custom modules 
Modules are files containing a set of functions to include in your application. 

Importing:
'''

# import Example 
#    #this is necessary before being able to reference a function in the file. 

# solution = Example.add(2, 3)
# print(solution)

# solution1 = Example.substract(2,3)
# print(solution1)

# solution2 = Example.multiply(2,3)
# print(solution2)

# solution3 = Example.mod(3, 2)
# print(solution3)


# #importing specific functions when you only need one function then you only need to call the function, not the filename.function name()
# from Example import add

# solution4 = add(2,3)
# print(solution4)


'''
python modules that you can install using pip (P)ython (I)nstall (P)achage. Ex: "Django"

Django is a framework that exists on top of Python Programming Language to handle server-side back-end website logic. 

"Distributions" are dedicated packages. The dedicated distribution for Data Science and Machine Learning is called "Anaconda"

CORE Modules are already installed in python. Therefore can just be imported without referencing a file. 
Calling a module: <Module>.<Module_Method>
'''

# import datetime #module built into python

# today = datetime.date.today()
# print(today)
#     #output is: 2021-05-26

from math import trunc
import random
#Random has a method called getrandbits() which will return a random number from 0 up to whatever max value you can get with the "bits" that you passed in. It takes in an argument, a number which represents the amount of bits you're working with. 
# randNum = random.getrandbits(4)
# print(randNum)

''' Let's say that we want to generate a random number, but we don't want to represent the range by the amount of bits, but explicitly with a range and using decimal number.Python and it's random module are good for that. 
    .randrange(x, y): x defines the starting point (inclusive) and y defines the stopping point (exclusive)
EX) we have radrange(0, 10). We will have a function that will generate a random number from 0 - 9.
'''


'''
Importing python installed package module (PIP): "sudo pip3 install camelcase"
We installed Camelcase. Camelcasing is when instead of using spaces to separate words, you structure if as follow:
    firstSecondThirdFourthFifth
    baconEggsCheese
    peanutButterJelly

To extract/import: <Module>.<Module_Method>
'''
# import camelcase

# camelObj = camelcase.CamelCase()

# print(camelObj.hump("is night")) #Capitalizes first letter of every word in a string that is separated by a space.
#                                     #Note: this will never capitalize the word "is".


'''
Strings with decimals cannot be immediately cast to an integer because integers do not have decimals, but floats do handle decimals and can be cast to integers.

Call float(string) to convert string into a float. Call int(float_obj) with float_obj as the result of the previous step to convert float_obj into an integer.'''
import math
#Ex:

grades = "98.7"
print(grades)
print(type(grades))

grades = float(grades)              # makes string decimal value into a float
print(grades)
print(type(grades))


grades = round(grades)             # Converts float into an integer and rounds up or down based on decimal values. 
grades = math.trunc(grades)        # makes float into an integer but rounded down.
print(grades)
print(type(grades))




