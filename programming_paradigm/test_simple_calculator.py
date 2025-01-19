#!/usr/bin/env python3

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)            # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)           # Negative and positive integer
        self.assertEqual(self.calc.add(0, 0), 0)            # Zero
        self.assertEqual(self.calc.add(-2, -3), -5)         # Negative integers

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)       # Positive integers
        self.assertEqual(self.calc.subtract(-1, 1), -2)      # Negative and positive integer
        self.assertEqual(self.calc.subtract(0, 0), 0)        # Zero
        self.assertEqual(self.calc.subtract(-5, -3), -2)     # Negative integers

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)       # Positive integers
        self.assertEqual(self.calc.multiply(-2, 3), -6)      # Negative and positive integer
        self.assertEqual(self.calc.multiply(0, 100), 0)      # Zero in multiplication
        self.assertEqual(self.calc.multiply(-4, -5), 20)     # Negative integers

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)          # Positive integers
        self.assertEqual(self.calc.divide(-6, 3), -2)         # Negative and positive integer
        self.assertEqual(self.calc.divide(0, 5), 0)           # Division by a nonzero number should return 0
        self.assertEqual(self.calc.divide(-6, -3), 2)         # Negative integers

        # Edge case: Division by zero, should return None
        self.assertIsNone(self.calc.divide(5, 0))

    def test_divide_edge_cases(self):
        """Test division by zero for edge cases."""
        self.assertIsNone(self.calc.divide(10, 0))             # Division by zero with positive number
        self.assertIsNone(self.calc.divide(-10, 0))            # Division by zero with negative number
        self.assertIsNone(self.calc.divide(0, 0))              # Division by zero where both numbers are zero

if __name__ == '__main__':
    unittest.main()
