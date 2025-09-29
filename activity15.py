#String Formatting

#first part
surname = 'Avellano'
mddlname = 'Alimpolos'
frstname = 'Jireh Mei'
nickname = 'Jireh'

print(f"I am {surname}, {frstname} {mddlname}. You can call me {nickname} for short.\n")

#Second Part
sum = 0
for j in range(1,11,1):
    num = eval(input(f"{j} - Input a number --> "))
    sum += num
print(f"The sum of all the numbers given is {sum}")