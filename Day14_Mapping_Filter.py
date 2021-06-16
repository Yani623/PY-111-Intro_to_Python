''' With the map() function, the map() method will map a function to a list/collection/sequence. '''

# example = [2, 3, 4, 5, 6]
# squared = []
# for i in range(len(example)):
#     squared.append(example[i] ** 2)

# print(example)
# print(squared) 


'''Example'''

# def squared(x):
#     return x ** 2


# squared2 = list(map(squared, example))   # If you want output as another type, you have to cast it. ex) list().
    # The map method takes in two arguments:
            #1. The function you want to run.
            #2. The object/collection/sequence you're running the function on. 



''' This will perform the function squared on every item in list example and return the squared values in a list.'''

# print(example)
# print(squared2)

'''Recall, Lambda:

function = function and argument : output requested

ex) add = lambda x,y : x + y '''


'''Make squared() function into a lambda and then plug it in as the function in the mapping method:'''

# squared = lambda x: x ** 2

# squared2 = list(map(lambda x: x ** 2, example))


'''W3resource.com Practice Problems:'''

# 1. Write a program to triple all numbers of a given list of integers.

# originalList = [1, 2, 3, 4, 5]
# print(originalList)

# triple = [x * 3 for x in originalList]
# print(triple)


# 2. Write program to add three given lists using python map and lambda.

# li1 = [1, 2, 3, 4, 5]
# li2 = [6, 7, 8, 9, 10]
# li3 = [11, 12, 13, 14, 15]


# addThree = list(map(lambda x, y, z : x + y + z, li1, li2, li3))

# print(li1)
# print(li2)
# print(li3)
# print(addThree)

# 3. Write a Python program to listify the list of given strings individually using Python map.

li4 = ["fog", "rain", "hail"]
list4 = list(map(list, li4))

print(li4)
print(list4)


# 5. Write a Python program to square the elements of a list using map() function: 

# example = [2, 3, 4, 5, 6]

# squared2 = list(map(lambda x: x ** 2, example))
# print(example)
# print(squared2)


# 6. Write a Python program to convert all the characters in uppercase to lowercase and eliminate duplicate letters from a given sequence. Use map() function.

chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}  #This looks like a dictionary, but is a 'set'.
# print("Original Characters:\n",chrars)

# def change_cases(s):
#     return str(s).upper(), str(s).lower()

# result = map(change_cases, chrars)
# print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
# print(set(result))


''' Using list comprehension'''
# print(chrars)

# upLow = list(set([x.swapcase() for x in chrars])) # Used set to remove duplicates and then converted it back to a list. 

# print(upLow)



'''Filter Method:'''


# def evenNumsOnly( dataset = [1, 2, 3, 4, 5, 6, 323, 54, 23, 64]):
#     dataset2 = []
#     for i in range(len(dataset)):
#         if dataset[i] % 2 ==0:
#             dataset2.append(dataset[i])
    
#     print(dataset2)
#     return dataset2

# evenNumsOnly()

''' Same Function Using Filter Method:'''

# dataset = [1, 2, 3, 4, 5, 6, 323, 54, 23, 64]
# evenNumsOnly = list(filter(lambda x: x % 2 == 0, dataset))
#     # For every item in dataset, I will only print it in a list called evenNumsOnly in x % 2 ==0 (only if it is even)

# print(evenNumsOnly)

