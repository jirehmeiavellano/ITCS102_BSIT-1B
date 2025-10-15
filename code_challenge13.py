# SUMMATION OF ODD NUMBERS

isName = input("Input your name --> ").lower()
print("———————————————————————————————————")
print("ODD NUMBER SUMMATION, press 0 stop")
print("———————————————————————————————————\n")

isNumber = True
sum = 0
odd_numbers = ""

while isNumber  == True:
    num = eval(input("Input a random number: "))

    if num == 0:
        print("Program Stops!!!")
        break
    elif num % 2 == 0:
        print("EVEN NUMBER DETECTED, code continues")
        continue
    elif num % 2 == 1:
        sum += num
        odd_numbers += str(num) + " "
        print("ODD NUMBER DETECTED, code continues")
        continue
    else:
        print("Invalid Output")
        continue

print("Hi,", isName, "the sum of all ODD numbers is", sum)
print("ODD numbers detected included the ff", odd_numbers)