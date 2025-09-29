#NESTED FOR LOOP (Numeric Pyramid Pattern)

print("\t\t1", end = "")
for j in range(1, 10, 1):
    for m in range(9, j, -1):
        print(" ", end = " ")
    for e in range(j, 1, -1):
        print(e, end = " ")
    for i in range(1, j + 1, 1):
        print(i, end = " ")
    print()