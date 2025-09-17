#the countdown timer

print("⏳️ COUNTDOWN TIMER SIMULATOR")
value = eval(input("\nEnter the starting number for countdown --> "))
print("\nCountdown Started:")

for loop in range(value, 0, -1):
    print(loop)
print("Liftoff!")