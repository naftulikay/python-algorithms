#!/usr/bin/env python
# -*- coding: utf-8 -*-

from algorithms.linkedlist import (
    DoublyLinkedList,
    LinkedList,
)

import unittest


class DoublyLinkedListTestCase(unittest.TestCase):

    def test_from_list(self):
        """Create a doubly linked list from a list."""
        data = [0, 1, 3, 5]

        self.assertEqual(data, [value for value in DoublyLinkedList.from_list(data).forward()])

    def test_forward(self):
        """Iterate over a doubly linked list forward."""
        data = [0, 1, 5, 3]
        ll = DoublyLinkedList()

        for i in data:
            ll.push(i)

        self.assertEqual(data, [value for value in ll.forward()])

    def test_backward(self):
        """Iterate over a doubly linked list backward."""
        data = [0, 1, 5, 3]
        ll = DoublyLinkedList()

        for i in data:
            ll.push(i)

        self.assertEqual(list(reversed(data)), [value for value in ll.backward()])

    def test_push(self):
        """Push an item into the doubly linked list."""
        ll = DoublyLinkedList()
        ll.push(5)

        # head and tail should be the same
        self.assertEqual(5, ll.head.value)
        self.assertEqual(5, ll.tail.value)
        # there aren't any values so things should be none
        self.assertIsNone(ll.head.next)
        self.assertIsNone(ll.tail.next)

        ll.push(7)

        # two elements
        self.assertEqual(5, ll.head.value)
        self.assertEqual(7, ll.head.next.value)
        self.assertEqual(7, ll.tail.value)
        self.assertEqual(5, ll.tail.prev.value)

        ll.push(9)

        # three elements
        self.assertEqual(5, ll.head.value)
        self.assertEqual(7, ll.head.next.value)
        self.assertEqual(9, ll.tail.value)
        self.assertEqual(7, ll.tail.prev.value)
        self.assertIsNone(ll.tail.next)
        self.assertIsNotNone(ll.head.next)

    def test_reverse(self):
        """Reverse a doubly linked list in place."""
        data = [1, 5, 7, 9]
        ll = DoublyLinkedList.from_list(data)
        ll.reverse()

        self.assertEqual(list(reversed(data)), [value for value in ll.forward()])


class LinkedListTestCase(unittest.TestCase):

    def test_from_list(self):
        """Create a singly linked list from a list."""
        data = [1, 5, 7, 9]
        result = LinkedList.from_list(data)

        self.assertEqual(list(reversed(data)), [value for value in result.forward()])

    def test_forward(self):
        """Iterate over a singly list list forward."""
        ll = LinkedList()

        for i in [1, 33, 7, 2]:
            ll.push(i)

        self.assertEqual([2, 7, 33, 1], list(ll.forward()))

    def test_push(self):
        """Push an item into the singly linked list."""
        ll = LinkedList()

        self.assertIsNone(ll.head)

        ll.push(7)

        self.assertIsNotNone(ll.head)
        self.assertIsNone(ll.head.next)
        self.assertEqual(7, ll.head.value)

        ll.push(9)

        self.assertIsNotNone(ll.head)
        self.assertIsNotNone(ll.head.next)
        self.assertEqual(9, ll.head.value)
        self.assertEqual(7, ll.head.next.value)

        ll.push(5)

        self.assertEqual(5, ll.head.value)
        self.assertEqual(9, ll.head.next.value)
        self.assertEqual(7, ll.head.next.next.value)

    def test_kth_from_end(self):
        """Fetch the kth from end value in a singly linked list."""
        ll = LinkedList.from_list([1, 2, 3, 4, 5])

        self.assertEqual(3, ll.kth_from_end(2))
        self.assertEqual(2, ll.kth_from_end(1))
        self.assertEqual(1, ll.kth_from_end(0))

    #  @unittest.skip
    def test_find_loop_start(self):
        """Find the start of a loop in a linked list."""
        head = LinkedList.Node(0)
        preamble0 = LinkedList.Node(1)
        preamble1 = LinkedList.Node(2)
        preamble2 = LinkedList.Node(3)

        ll = LinkedList()
        ll.head = head
        head.next, preamble0.next, preamble1.next = preamble0, preamble1, preamble2

        # build the loop
        loop0 = LinkedList.Node(4)
        loop1 = LinkedList.Node(5)
        loop2 = LinkedList.Node(6)
        loop3 = LinkedList.Node(7)
        loop4 = LinkedList.Node(8)
        loop5 = LinkedList.Node(9)
        loop6 = LinkedList.Node(10)
        loop7 = LinkedList.Node(11)

        # setup the loop
        preamble2.next = loop0
        loop0.next = loop1
        loop1.next = loop2
        loop2.next = loop3
        loop3.next = loop4
        loop4.next = loop5
        loop5.next = loop6
        loop6.next = loop7
        loop7.next = loop0

        self.assertEqual(loop0, ll.find_loop_start())

    def test_find_loop_no_prefix(self):
        """Find loop start for a zero prefix loop."""
        head = LinkedList.Node(0)
        l1 = LinkedList.Node(1)
        l2 = LinkedList.Node(2)

        ll = LinkedList()
        ll.head = head
        head.next = l1
        l1.next = l2
        l2.next = head

        self.assertEqual(head, ll.find_loop_start())

    def test_find_loop_start_noloop(self):
        """Find the nonexistent loop in a linked list."""
        self.assertIsNone(LinkedList.from_list([1, 2, 3]).find_loop_start())

