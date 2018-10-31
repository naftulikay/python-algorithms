#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.heapsort import (
        heap_sift_down,
        heap_sift_up,
        heapify_max_in_place,
        heapsort,
        heapsort_in_place,
)

from random import SystemRandom; random = SystemRandom()

import unittest


class HeapsortTestCase(unittest.TestCase):

    def test_heap_sift_up(self):
        """Sift up must move a value up the heap as long as a condition is met."""
        data = [0, 1, 2, 3, 4]
        heap_sift_up(data, 4)

        # index 4's parent is index 1, whose parent is index 0
        # first, index 4 is replaces index 1, so [0, 4, 2, 3, 1]
        # now, we are at index 1, which replaces index 0, so [4, 0, 2, 3, 1]
        self.assertEqual([4, 0, 2, 3, 1], data)

    def test_heap_sift_down(self):
        """Sift down must correct the heap property downward with an upper bound for the last index."""
        data = [0, 1, 2, 3, 4]
        # sift down with no upper bound
        heap_sift_down(data, 1)

        # data[1] (1), left child data[3] (3), swap to: [0, 3, 1, 2, 1, 4]
        self.assertEqual([0, 3, 2, 1, 4], data)

    def test_heap_sift_down_limit(self):
        """Sift down with an explicit end cap."""
        data = [0, 1, 2, 3, 4, 5]
        # sift down with an explicit upper bound
        heap_sift_down(data, 0, 2)

        # data[0] (1), left child data[1] (1)
        self.assertEqual([1, 0, 2, 3, 4, 5], data)

    def test_heapify_max_in_place(self):
        """Create a max heap in-place in an array."""
        data = [int(random.random() * 100) for _ in range(100)]

        heapify_max_in_place(data)

        for i in reversed(range(len(data))):
            parent_i = int((i - 1) / 2)
            value, parent = data[i], data[parent_i]

            if value > parent:
                self.fail("Heap property does not hold (index: {}, parent_index: {}), value: {}, parent: {}".format(
                    i, parent_i, value, parent))

    @unittest.skip
    def test_heapsort_in_place_random(self):
        """Sort a randomized array in place using heapsort."""
        data = [int(random.random() * 100) for _ in range(100)]

        heapsort_in_place(data)

        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                self.fail("Array not in sorted order.")

    @unittest.skip
    def test_heapsort_in_place(self):
        """Sort an array in place using heapsort."""
        data = [10, 9, 7, 6, 2, 1]

        heapsort_in_place(data)

        self.assertEqual([1, 2, 6, 7, 9, 10], data)

    @unittest.skip
    def test_heapsort(self):
        """Sort an array without side-effects using heapsort."""
        data = [int(random.random() * 100) for _ in range(100)]
        copy = [value for value in data]

        result = heapsort(data)

        for i in range(1, len(result)):
            if result[i - 1] > result[i]:
                self.fail("Array not in sorted order.")

        for i, value in enumerate(data):
            if data[i] != copy[i]:
                self.fail("Array destroyed.")
