'''
Expressions
'''

# userInput = int(input("Enter your age as a number, please:"))     

# if (userInput >= 21):
#     print("You're good to go...")
# else:
#     print("You gotta go")

'''
#The conditional statement expression is known as a Ternary Operators.  This translates the if and else statements into a one liner. 

'''

canDrink = "You're good to go" if userInput >= 21 else "You gotta go..."

print(type(canDrink))
print(canDrink)

'''
Just like Ternary Operators into one-liners, Lambda expressions can turn functions into one-liners. Lambdas are one-line functions. Also known as "anonymous functions" which is something more known in other languages. 

You might want to se lambdas when you don't want to use a function twice in a program. They are just like normal functions and even behave like them. 

If the function returns ONE expression from the given arguments, you can convert it into a lambda expression.

"lamda" is a key word. 
'''

# def add(x,y):
#     return x + y
    #I can't store the return value as a variable or pass it in as an argument to another function. I can only call this function, since that's what we do with them. 

# add = lambda x,y : x + y
    # function and argument : output requested

''' To Call:'''


# print(add(4,6))


# def specialAdd(x,y):
#     if x + y > 21:
#         return True
#     else:
#         return False

# def specialAdd(x,y):
#     return True if x + y > 21 else False

''' To further condense it:'''


# specialAdd = lambda x,y : True if x + y > 21 else False
# print(specialAdd(34,8))

'''
List Comprehension:

What if we had a list of numbers and then wanted to return that list with it's values squared and without modifying the actual values that are in the original list?
''' 

'''
Long Method:
'''
# originalList = [1, 2, 3, 4, 5]

# newList = []
# for i in range(len(originalList)):
#     newList.append(originalList[i] ** 2) # ** 2 is used to square a value. 

# print(originalList)
# print(newList)

'''
Using List Comprehension:

newList = [ expression for item in iterable/sequence/collection]

** It's important to understand is that these one-liners come at a price for new developers. They utilize so many fundamental features in one expression that it can be extremely tough to interpret what you're seeing or working with. Think about how many times we have encountered reference errors in our code, and they were all split among several lines. 

'''


# newList2 = [x **2 for x in originalList]

# print(originalList)
# print(newList2)


li = [4, 5, 6, 7, 8, 9, 6, 5]
# for i in range(10):
#     li.append(i)

# print(li)

'''
List Comprehension Equivalent:
    1. Expression
    2. __ for what is withing the "for __ in"
    3. Sequence, iterable, or collection
'''


# li = [i+2 for i in range(10)]
# print(li)



'''
Mini Activity: Create a function called evenNums that takes in a list of numbers as a parameter/argument, and return a new list with only the even numbers. 
'''

# li = [4, 5, 6, 7, 8, 9, 6, 5]
# evenNums = [i for i in li if i % 2 == 0]
# print(evenNums) 


'''Tuple Comprehension'''


# dataset = (1, 2, 3, 4, 5, 6, 323, 54, 23, 64)

# myTuple = tuple(x for x in dataset)  # need to cast into tuple b/c iat returns a "generator"
# myList = [x for x in dataset]


# print(type(myTuple)) 
# print()


''' Dictionary Comprehension'''

# myDict = {k:v for x in dataset}

# print(type(myDict))

# myDict = {}
# for i in range(10):
#     if (i % 2 ==0):
#         myDict[i] = i ** 2

# print(myDict)


'''Using Dict Comprehension'''

# newDict = {i : i ** 2 for i in range(10) if i % 2 == 0}
# print(newDict)

# fahrenheit = {"t1": 23, "t2": 56, "t3": 98}
# print(fahrenheit.items())   # Returns the keys and values as a Tuple as separate item in a list to make them immutable.

# newDict2 = {k: ((5/9) * (v - 32)) for (k, v) in fahrenheit.items()}
# print(newDict2)
#     #This returns a new dictionary, with the same keys used in fahrenheit dictionary, but with the values converted to celsius.

# newDict2 = {k: ((5/9) * (v - 32)) for (k, v) in fahrenheit.items() if v < 25}
# print(newDict2)