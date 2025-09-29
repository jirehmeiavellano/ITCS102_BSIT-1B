#NESTED FOR LOOP (Pyramid or Half Diamond Pattern)

print("\t\t\t   𐙚", end = "")
for j in range(1, 16, 1):
    for m in range(15, j, -1):
        print(" ", end = " ")
    for e in range(1, j, 1):
        print("𐙚", end = " ")
    for i in range(1, j, 1):
        print("𐙚", end = " ")
    print()