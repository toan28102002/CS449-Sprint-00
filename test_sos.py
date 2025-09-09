import unittest

# Function to add two numbers
def add_numbers(x, y):
    return x + y 

# Unit test class
class AdditionTests(unittest.TestCase):
    """Tests for the add_numbers function."""

    def test_two_positive(self):
        """Adding two positive numbers should return correct sum."""
        self.assertEqual(add_numbers(7, 5), 12)

    def test_two_negative(self):
        """Adding two negative numbers should return correct sum."""
        self.assertEqual(add_numbers(-3, -8), -11)

if __name__ == "__main__":
    unittest.main()
