#!/bin/bash
pattern_size = int(input("Enter pattern size:"))
print(pattern_size)

if pattern_size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0

    # Outer while loop for rows
    while row < pattern_size:
        # Inner for loop for columns
        for col in range(pattern_size):
            print("*", end="")  # Print * without a newline
        print()  # Move to the next line after finishing a row
        row += 1

