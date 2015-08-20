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


    def test_assumption_crawl_forward(self):
        """
        Tests assumptions about the actual step requirements for an algorithm which nests loops.

        This test concerns cases like this:

            for i in xrange(0, n):
                for j in xrange(i + 1, n):
                    o(1)

        How many iterations total will be run for this equation? Conventional knowledge tells us that the mathematical
        formula for deriving this is:

            n * (n - 1)
            ———————————
                 2

        Or, in Python:

            (n * (n - 1)) / 2.0

        This test validates that assumption in code.
        """
        # define an iterate up approach
        def iterate_up(n):
            """
            For every value up to n (non-inclusive) as i, iterate upward from i + 1 to n (non-inclusive).
            """
            count = 0

            for i in xrange(0, n):
                for j in xrange(i + 1, n):
                    count += 1

            return count

        # define an iterate down approach, like insertion sort
        def iterate_down(n):
            """
            For every value up to n (non-inclusive) as i, iterate downward from i - 1 to 0 (inclusive).
            """
            count = 0

            for i in xrange(0, n):
                for j in reversed(xrange(0, i)): # remember that xrange is NON-INCLUSIVE, therefore we're going to i - 1
                    count += 1

            return count

        self.assertEqual((100 * (100 - 1)) / 2.0, iterate_up(100))
        self.assertEqual((1000 * (1000 - 1)) / 2.0, iterate_up(1000))

        self.assertEqual((100 * (100 - 1)) / 2.0, iterate_down(100))
        self.assertEqual((1000 * (1000 - 1)) / 2.0, iterate_down(1000))
