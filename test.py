import unittest
from main import generate_random_list

class TestGenerateRandomList(unittest.TestCase):
    def test_correct_length(self):
        result = generate_random_list(5)
        self.assertEqual(len(result), 5)

    def test_values_are_integers(self):
        result = generate_random_list(10)
        for item in result:
            self.assertIsInstance(item, int)

    def test_values_in_range(self):
        result = generate_random_list(20)
        for item in result:
            self.assertGreaterEqual(item, 0)
            self.assertLessEqual(item, 100)

    def test_zero_length(self):
        result = generate_random_list(0)
        self.assertEqual(result, [])

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            generate_random_list(-1)

if __name__ == "__main__":
    unittest.main()
