#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import getLogger

logger = getLogger('linkedlist')

class DoublyLinkedList(object):

    class Node(object):

        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next, self.prev = next, prev

    @classmethod
    def from_list(cls, data):
        result = cls()

        for value in data:
            result.push(value)

        return result


    def __init__(self):
        self.head, self.tail = None, None

    def push(self, value):
        node = self.Node(value)

        if not self.head:
            self.head = node

        if not self.tail:
            self.tail = node

        if self.tail != node:
            self.tail.next, node.prev = node, self.tail
            self.tail = node

    def forward(self):
        node = self.head

        while node:
            yield node.value

            node = node.next

    def backward(self):
        node = self.tail

        while node:
            yield node.value

            node = node.prev

    def reverse(self):
        node = self.head

        while node:
            node.next, node.prev = node.prev, node.next
            node = node.prev

        self.head, self.tail = self.tail, self.head


class LinkedList(object):

    class Node(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __repr__(self):
            return "LinkedList.Node[{:02d}]".format(self.value)

    @classmethod
    def from_list(cls, data):
        result = LinkedList()

        for value in data:
            result.push(value)

        return result

    def __init__(self):
        self.head = None

    def forward(self):
        node = self.head

        while node:
            yield node.value

            node = node.next

    def push(self, value):
        self.head = self.Node(value, self.head)

    def push_node(self, node):
        self.head, node.next = node, self.head

    def kth_from_end(self, k):
        list_length = 0
        node = self.head

        while node:
            list_length += 1
            node = node.next

        if k >= list_length:
            raise IndexError("k is larger than the size of the linked list.")

        k_index = (list_length - 1) - k
        current_index = 0
        node = self.head

        while current_index < k_index:
            node = node.next
            current_index += 1

        return node.value

    def find_loop_start(self):
        # it is critical that they start at the _exact same place_
        slow, fast = self.head, self.head

        while fast and fast.next:
            logger.debug("slow={:02d}, fast={:02d}, loop_start=4".format(slow.value, fast.value))

            # advance slow by one, fast by two
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                # when we have the meeting point, break out of the loop
                break

        if not fast or not fast.next:
            # no loop exists
            return None

        # reset slow to the beginning of the list
        slow = self.head

        while slow != fast:
            # advance both by one until we collide, the collision point will be the start of the loop
            slow = slow.next
            fast = fast.next

        return slow
