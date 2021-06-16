#Introductions: 
#A file is an object on a computer that stores data, information, settings, and/or commands used with a computer program

#An example of a computer program would be your Python File/Module. 

#What are some advantages of files: 
# 1. Data is stored permanently
# 2. Updating can be made easy
# 3. Data can be shared among various programs that also with with file objects 
# 4. Huge amounts of data that can be stored in a file

#I want you to know that in general there are two types of files: 
# 1. Text File
# 2. Binary File

#In this lesson and this course, we will be focusing on Text Files: 

#Text Files store the data in the form of "Strings":

#Example: 
'''

"Ram" -> That is stored as 3 characters
234.98 -> That is stored as 6 characters

'''             
#Then there are examples of text files such as: .txt, .c, or .cpp. 
#In today's class we are working with text files with the ".txt" extension

#Let's begin talking about what Python can do with files. Starting with OPENING one: 

#Python has a built in method called "open()"

#Example: 
'''

myFile = open(<file_name>, <open_mode>)

'''

#Our immidiate next questions should be: 
'''
#Student Questions: 
#1. Whatchu mean by <open_mode>
#2. Can You use Path for File Name?
#3. In what context would you use this?
#4. Can you open multi files with that one line?
'''

#Elvis's Pre-Defined Questions: 
'''
#1. What is <open_mode>?
#2. What is <file_name> referring to
#3. Are those two "<file_name> <open_mode>" parameter?
#4. Open is a method?
#5. myFile is the variable storing the newly opened file object?
'''

#Elvis's Pre-Defined Answers: 
'''
#1. myFile indeed is the variable name, and it is assigned the value of the open method with two parameters of "<file_name> <open_mode>"
#2. open() indeed is a method that is used to open a file in Python, and it takes in at least two arguments as referenced above with "<file_name> <open_mode>"
#3. <file_name> and <open_mode> are the parameters that you substitute with arguments representing what those paramters are expecting
#4. <file_name> is referring to the name you want your file to have. Similar to when we hit "Command+S". We choose a name and an extension. Except we are not using our Computer's Graphic User Interface or OS (Operating System) to accomplish this. We are using pure python. 
#5. <open_mode> is referring to a character code that grants different privileges to the file that you are currently creating. The different <open_mode>'s are: 
    #5.1: "w" -> To write the data. If the file already exists, the data will be overwritten.
    #5.2: "r" -> To read the data. The file pointer is positioned at the beginning of the file
    #5.3: "a" -> To append data to a file. The file pointer is positioned at end of the file. 
    #5.4: "w+" -> To write AND read data to/from a file. If the file already exists, the previous data will be overwritten (or lost...)
    #5.5: "r+" -> To read AND write data from/to a file. If the file already exists, your previous data will not be deleted. The file is placed in the beginning of the file. 
    #5.6: "a+" -> To append and to read data from a file. The file pointer will be at the end of the file. 
    #5.7: "x" -> To open the file in exclusive creation mode. the file creation will FAIL if the file already exists. Meaning this is simply to create the file. 
'''

#Let's do an example of each and test them to see their results: 
#myFile = open("Elvis.txt", "x")
#myFile2 = open("Tyler.txt", "x")


# with open("Tony.txt") as files: 
#     line = files.read()
#     print(line)


# myFile3.write("The previous information gets overwritten")




