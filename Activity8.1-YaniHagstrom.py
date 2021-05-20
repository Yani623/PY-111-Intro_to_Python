
#Without using any built in string or list method, create a function that takes in 3 integers as parameters.

#Perform some operation that will compare these values and order them from least to greatest.

#Return these values as a set in tuple.


def increasing(a , b, c):
    if(a < b and b < c):
        return a, b, c
    elif(a > b and b < c):
        return b, a, c
    elif(a > c and b < c):
        return b, c, a
    elif(b > a and a > c):
        return c, a, b
    elif(a < c and b > c):
        return a, c, b
    elif(c < b and a > b):
        return c, b, a

print(increasing(77, 13, 125))

print(type(increasing(77, 13, 125)))

