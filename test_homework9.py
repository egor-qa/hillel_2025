import unittest
from homework9 import sum_of_numbers
from homework9 import average_numbers
from homework9 import reverse_string
from homework9 import longest_word



class MyTestCase(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(sum_of_numbers(15, 12), 27 )      # equal a == b

    def test_sum2(self):
        self.assertNotEqual(sum_of_numbers(15, 12), 28)    # not equal a != b

    def test_sum3(self):
        self.assertGreater(sum_of_numbers(15, 12), 20)         # greater a > b

    def test_sum4(self):
        self.assertLess(sum_of_numbers(15, 12), 100)           # less a < b

    def test_sum5(self):
        self.assertGreaterEqual(sum_of_numbers(15, 12), 26)    # greater or equal a >= b

    def test_sum6(self):
        self.assertLessEqual(sum_of_numbers(15, 12), 29)       # less or equal a <= b


class AverageNumber(unittest.TestCase):
    def test_average_true_list1(self):
        self.assertEqual(average_numbers([7, 44, 13, 37, 4, 11, 12, 14]), 17.75)

    def test_average_true_list2(self):
        # self.assertAlmostEqual(average_numbers([7, 44, 13, 37, 4, 11, 12, 14]), 17.75)
        self.assertAlmostEqual(average_numbers([-4, 4]), 0.0)                         # almost equal

class ReversedList(unittest.TestCase):
    def test_reversed_list(self):
        input_text = "Hello Python world!"
        expected_result = "!dlrow nohtyP olleH"
        self.assertEqual(reverse_string(input_text), expected_result)

class LongestWord(unittest.TestCase):
    def test_longest_word(self):
        self.assertNotEqual(longest_word(["Longest", "word", "in", "this", "sentence"]), "Longest")

    def test_longest_word2(self):
        self.assertEqual(longest_word(["Longest", "word", "in", "this", "sentence"]), "sentence")
