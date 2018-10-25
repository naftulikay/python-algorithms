#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import algorithms
import logging
import unittest

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('algorithms.tests')

class AlgorithmsTestCase(unittest.TestCase):
    """
    Test cases for algorithm compatibility.
    """

    def test_swap(self):
        """Tests that the swap method swaps indices in-place in a collection."""
        # test simple forward swap
        collection = [4, 3]
        algorithms.swap(collection, 1, 0)
        self.assertEqual([3, 4], collection)

        # test reverse swap
        collection = [10, 5]
        algorithms.swap(collection, 0, 1)
        self.assertEqual([5, 10], collection)

        # test big difference swap
        collection = [i for i in range(0, 100)]
        algorithms.swap(collection, 95, 5)

        expected = [i for i in range(0, 100)]
        expected[95] = 5
        expected[5] = 95

        self.assertEqual(expected, collection)

        # test out of bounds
        collection = [i for i in range(0, 10)]

        try:
            algorithms.swap(collection, 3, 100)
            self.fail("the algorithm failed to raise an IndexError on out of bounds access")
        except IndexError as e:
            logger.debug("successfully threw error: %s", e)

        # test negative indices
        collection = [0, 1, 2]
        algorithms.swap(collection, -1, -2)
        self.assertEqual([0, 2, 1], collection)

        # test negative indices out of bounds
        collection = [i for i in range(0, 10)]

        try:
            algorithms.swap(collection, -1, -11)
            self.fail("the algorithm failed to raise an IndexError on negative out of bounds")
        except IndexError as e:
            logger.debug("successfully threw error: %s", e)


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
        worst = [i for i in range(9, -1, -1)]

        algorithms.bubble_sort(worst)

        self.assertEqual([i for i in range(0, 10)], worst)


    def test_insertion_sort(self):
        """
        Tests the insertion sort algorithm implementation.
        """
        collection = [5, 1, 10, 2, 16, 1]

        algorithms.insertion_sort(collection)

        self.assertEqual(collection, [1, 1, 2, 5, 10, 16])

        # test worst case with 10 ints
        collection = [i for i in range(9, -1, -1)]

        algorithms.bubble_sort(collection)

        self.assertEqual([i for i in range(0, 10)], collection)


    def test_heap_sort(self):
        """
        Tests the heap sort algorithm implementation.
        """
        # test random case
        collection = [5, 1, 10, 2, 16, 1]

        algorithms.heap_sort(collection)

        self.assertEqual([1, 1, 2, 5, 10, 16], collection)

        # test worst case
        collection = [i for i in reversed(range(0, 10))]

        algorithms.heap_sort(collection)

        self.assertEqual([i for i in range(0, 10)], collection)

        # test a huge array worst case
        collection = [i for i in reversed(range(0, 1000))]
        algorithms.heap_sort(collection)
        self.assertEqual([i for i in range(0, 1000)], collection)

    @unittest.skip("not implemented")
    def test_heapify(self):
        """
        Tests the heapify algorithm implementation.
        """
        self.fail("not implemented")

    @unittest.skip("not implemented")
    def test_heap_sift_down(self):
        """
        Tests that sifting down a heapified collection works as planned.
        """
        self.fail("not implemented")


class MathTestCase(unittest.TestCase):
    """
    Test case for math formulae, comparing them with actual results.
    """


    def test_assumption_crawl_forward(self):
        """
        Tests assumptions about the actual step requirements for an algorithm which nests loops.

        This test concerns cases like this:

            for i in range(0, n):
                for j in range(i + 1, n):
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

            for i in range(0, n):
                for j in range(i + 1, n):
                    count += 1

            return count

        # define an iterate down approach, like insertion sort
        def iterate_down(n):
            """
            For every value up to n (non-inclusive) as i, iterate downward from i - 1 to 0 (inclusive).
            """
            count = 0

            for i in range(0, n):
                for j in reversed(range(0, i)): # remember that range is NON-INCLUSIVE, therefore we're going to i - 1
                    count += 1

            return count

        self.assertEqual((100 * (100 - 1)) / 2.0, iterate_up(100))
        self.assertEqual((1000 * (1000 - 1)) / 2.0, iterate_up(1000))

        self.assertEqual((100 * (100 - 1)) / 2.0, iterate_down(100))
        self.assertEqual((1000 * (1000 - 1)) / 2.0, iterate_down(1000))
