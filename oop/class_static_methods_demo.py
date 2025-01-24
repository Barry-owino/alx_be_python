#!/usr/bin/env python3

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Returns the sum of two numbers.

        :param a: First number.
        :param b: Second number.
        :return: Sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Returns the product of two numbers and prints the class attribute calculation_type.

        :param a: First number.
        :param b: Second number.
        :return: Product of a and b.
        """
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 20)
    print(f"Sum: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 20)
    print(f"Product: {product_result}")
