# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(1, 3), -2)
        # Add more assertions to thoroughly test the subtract method.

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 7), 0)
        # Add more assertions to thoroughly test the multiply method.

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero
        # Add more assertions to thoroughly test the divide method.

if __name__ == "__main__":
    unittest.main()
