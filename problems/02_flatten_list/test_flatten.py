import unittest

from flatten import flatten


class FlatteningAListTest(unittest.TestCase):
    def test_does_not_change_a_flattened_list(self):
        flat_list = [1, 2, 3, 4]

        self.assertEqual(flatten(flat_list), flat_list)

    def test_does_not_flatten_list_by_default(self):
        list_to_flatten = [1, 2, 3, [1, 2, 3]]

        self.assertEqual(flatten(list_to_flatten), list_to_flatten)

    def test_does_not_remove_duplicated_elements(self):
        list_to_flatten = [1, 2, 3, [1, 2, 3]]

        self.assertEqual(flatten(list_to_flatten, 1), [1, 2, 3, 1, 2, 3])

    def test_allows_to_specify_the_maximum_flattening_depth(self):
        list_to_flatten = [1, [2, 3], [[[1], 2], 3]]

        self.assertEqual(flatten(list_to_flatten, 1), [1, 2, 3, [[1], 2], 3])
        self.assertEqual(flatten(list_to_flatten, 2), [1, 2, 3, [1], 2, 3])
        self.assertEqual(flatten(list_to_flatten, 3), [1, 2, 3, 1, 2, 3])
        self.assertEqual(flatten(list_to_flatten, 4), [1, 2, 3, 1, 2, 3])

    def test_does_not_impact_other_collection_types(self):
        list_to_flatten = [1, {2, 3}, ([[1], 2], 3), "test string"]

        self.assertEqual(flatten(list_to_flatten, 1), list_to_flatten)

    def test_raises_an_error_if_the_specified_depth_is_invalid(self):
        with self.assertRaises(Exception):
            flatten([2], -3)

        with self.assertRaises(Exception):
            flatten([2], "something")


if __name__ == '__main__':
    unittest.main()
