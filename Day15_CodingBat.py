'''1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.'''

# sleep_in = lambda x: True if not "weekday" or "vacation" else False
# print(sleep_in("weekday"))


'''2. Given two int values, return their sum. Unless the two values are the same, then return double their sum.'''

# sum_double = lambda a, b: (a + b)* 2 if a == b else a + b
# print(sum_double(2,2))


'''3. Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.'''

# absDif = lambda n : abs(n - 21)* 2 if n > 21 else abs(n-21)


'''4. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.'''

# parrot_trouble = lambda talking, hour : True if talking and hour in range(7,21) else False

'''5. Given 2 integers, a and b, return True if one if them is 10 or if their sum is 10.'''

# def makes10(a, b):  
#     if(a == 10 or b == 10):
#         return True
#     elif(a + b == 10):
#         return True
#     else:
#         return False

# #OR 

# def makes10(a, b):
#     return True if (a == 10 or b == 10) or (a + b == 10) else False  

# #OR

# makes10 = lambda a, b: True if (a == 10 or b == 10) or (a + b == 10) else False


'''6. Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number. '''

# near_hundred = lambda n: True if n in range(90,111) or n in range(190, 211) else False

'''7. Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.'''

# def pos_neg(a, b, negative):
#     if negative:
#         return (a < 0 and b < 0)
#     else:
#         return ((a < 0 and b > 0) or (a > 0 and b < 0))

# #OR

# def pos_neg(a, b, negative):
#     return True if ((a < 0 and b > 0 and not negative) or (a > 0 and b < 0 and not negative)) or ( a < 0 and b < 0 and negative) else False

#OR

# pos_neg = lambda a, b, negative: True if (a < 0 and b < 0 and negative) or (a < 0 and b > 0 and  negative) or (a > 0 and b < 0 and negative) else False   


# print(pos_neg(-2,-3,"negative))


def reverse(nums = [4, 5, 6, 7]):
    nums = nums[:1]
    #nums[1:] = [5, 6, 7]   nums[:1] = [4]
    return nums

print(reverse())

