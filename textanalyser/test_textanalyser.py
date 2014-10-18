import unittest
import textanalyser

class TestTextanalyser(unittest.TestCase):
    def test_find_most_common_first_letter(self):
        self.assertEqual('t', textanalyser.find_most_common_first_letter('sample.txt'))


if __name__ == '__main__':
    unittest.main()
