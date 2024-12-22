#!/bin/bash

number = int(input("Enter a number to see its multiplication table: "))

print(number)

print(f"Multiplication Table for {number}:")

for i in range(1, 11):  # Iterate from 1 to 10
     product = number * i
     print(f"{number} * {i} = {product}")

