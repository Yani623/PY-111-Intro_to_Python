'''
16) Given two int values, return their sum. Unless the two values are the same, then return the square of their sum.


sum_squared(1, 2) → 3
sum_squared(3, 2) → 5
sum_squared(2, 2) → 16
'''

# def sum_squared(a, b):
#     if a == b:
#         return (a+b) ** 2
#     return a+b

# sum_squared(3, 2)
# print(sum_squared(3, 2))



'''
17)
Using List Comprehension, write a function that given a list of numeric values will generate and return a new list of values with each item in the original list cubed (raised to the third power)

Input: [0, 1, 2, 4] 
Output: [0, 1, 8, 64]
'''
# li = [0, 1, 2, 4]
# li2 = [x ** 3 for x in li]

# print(li2)




'''
18)
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
'''

# def has23( a, b):
#     if a == 2 or a == 3 or b == 2 or b == 3:
#         return True
#     return False

# has23(4,5)
# print(has23(4,5))



'''
19)
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

# li2 = [2, 2, 0]

# def count_evens(li = [2, 1, 2, 3, 4]):
#     count = 0
#     for x in range(len(li)):
#         if li[x] % 2 == 0:
#             count += 1

#     return count

# count_evens(li2)
# print(count_evens(li2))








'''
20)
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''


# def lucky_sum(a, b, c):
#     sum = 0
#     if a != 13:
#         sum += a
#         if b != 13:
#             sum += b
#             if c !=13:
#                 sum +=c
#     return sum

# lucky_sum(1, 13, 3)
# print(lucky_sum(1, 13, 3))
















