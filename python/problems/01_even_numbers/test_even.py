import unittest

from even import even


class EveningAList(unittest.TestCase):
    def test_returns_empty_list_if_no_even_numbers(self):
        self.assertEqual(even([]), [])
        self.assertEqual(even([1, 7, 111, 1987]), [])

    def test_returns_only_even_elements_from_list(self):
        some_numbers = [1, 202, 3, 4, 404]

        self.assertEqual(even(some_numbers), [202, 4, 404])

    def test_does_not_remove_duplicated_values(self):
        some_numbers = [202, 202, 3, 4, 4]

        self.assertEqual(even(some_numbers), [202, 202, 4, 4])

    def test_non_integer_elements_are_ignored(self):
        numbers_with_strings = [2, "4", 5, "hello", "world"]
        self.assertEqual(even(numbers_with_strings), [2])

        numbers_with_strings = [4, [30, 50], {"hello": "world", "2": 242}]
        self.assertEqual(even(numbers_with_strings), [4])


if __name__ == '__main__':
    unittest.main()
