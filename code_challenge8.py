#the multiplication table program

print("MULTIPLICATION TABLE MAKER")
value = eval(input("Enter a number --> "))
print("\nMultiplication table for number",value,":")

for loop in range(1, 11, 1):
    total = value * loop 
    print(value, "x" ,loop, "=" ,total)