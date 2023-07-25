# Giving the number of rows to be printed.
rows = int(input("Enter the number of rows: "))
# k = number of stars
k = 0

# printing spaces
# i = rows, j = spaces
for i in range(1, rows + 1):
    for j in range(1, (rows - i) + 1):
        print(end="  ")

    # printing number of stars
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()
