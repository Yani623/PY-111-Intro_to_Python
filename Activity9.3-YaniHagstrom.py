# Write a function called isSorted which will be passed in a list of numbers.
    #function should determine if the list is in need of being sorted or if it already is. 
    #function should return a boolean determining whether or not that is the case. 
        #output of True if already sorted OR False if not sorted

#define the function isSorted with a list of integers

def isSorted(myList = [0, 2, 4, 98, 9, 15, 34, 64, 74, 89, 99]):
    for i in range(0, len(myList)): #i is index
        if i > (i + 1):
            #need to use myList[i] > myList[i+1]
            return False
        else:
            return True
            
print(isSorted())
    ##Output kept giving True because I was not referencing the list index correctly. Should have used list name to call the value of the index i instead of calling the index itself. 
        



# Elvis's solution:

# def isSorted(myList = [1, 2, 3, 4, 5]):

#     for item in range(0, len(myList)):
#         if(myList[item] > myList[item + 1]):
#             return False

#         return True

# print(isSorted())

