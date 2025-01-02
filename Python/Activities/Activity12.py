def totalSum(num):
    if num:
        return num + totalSum(num-1)
    else:
        return 0
    
result = totalSum(10)
print(result)