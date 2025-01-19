#!/usr/bin/env python3

def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: please enter numeric values only."
