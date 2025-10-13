# easy (midterms exam)

print("Asterisk Triangle")
for m in range (1, 6, 1):
    for e in range (7, m, -1):
        print(" ", end="")
    for i in range (1, m*2, 1):
        print("*", end="")
    print()

print("\nNumber Sequence")
for j in range (1, 6, 1):
    for a in range (1, j, 1):
        print(j, end = "")
    print(j)