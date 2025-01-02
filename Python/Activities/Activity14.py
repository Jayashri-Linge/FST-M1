def fibonacci_Series(number):
    if number <= 1:
        return number
    else:
        return(fibonacci_Series(number-1) + fibonacci_Series(number-2))

getInput = int(input("Enter a number: "))

if getInput <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Sequence: ")
    for i in range(getInput):
        print(fibonacci_Series(i))