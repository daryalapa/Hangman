import unittest
from game import guess_letter


class MyTestCase(unittest.TestCase):
    def test_right_letter(self):
        self.assertTrue(guess_letter(list('hello'), list('*****'), 'h'))

    def test_wrong_letter(self):
        self.assertFalse(guess_letter(list('hello'), list('*****'), 'g'))

    def test_wrong_input(self):
        self.assertRaises(ValueError, guess_letter, list('hello'), list('*****'), '4')

    def test_long_input(self):
        self.assertRaises(ValueError, guess_letter, list('hello'), list('*****'), 'gg')


if __name__ == '__main__':
    unittest.main()
