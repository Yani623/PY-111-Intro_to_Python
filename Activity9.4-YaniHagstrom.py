#Write a function that given a string will return True if the string is a palindrome and False if it is not. 
    #Palindrome is a word that if spelled backwards will return the same word.


def palindrome(string1 = "rotator"):
    for letter in range(0, len(string1)):
        if string1[letter] != string1[len(string1)- (letter + 1)]: #testing index 0 to 7-(0+1)= 6
            return False

        return True

print(palindrome())

#Elvis' Solution

# def isPalindrome(str = "pizza"):
#     originalWordList = list(str)
#         #The list() constructor takes a single argument and returns the elements in list form.
#     reverseWordList = originalWordList.copy()
#     reverseWordList.reverse()
#     #The reverse() operator does not take in any arguments or return any value. It updates the existing list. 
#     print(originalWordList)
#     print(type(originalWordList))
#     print(reverseWordList)
#     print(type(reverseWordList))
#     if(originalWordList == reverseWordList):
#         return True
#     else: 
#         return False

# print(isPalindrome())

Lets play Rock, Paper, Scissors. Choose 1 for Rock, 2 for Paper, or 3 for Scissors:2
You chose Paper
randNum = 3
I challenge you with Scissors
You beat me this time...