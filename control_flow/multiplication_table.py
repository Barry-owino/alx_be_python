#!/usr/bin/env python3

number = int(input("Enter a number to see its multiplication table: "))

print(f"You entered: {number}")

print(f"\nMultiplication Table for {number}:")

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")


