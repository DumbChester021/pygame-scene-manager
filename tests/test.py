# test_your_module.py

import unittest
from src.your_module import your_function

class TestYourModule(unittest.TestCase):
    def test_your_function(self):
        result = your_function(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
