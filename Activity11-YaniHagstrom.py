'''
Activity 11.1:

Write a function that is given a list of exam grades represented by numbers. Calculate the standard deviation of the exam grades represended by some numeric data set. 
-Return a list with all the exam values updated by itself PLUS the stdev. 
-If the score would go above 100, keep the score at 100.
'''

import statistics
import math

grades2 = [65, 98, 67, 46, 76, 63, 67, 100]

print("Activity 11.1:")
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

curvedGrades()

'''
Activity 11.2:

Write a function that returns to me the average value of the curved exam grades.
    -can reference your own function if needed. 
'''

print("Activity 11.2:")
def classMean(newList2 = [90, 50, 60]):
    newList2 = curvedGrades(newList2)
    mean = statistics.mean(newList2)
    print(f"The mean of the class scores is {mean}")

classMean()

'''
Activity 11.3:

Create a function that given a list of numbers will return:
    - A list of booleans
        * If the numbers are < 55, substitute the item with False. Otherwise, return True
    
    - Return must be in list type (show type)

'''
print("Activity 11.3:")
def retirementAge( age = [25, 86, 55, 46, 56, 48, 67]):
    for x in range(0, len(age)): 
        if age[x] < 55:
            age[x] = False
        else:
            age[x] = True
            
    print(age)
    return age

retirementAge()



#Elvis' Solution:

# def numToBool(dataset = [55, 98, 34, 65, 75, 85]):
#     for i in range(0, len(dataset)):
#         if dataset[i] < 55:
#             dataset[i] = "False"
#         else:
#             dataset[i] = "True"
#     print(dataset)
#     return dataset

# numToBool()

'''
Activity 11.4:

Create a function that takes in a list and returns:
    -How many people, in a list of grades, have passed the class
        *print a message telling me how many people passed or failed the class if >= 55 is passing.
'''
print("Activity 11.4:")
def passFail(grades = [25, 86, 55, 46, 56, 48, 67]):
    for x in range(0, len(grades)):
        if grades[x] <55:
            grades[x] = False
        else:
            grades[x] = True
    print(grades)
    countFailed = grades.count(False)
    countPassed = grades.count(True)
    print(countPassed, "students passed,", countFailed, "students failed")
    

passFail()


# #Elvis' Solution:

# def classReport(dataset = [55, 98, 34, 65, 75, 85]):
#     passing = 0
#     failing = 0

#     for i in range(len(dataset)):
#         if dataset[i] < 55:
#             failing += 1
#         else:
#             passing +=1
#     sentence = f"You have {passing} passing students and {failing} failing students"
#     print(sentence)
#     return sentence

# classReport()

