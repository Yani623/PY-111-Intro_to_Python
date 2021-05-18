# #Mini Activity

# firstWord = "{0}{1}{0}".format("abra", "cad")
# secondWord= "{2}{3}{2}{4}{2}{0}{2}{1}".format("z", "m", "a", "l", "k")
# concat = firstWord + " " + secondWord
# print(concat)


#Activity 4

firstName= "Yanira"
lastName= "Hagstrom"
favoriteColor= "Purple"
favoriteMeal= "Dominican Breakfast"


#F-String

# sentence_a = f"My First Name is {firstName}. My Last Name is {lastName}. My favorite color is {favoriteColor} and my favorite meal is {favoriteMeal}"

# print(sentence_a)



# Concatenation

# sentence_b = "My First Name is"+" " +firstName +". My Last Name is" +" "+ lastName +". My favorite color is" + " "+favoriteColor + " and my favorite meal is" +" "+ favoriteMeal

# print(sentence_b)



#Argument by Position

# sentence_c = "My First Name is {0}. My Last Name is {1}. My favorite color is {2} and my favorite meal is {3}".format( firstName, lastName, favoriteColor, favoriteMeal)

# print(sentence_c)

#Argument by Name

sentence_d = "My First Name is"+" " +firstName +". My Last Name is" +" "+ lastName +". My favorite color is" + " "+favoriteColor + " and my favorite meal is" +" "+ favoriteMeal. format(lastName, favoriteMeal, firstName, favoriteColor)

print(sentence_d)


