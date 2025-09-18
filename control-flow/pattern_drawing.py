# Get the size of the pattern from the user
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to the next line after each row
    row += 1  # Increment the row counter