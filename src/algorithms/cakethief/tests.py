#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.cakethief import cakethief

import unittest


class CakeThiefTestCase(unittest.TestCase):
    """Tests for the cake thief interview problem."""

    def test_one_cake(self):
        self.assertEqual(4, cakethief([(2, 1)], 9))

    def test_two_cakes(self):
        self.assertEqual(9, cakethief([(4, 4), (5, 5)], 9))

    def test_only_take_less_valuable_cake(self):
        self.assertEqual(12, cakethief([(4, 4,), (5, 5)], 12))

    def test_lots_of_cakes(self):
        self.assertEqual(12, cakethief([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7))

    def test_value_to_weight_not_optimal(self):
        self.assertEqual(100, cakethief([(51, 52), (50, 50)], 100))

    def test_zero_capacity(self):
        self.assertEqual(0, cakethief([(1, 2)], 0))

    def test_cake_with_zero_value_and_weight(self):
        self.assertEqual(3, cakethief([(0, 0), (2, 1)], 7))

    def test_infinite_cakes(self):
        self.assertEqual(float('inf'), cakethief([(0, 5)], 5))
