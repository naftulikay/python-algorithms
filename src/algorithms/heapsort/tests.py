#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.heapsort import (
        heap_parent,
        heap_left_child,
        heap_right_child,
        heap_sift_down,
        heap_sift_up,
        heapify,
        heapsort,
)

import unittest


class HeapSortTestCase(unittest.TestCase):
    """Heap sort tests."""

    def test_heap_sift_up(self):
        """Sift up must move a value up the heap as long as a condition is met."""
        data = [0, 1, 2, 3, 4]
        heap_sift_up(data, 4)

        # index 4's parent is index 1, whose parent is index 0
        # first, index 4 is replaces index 1, so [0, 4, 2, 3, 1]
        # now, we are at index 1, which replaces index 0, so [4, 0, 2, 3, 1]
        self.assertEqual([4, 0, 2, 3, 1], data)

    def test_sift_down_limitless(self):
        # sifts here (note: the right child is always preferred in our example above)
        #   - start                (0, 1, 2, 3, 4, 5)
        #   - swap indices 0 and 2 (2, 1, 0, 3, 4, 5)
        #   - swap indices 2 and 5 (2, 1, 5, 3, 4, 0)
        self.assertEqual([2, 1, 5, 3, 4, 0], heap_sift_down([0, 1, 2, 3, 4, 5], 0))

    def test_sift_down_limited(self):
        # sifts here (note: the right child is always preferred in our example above)
        #   - start                (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...)
        #   - swap indices 0 and 2 (2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...)
        #   - swap indices 2 and 6 (2, 1, 6, 3, 4, 5, 0, 7, 8, 9, 10, 11, ...)
        self.assertEqual(
            [2, 1, 6, 3, 4, 5, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            heap_sift_down(list(range(16)), 0, 10),
        )

    def test_sift_down_start(self):
        # sifts here (note: the right child is always preferred in our example above)
        #   - start (index 3)      (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...)
        #   - swap indices 3 and 8 (0, 1, 2, 8, 4, 5, 6, 7, 3, 9, 10, 11, ...)
        self.assertEqual(
            [0, 1, 2, 8, 4, 5, 6, 7, 3, 9, 10, 11, 12, 13, 14, 15],
            heap_sift_down(list(range(16)), 3),
        )

    def test_heapify(self):
        data = heapify([2, 5, 3, 17, 8, 12])

        for start in reversed(range(len(data))):
            current = start
            # walk upward evaluating the heap property
            while current > 0:
                parent = heap_parent(current)
                self.assertGreaterEqual(data[parent], data[current],
                    "Heap property invalid at {:d} (parent {:d})".format(current, parent))

                current = parent

        # prove by implementation details
        # heapify(2, 5, 3, 17, 8, 12)
        #     heap_sift_down(data, 3)
        #         start: [2, 5, 3, 17, 8, 12]
        #
        self.assertEqual(
            [17, 8, 12, 5, 2, 3],
            data
        )

    def test_heapsort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], heapsort(list(reversed(range(6)))))

    def test_heap_left_child(self):
        self.assertEqual(1, heap_left_child(0))
        self.assertEqual(3, heap_left_child(1))

    def test_heap_right_child(self):
        self.assertEqual(2, heap_right_child(0))
        self.assertEqual(4, heap_right_child(1))

    def test_heap_parent(self):
        self.assertEqual(0, heap_parent(0))
        self.assertEqual(2, heap_parent(5))
        self.assertEqual(2, heap_parent(6))
