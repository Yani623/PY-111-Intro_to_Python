#Defining a function
    #def FUNCTION NAME ():
        ## Consider if this function needs a parameter/argument

# def printStuff():
#     print("Hello World")
#     print("Yani")

# printStuff()
    # output =  Hello World
    #           Yani

########################

## assigning a value. name is the placeholder/parameter and "Yani" is the argument.
def printIt(name = "Yani"):
    print(f"Hi my name is {name}")
    ## f in parenthesis is the f string function. 

printIt()
# printIt("Camila")
    ## output =  Hi my name is Yani
    ##           Hi my name is Camila



########################

# Return 

def gimmeFive():
    return 5

print(type(gimmeFive()))
    ##output = <class 'int'>



