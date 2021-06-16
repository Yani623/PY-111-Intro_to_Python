

[1, 1, 6, 7, 2]

def sum67(nums = [1, 1, 6, 7, 2]):
    for x in range(len(nums)):
        sum1 = 0
        sum2 = 0
        if nums[x] != 6:
            sum1 =+ nums[x]
        if nums[x] == 6:
            if nums[x] == 7:
                sum2 += nums[x]
        else:
            continue
        sum3 = sum1 + sum2
    print(sum3)
    return sum2 + sum1


sum67()

round()
