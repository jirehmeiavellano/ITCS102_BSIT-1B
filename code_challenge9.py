#the parrot simulator program

print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!\n")
phrase = input("What do you want your parrot to say? ")
times = eval(input("How many times should the parrot squawk it? "))
print("\nListen to your parrot:")

for loop in range(times):
    print("🦜 Squawk!" ,phrase)