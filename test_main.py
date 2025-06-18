import unittest
from main import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        length = 16
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_minimum_length(self):
        length = 14
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_too_short_raises(self):
        with self.assertRaises(ValueError):
            generate_password(10)

if __name__ == '__main__':
    unittest.main()
