#the factorial program

summation = 1
value = eval(input("Enter any number --> "))

for loop in range(value, 0, -1):
    summation *= loop
print("The factorial of", value, "is" ,summation)