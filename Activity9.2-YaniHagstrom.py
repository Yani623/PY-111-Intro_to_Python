#Write a function that does what the max(list) methond does.
    #Function should return the greatest value in that list (without using the max(list) Method) when given a list of parameters. 

#max(list): returns the elements from the referenced list with the maximum value. 


#input: list of parameters
#output: largest number in list


def largestNum(myList = [15, 9, 14, 356, 785]):
    myList.sort()
    maxNum = myList[-1]
    # maxNum = newList[-1]
    print(maxNum)
    
largestNum([98,64,73,64])



##Elvis' Solution:
# example1 = [875, 94, 3674, 4563]

# def maxNum(myList = [9, 4, 6, 1, 7]):
#     #define the logic that gets the greatest number. 
#     greatestNum = myList[0]

#     #challenge the first list item for each list item in the list. 
#     #if the current list item is > the greatestNum, then the greatestNum becomes the current list item.
#     for i in range(1,len(myList)):
#         if(myList[i] > greatestNum):
#             greatestNum = myList[i]
            
#     print(greatestNum)
#     return(greatestNum)

# maxNum() #output is 9
# maxNum(example1) #output is 4563
