listElements = [20,30,40,60]

def getSum(numbers):
    sum = 0
    for number in numbers:
        sum += number 
    return sum

res = getSum(listElements)
print("The total of list element is: " , str(res))


