import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -2), -4)
        # Add more assertions to thoroughly test the add method. 
            
    def test_subtract(self):
        """test the subtraction method"""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(5, -5), 10)
    
    def test_multiply(self):
        """test the multiplication method"""
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(2, -5), -10)
        self.assertEqual(self.calc.multiply(5, 0),  0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_divide(self):
        """test the division  method"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(10, 0), "Cannot divide by zero")



        




# Remember to write additional test methods for subtract, multiply, and divide.