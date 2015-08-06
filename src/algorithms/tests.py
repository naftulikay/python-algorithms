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

        # test worst case with 10 ints
        worst = [i for i in xrange(9, -1, -1)]

        algorithms.bubble_sort(worst)

        self.assertEqual([i for i in xrange(0, 10)], worst)

    
    def test_insertion_sort(self):
        """
        Tests the insertion sort algorithm implementation.
        """
        
        collection = [5, 1, 10, 2, 16, 1]

        algorithms.insertion_sort(collection)

        self.assertEqual(collection, [1, 1, 2, 5, 10, 16])

        # test worst case with 10 ints
        collection = [i for i in xrange(9, -1, -1)]

        algorithms.bubble_sort(collection)

        self.assertEqual([i for i in xrange(0, 10)], collection)

