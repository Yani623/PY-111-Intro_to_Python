#Create a Function that is given a list of 3 different numbers as a parameter.
    #Sort this list in any way other than using the List object. That means no calling the ".sort()" or "sorted()" method. 



def increasing(a , b, c):
    if(a < b and b < c):
        return [a, b, c]
    elif(a > b and b < c):
        return [b, a, c]
    elif(a > c and b < c):
        return [b, c, a]
    elif(b > a and a > c):
        return [c, a, b]
    elif(a < c and b > c):
        return [a, c, b]
    elif(c < b and a > b):
        return [c, b, a]

print(increasing(74, 96, 253))

### Elvis' Solution: **Incomplete

# def sortList(myList = [8, 3, 6]):
#     #write the logic that sorts the list
#     smallestNum = 0
#     middleNum = 0
#     greatestNum = 0

#     if(myList[0] > myList[1] and myList[0] > myList[2]):
#         greatestNum = myList[0]
#     elif(myList[0] < myList[1] and myList[0] < myList[2]):
#         smallestNum = myList[1]
#     else:
#         middleNum = myList[1]

#     myList.clear()
#     myList.append(smallestNum)
#     myList.append(middleNum)
#     myList.append(greatestNum)

#     print(myList)
#     return myList

# sortList([9, 8, 6])








