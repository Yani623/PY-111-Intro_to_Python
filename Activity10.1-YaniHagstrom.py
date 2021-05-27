'''Write a function using that:
    * takes in an integer as a parameter and:
        * creates a list with the same number of items as the size passed in as an argument 
            ~The digits of the number you put in are separated into a list. 
        * populates the list with a random number between 0 - 1023 (10 bits). You're going to be using the "getrandbits()" method.
'''

import random #importing the CORE modulus

def createList(integer = 3): #the input will be an integer
    newList = [] 

    for x in range(integer):
        randNum= random.getrandbits(10)
        newList.append(randNum)
    
    print(newList)
    
createList(5)


#Elvis' Solution:

# def createRandomList(num = 5):
#     li = [] #making a list that will be populated.
#     randNum = random.getrandbits(10)
#     #.append() will constantly populate the end of a list. 
#     for i in range(num):
#         li.append(randNum)
#     print(li)
#     return li

# createRandomList()

'''Activity 10.2: Create a function that will generate a random list with the values passed in between 20-39.'''

def randList(integer2 = 3):
    newList2 = []
    
    for x in range(integer2):
        newList2.append(random.randrange(20,40))
    
    print(newList2)

randList(5)



random.choices