

# def make_bricks(small, big, goal):
#     x = goal - (big *5) # if small >= x. => True
#     y = goal - small  # if big(5) >= y.

#     if big >= 1 and big * 5 > goal:
#         if y % 5 == 0:
#             return True
#         else:
#             return False
#     if small >= x or big*5 >= y:
#         return True
#     else: 
#         return False

# make_bricks(3,1,9)
# print(make_bricks(3,1,9))


def round10(num):
    return (num+5)/10+10

def round_sum(a, b, c):
    
    return round10(a)+round10(b)+round10(c)

round_sum(16, 17, 18)
print(round_sum(16, 17, 18))