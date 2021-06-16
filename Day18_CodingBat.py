'''List_2> Sum 13:
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
'''

nums1 = [1, 2, 2, 1] #→ 6
nums2 = [1, 1] #→ 2
nums3 = [1, 2, 2, 1, 13] #→ 6

'''Using For Loop'''

# def sum13(nums):
#     if len(nums) == 0:
#         return 0
    
#     sumNums = 0
    
#     if nums[0] == 13:
#         for x in range(1,len(nums)):
#             if nums[x] == 13: 
#                 continue
#             elif nums[x-1] == 13:
#                 continue
#             elif nums[x] != 13:   
#                 sumNums += nums[x] 
#     elif nums[0] != 13:
#         sumNums = nums[0]
#         for x in range(1,len(nums)):
#             if nums[x] == 13: 
#                 continue
#             elif nums[x-1] == 13:
#                 continue
#             elif nums[x] != 13:
#                 sumNums += nums[x]
            
#     return sumNums


# sum13(nums3)
# print(sum13(nums3))

'''Using While Loop'''

# def sum13(nums):
#     sumNums = 0
#     x = 0

#     while x < len(nums):
#         if nums[x] == 13:
#             x += 2 # replacing x with (x + 2) to skip the next element in the list.
#             continue # continuing the while loop  with the new x value. 
#         sumNums += nums[x]
#         x += 1
#     return sumNums

# sum13(nums1)
# print(sum13(nums1))


'''list-2 > sum67:

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''

nums4 = [2, 7, 6, 2, 6, 7, 2, 7]

# def sum67(nums):
#     if len(nums) == 0:
#         return 0
    
#     total = 0
#     x = 0
    
#     while x < len(nums):
#         if nums[x] != 6:  
#             total += nums[x]
#         elif nums[x] == 6: 
#             i = x + 1 # starts checking from the element after x
#             while i < len(nums):
#                 if nums[i] != 7: 
#                     i += 1 # since != 7, need to move to next i
#                     x = i # since we will be going back to our 1st while loop, we need to keep track of where in the loop we should be. 
#                     continue
#                 elif nums[i] == 7:
#                     x = i # we need this final number to ensure we return to the correct x after nums[i] == 7
#                     break
#         x += 1    # on to the next one   

#     return total

# sum67(nums4)
# print(sum67(nums4))


''' Warmup-2 > array123:
Given an array of integers, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''


nums5 = [1, 1, 2, 4, 1]

def array123(nums):
    if len(nums) < 3:
        return False

    for x in range(len(nums)):
        
        if nums[x] != 1:
            x += 1
            continue
        elif nums[x] == 1:
            if (x+2) > len(nums): # has to be x+2 because it is comparing the index to the length of the list which is always 1 greater than the last index.
                return False
            elif nums[x+1] != 2:
                x += 1
                continue
            elif nums[x+1] == 2:
                if (x+3) > len(nums):
                    return False
                elif nums[x+2] != 3:
                    x += 1
                    continue
                elif nums[x+2] == 3:
                    return True
            
            
        
    
array123(nums5)
print(array123(nums5))

#CodingBat Solution:

def array123(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    # ex) nums5 = [1, 1, 2, 4, 1], len(nums5)-2 = 3
    for i in range(len(nums)-2): # from nums[0] to nums[3]
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False