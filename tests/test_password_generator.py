import unittest
from src.password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    
    def test_default_length(self):
        self.assertEqual(len(generate_password()), 12)

    def test_custom_length(self):
        self.assertEqual(len(generate_password(16)), 16)
    
    def test_with_digits(self):
        password = generate_password(use_digits=True)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_with_special_chars(self):
        password = generate_password(use_special_chars=True)
        self.assertTrue(any(char in "!@#$%^&*()_+[]{}|;:,.<>?" for char in password))

if __name__ == "__main__":
    unittest.main()
