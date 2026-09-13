#!/usr/bin/env python3

import unittest
from unittest.mock import patch

from src.find_matching import find_matching


class TestFindMatching(unittest.TestCase):

    def test_worked_example(self):
        words = ["sensitive", "engine", "rubbish", "comment"]
        result = find_matching(words, "en")
        self.assertIsInstance(
            result, list,
            msg=f"find_matching should return a list. Got {type(result)}.")
        self.assertEqual(
            result, [0, 1, 3],
            msg="find_matching(%s, 'en') should return [0, 1, 3]: "
            "'sensitive' (0), 'engine' (1) and 'comment' (3) contain 'en', "
            "'rubbish' (2) does not." % (words,))

    def test_uses_enumerate(self):
        words = ["sensitive", "engine", "rubbish", "comment"]
        with patch('builtins.enumerate',
                   return_value=enumerate(words)) as mock_enumerate:
            find_matching(words, "en")
            mock_enumerate.assert_called_once()

    def test_empty_list(self):
        result = find_matching([], "en")
        self.assertEqual(
            result, [],
            msg="find_matching([], 'en') should return an empty list, "
            "since an empty list cannot contain any matches!")

    def test_no_matches(self):
        result = find_matching(["apple", "banana"], "xyz")
        self.assertEqual(
            result, [],
            msg="find_matching(['apple', 'banana'], 'xyz') should return "
            "an empty list: neither word contains the pattern 'xyz'.")


if __name__ == '__main__':
    unittest.main()
