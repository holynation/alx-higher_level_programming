#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """ command for test: python3 -m unittest -v tests.6-max_integer_test"""

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([10, -10, 10]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([{1, 9}, {2}, {3}]), {1, 9})
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.5, -2.5]), -1.5)

    def test_list_of_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'x', 'y', 'z']), 'z')
        self.assertEqual(max_integer(["abc", 'x']), 'x')
        self.assertEqual(max_integer("6789"), '9')
        self.assertEqual(max_integer("abcxyz"), 'z')

    def test_lists(self):
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_other_samples(self):
        with self.assertRaises(TypeError):
            max_integer({10, 21, 31, 41, 51})
        with self.assertRaises(TypeError):
            max_integer([-9, 0.7, "int", {2, 6}])
        with self.assertRaises(TypeError):
            max_integer({2, 4}, {6, 8, 9})
        with self.assertRaises(TypeError):
            max_integer([True, None])

    def test_None(self):
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([]), None)

if __name__ == "__main__":
    unittest.main()
