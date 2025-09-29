temp = input("Enter Temperature --> ")

if temp.isnumeric():
    if int(temp) <= 0:
        print("The Temperature is Considered as Freezing")
    elif int(temp) >= 1 and int(temp) <= 15: 
        print("The Temperature is Considered as Extremely Cold")
    elif int(temp) >= 16 and int(temp) <= 30:
        print("The Temperature is Considered as Cold")
    elif int(temp) >= 31 and int(temp) <= 38:
        print("The Temperature is Considered as Lukewarm")
    elif int(temp) >= 39 and int(temp) <= 42:
        print("The Temperature is Considered as Warm")
    elif int(temp) >= 43 and int(temp) <= 50: 
        print("The Temperature is Considered as Hot")
    elif int(temp) > 51 and int(temp) <= 60: 
        print("The Temperature is Considered as Extremely Hot")
    elif int(temp) >= 61:
        print("The Temperature is Considered as Burning")
else:
    print("Invalid Temperature")