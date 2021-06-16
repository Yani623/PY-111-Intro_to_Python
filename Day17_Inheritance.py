# return int(round(num, -1))

def round10(num):
    num1 = str(num) 
    li = [int(x) for x in num1]
    if li[-1] in range(5,10):
        roundUp = num + (10 - li[-1])
        return roundUp
    elif li[-1] in range(1,5):
        roundDown = num - (10 - li[-1])
        return roundDown

    

# round10( 16)
# print(round10(16))  



def round_sum(a = 16 , b = 17, c = 18):
    return round10(a) + round10(b) + round10(c)

round_sum(12, 56, 78)
print(round_sum(12, 56, 78))