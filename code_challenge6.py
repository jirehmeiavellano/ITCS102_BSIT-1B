#enter 10 random numbers, then get the summation of all odd numbers

summation = 0

for loop in range(1, 11, 1):
   value = int(input("Enter any number --> "))
   if value % 2:
       summation += value
print("The sum of all the given odd numbers is" ,summation)