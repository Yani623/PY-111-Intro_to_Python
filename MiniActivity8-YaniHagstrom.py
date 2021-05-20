#1: Create a While Loop that goes through the 12 days of christmas:


# i = 0 #index

# gift = ["puppy", "socks", "chocolates", "earings", "vacations", "kittens", "apples", "bananas", "pears", "shoes", "rings", "bracelets"]

# n = 1 #day
# length = len(gift)

# while(i < length):
#     print(f"On the {n} day of Christmas my true love gave to me, {n}", gift[i]) # has to come before the equations to include index 0.
#     n = n + 1
#     i = i + 1
    




#2: Create a While Loop that takes a list of integers and gives the sum of the integers.

#Attempt 1
# myList1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# i = 0
# #len = 11
# while(i < (len(myList1))):
#     sum = myList1[i] + myList1[i + 1] 
#     i = i + 1      
#     print(sum)
    # outputs sums list. We want the total sum only....

#Attempt 2

# myList1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# length = len(myList1)
# sum = 0
# i = 0 #index

# while(i < length):
#     sum = sum + myList1[i]
#     i = i + 1

# print(sum)



# # Elvis' solution
# sum = 0
# i = 0
# myList = [1, 4, 3, 5, 6]
# length = len(myList)
# while(i < length):
#     sum = sum + myList[i]
#     i = i + 1


#Mini Activity 8.1.2:

#1: Create a For Loop that goes through the 12 days of christmas:


# gift = ["puppy", "socks", "chocolates", "earings", "vacations", "kittens", "apples", "bananas", "pears", "shoes", "rings", "bracelets"]

# i = 0 #index

# for x in range(1,13):
#         print(f"On the {x} day of Christmas, my true love gave to me, {x}", gift[i])
#         i = i + 1



#2: Create a For Loop that takes a list of integers and gives the sum of the integers:

# myList1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# y = len(myList1) + 1
# sum = 0

# for x in range(0, 10):
#     sum = sum + myList1[x]
#     x = x + 1

# print(sum)