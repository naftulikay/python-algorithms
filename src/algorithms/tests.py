#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import algorithms
import unittest


class AlgorithmsTestCase(unittest.TestCase):
    """
    Test cases for algorithm compatibility.
    """

    def test_bubble_sort(self):
        """
        Tests the bubble sort algorithm implementation.
        """

        collection = [5, 1, 10, 2, 16, 1]

        algorithms.bubble_sort(collection)

        # first, test that it actually worked and sorted the collection in place
        self.assertEqual(collection, [1, 1, 2, 5, 10, 16])

        # test that it works in the worst case scenario
        collection = [5, 4, 3, 2, 1]

        algorithms.bubble_sort(collection)

        self.assertEqual(collection, [1, 2, 3, 4, 5])

        # test that it works with strings
        collection = ['c', 'a', 'b']

        algorithms.bubble_sort(collection)

        self.assertEqual(collection, ['a', 'b', 'c'])
