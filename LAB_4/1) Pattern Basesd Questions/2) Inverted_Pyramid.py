
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (i - 1), end="")
    for j in range(rows - i + 1):
        print(i, end=" ")
    print()