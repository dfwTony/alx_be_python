# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Loop through each row using while
while row < size:
    # Print stars in the row using a for loop
    for col in range(size):
        print("*", end="")  # Print star without new line
    print()  # Move to the next line after one row
    row += 1