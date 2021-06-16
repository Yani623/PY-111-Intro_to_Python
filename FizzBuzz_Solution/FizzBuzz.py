''' FizzBuzz Challenge:
print out the values 1-100. except, if the number is divisible by 3, instead of printing the number, print "fiz", if number is divisible by 5, print "buzz", if divisible by 3 and 5, print "fizzbuzz"'''


li = list(range(0,101))
# print(li)
# print(type(li[1]))# int

def fizz_Buzz(li1 = []):
    for x in range(1, len(li1)):
        if (li1[x] % 3) == 0 and (li1[x] % 5) == 0:
            print("FizzBuzz") 
        
        elif (li1[x] % 5) == 0:
            print("Buzz")
        
        elif (li1[x] % 3) == 0:
            print("Fizz")
        
        else:
            print(li1[x])
    

fizz_Buzz(li)