rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line
    print()
