# Declaring a Tuple

myTuple = ("Camila", "Lucas", "Dustin")



#myTuple = (0) ** NOT a Tuple bc it only has one item. In order for it to be recognized as a tuple, it needs a comma after the first value. 

##ex) myTuple = (0,) IS a Tuple

# to delete entire Tuple:

## del(myTuple)
## print(myTuple)
##Output: NameError: name 'myTuple' is not defined

#METHODS:

#   Function                Output

## .index("Camila")     0

## .count("Camila")     1

## all(myTuple)

## any(myTuple)

## enumerate(myTuple)       Returns the objects location in memory

## len(myTuple)

## max(myTuple)

## min(myTuple)

## sorted(myTuple)       Returns a sorted LIST

## sum(myTuple)

## tuple(myTuple)       Converts any datatype to a tuple

### Activity5

#Create tuple with different data types.
# myTuple = ("Camila", "Lucas", "Dustin", 719, 1027, 828)

# #print the last item in tuple.
# ## one way to Access the last item in a list or a tuple:
#     # Leveraging the len() method, and subtracting 1 for the "offset" of indexes. 
#         # lastItem = len(myTuple) - 1
#         #print(lastItem)

# print(myTuple[-1])

#Write Python program to get the fourth element from the from and the back of the tuple. 
# partC = (myTuple[3], myTuple[-4])

# print(partC)

# #Write a Python program to find the length of the tuple.

# length = len(myTuple)

# print(length)

#########################################
#Creating Dictionary

## using empty brackets:
    #myDict = {"name":"yani","age":33}

## using dictionary constructor method:
    #myDict2 = dict(name="yani", age= 33)


''' .items() method:

Returns the keys and values as a Tuple as separate item in a list to make them immutable. 
'''


