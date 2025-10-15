
# MODULES -- Python file management

import random

print("GUESSING GAME......")
print("———————————————————\n")

# setting up random values
any_value = random.randint(1, 50)
times = 0
isGuess = True

while isGuess == True:
    num = eval(input("Guess a random number for 1 to 50 --> "))

    times +=1
    if num == any_value:
        print("WINNER, Send GCASH")
        print("Random value is", any_value)
    else:
        print("Incorrect, Try Again")
        continue
print("You guessed", times, "times")