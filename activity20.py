#NESTED FOR LOOP (Diamond Pattern)


for j in range(1, 16, 1):
    for m in range(15, j, -1):
        print(" ", end = " ")
    for e in range(1, j, 1):
        print("✦", end = " ")
    for i in range(1, j + 1, 1):
        print("✦", end = " ")
    print()

for j in range(14, 0, -1):
    for a in range(15, j, -1):
        print(" ", end = " ")
    for v in range(1, j, 1):
        print("✦", end = " ")
    for l in range(1, j + 1, 1):
        print("✦", end = " ", )
    print()
