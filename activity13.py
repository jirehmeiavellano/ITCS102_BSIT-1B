#getting the summation of all numbers

summation = 0
for loop in range(1, 16, 1):
    value = eval(input("Enter any number --> "))
    summation += value
print("The sum of all the numbers is", summation)