# medium (midterms exam)

print("Multiplication Columns Table")
columns = eval(input("Enter the number of colmuns: "))

for j in range (1, 11, 1):
    for m in range (1, columns + 1, 1):
        print(f"{j}x{m}={j*m}", end = "\t\t")
    print()

print("\n\nAsterisk Sequence Triangle")
for m in range (1, 6, 1):
    for e in range (6, m, -1):
        print(" ", end="")
    for i in range (1, m + 1, 1):
        print("* ", end="")
    print()