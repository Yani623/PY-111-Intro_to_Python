#For Loop Reintroduction
##Counter Controlled Loops.

#You can perform loops on a /sequence collection object directly or run an for loop on a range function.
 #Three components:
        #1: Initializing the Index/Counter
        #2: Creating the condition -  to indicate whether or not to re-execute the statements within the for loop.
        #3: Incramentation -  to indicate how much you would like to increase or decrease by at each loop iteration. 

myCryptos = [ "Ether", "Stellar", "Nexo"]

##Range Function:

# for counter in range(10): #can add a third argument that sets incrament. if left blank, incraments by value of 1. 
#     print(f"Elvis is currently at iteration number: {counter}")

# # length = len(myCryptos)
# for counter in range(0,len(myCryptos)):
#     print(f"Elvis' Fav Crypto is {myCryptos [counter]}")



##Object Function:

# for counter in myCryptos:
#     print(f"Elvis' favorite cryto is: {counter}")

##Practice: Get the sum of list using a for loop using range and object:

# myList = [5, 10, 15, 20]
# sum = 0
# sum2 = 0

# for index in myList:
#     sum = sum + myList[index]
    
# print(sum)

    #Output: IndexError: list index out of range

# for listItem in myList:
#     sum = sum + listItem # index is not the index location for myList. 
#     #*** sum += index will give the same result with less code***
# print(sum)

#     #Output: 50
#     # +=

# for listItem in range(0,4):
#     sum2 = sum2 + myList[listItem]
# print(sum2)


##Nested List:

myList =  ["Elvis", "Tyler", "Anthony"]
myDict = {"name": "Elvis", "age": 27}
myTuple = ("Elvis", "Tyler", "Anthony")
#All one dimensional collections

# #A multidimensional list:
# myList2 = ["Elvis", ["Ethereum", "Stellar"], "Tyler"]
# #We will need another index to access Ethereum on it's own.

# print(myList2[1][0])

# myList3 = ["Elvis", ["Ethereum", "Stellar", ["Kucoin", "Bitmart", "Nexo", "Coinbase"]], "Tyler"]

#Practice by changing Nexo to Trust from myList3 then print to see
#Step 1: extract the value
#Step 2: Re-Assign the value to be "Trust"
#changing Nexo to Trust:
# myList3[1][2][2] = "Trust"


#Step 3: Print the list again to see the modification.

# print(myList3)


##Printing every item in a list:

myList3 = ["Elvis", ["Ethereum", "Stellar", ["Kucoin", "Bitmart", "Nexo", "Coinbase"]], "Tyler"]

for i in myList3:
    print(i)
    for j in myList3[1]:
        print(j)
    #     for k in myList3[1][2]:
    #         print(k)
