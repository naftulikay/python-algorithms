#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.heapsort import (
        heapify_max_in_place,
        heapsort,
        heapsort_in_place,
)

from random import SystemRandom; random = SystemRandom()

import unittest


class HeapsortTestCase(unittest.TestCase):

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

    def test_heapsort_in_place(self):
        """Sort an arary in place using heapsort."""
        data = [int(random.random() * 100) for _ in range(100)]

        heapsort_in_place(data)

        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                self.fail("Array not in sorted order.")

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
