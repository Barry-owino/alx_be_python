#!/bin/bash
#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#operation  = str(input("Choose the operation (+, -, *, /): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Division by zero is not allowed. Please try again.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please enter one of +, -, *, or /.")
