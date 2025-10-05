def singleNumber(num):
    result = 0
    for i in range (len(num)):
        result ^= num[i]
    if i == len(num)-1:
        result ^= num[i]+1
    return result
print(singleNumber([1,2,1,2]))