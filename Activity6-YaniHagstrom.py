
#Create a Dictionary named car with keys for brand, model and year and values to describe a 1964 Ford Mustang.

car = {"year":"1964", "brand":"Ford", "model":"Mustang"}

#Access the dictionary to print the value of the "model" of the car.

# print(car.get("model"))

#Perform Dictionary Methods on Your Object, and in a comment explain the result you expected vs the result you got. 


#clear

# car.clear()

# print(car)
    ##outcome as expected

#copy

# car.copy()

# print(car)
    ##outcome as expected

#fromkeys

#attempt 1
# car.fromkeys("model")
# print(car)

# #attempt 2
# print(fromkeys({"model"="Mustang"})
    ## I was expecting the name of the dictionary (car) when I specified a key and it's value within the dictionary. I keep getting a syntax error. 

#get

# print(car.get("model"))


#setdefault

# print(car)

# print(car.setdefault("color"))

# print(car)
    ##outcome as expected

#items

print(car.items())
    ##output as expected










