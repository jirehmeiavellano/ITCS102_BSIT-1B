# while loop 
# laundry anology
# keywords -- while, continue, break
# requirements - boolean variable

isLaundry = True
sum = 0

while isLaundry == True:
    times = input("Do you wiah to continue washing? (yes or no) ").lower()
    sum += 1

    if times == 'yes':
        print("Washing Continues...")
        continue
    else:
        print("Washing Stops...")
        break

print("Number of cycle is", sum)