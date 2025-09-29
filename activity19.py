#NESTED FOR LOOP (Mixed Symbol Patterns)

#start - optional value / parameter (default = 0)
#stop - required vale / parameter
#step - optional value / parameter (default = 1)

for j in range(1, 16, 1):
    for m in range(1, j, 1):
        print("𝜚", end = " ")
    for a in range(15, j, -1):
        print("𝜗", end = " ")
    print()