'''
Activity 11.1:

Write a function that is given a list of exam grades represented by numbers. Calculate the standard deviation of the exam grades represended by some numeric data set. 
-Return a list with all the exam values updated by itself PLUS the stdev. 
-If the score would go above 100, keep the score at 100.
'''

import statistics
import math

grades = [85, 97, 65, 87, 56, 78, 99]

grades2 = [65, 98, 67, 46, 76, 63, 67, 100]

deviation = statistics.stdev(grades)

def curvedGrades(gradeList = [85, 97, 65, 87, 56, 78, 99]):
    deviation = statistics.stdev(gradeList) #gets stdev
    print(f"The standard deviation is {deviation}")
    newList = [] #new list that will be populated with curved grades
    for x in range(0,len(gradeList)): 
        if gradeList[x] < 100: 
            newGrade = gradeList[x] + deviation # Stdev is returned as a float but floats and integers CAN be mixed in arithmetic.
            #newGrade = math.trunc(newGrade)    # Removes the decimals. Does NOT round number up or down. 
            newGrade = round(newGrade)          # Converts a float into an integer and rounds up or down dependant on decimal value. 
            if newGrade > 100:
                newList.append(100)
            else:
                newList.append(newGrade)        # Adds new grade to end of newList
        else:
            newList.append(100) #add 100 if grade is
    
    print(f"Original grades are: {gradeList}")
    print(f"The curved grades are: {newList}")
    return newList

#curvedGrades()

'''
Activity 11.2:

Write a function that returns to me the average value of the curved exam grades.
    -can reference your own function if needed. 
'''


def classMean(newList2 = [90, 50, 60]):
    newList2 = curvedGrades(newList2)
    mean = statistics.mean(newList2)
    print(f"The mean of the class scores is {mean}")

classMean()

