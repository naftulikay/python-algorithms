#!/usr/bin/env python
# -*- coding: utf-8 -*-

def heap_parent(index):
    return int((index - 1) / 2)


def heap_left_child(index):
    return (index * 2) + 1


def heap_right_child(index):
    return (index * 2) + 2


def heapsort(data):
    # create heap property
    heapify(data)

    # start from the last element
    end = len(data) - 1

    # work until the second element (index 1)
    while end > 0:
        # swap the end element with the first element (the end element is the greatest element in the range)
        data[end], data[0] = data[0], data[end]
        # restrict our search space to not include the last element (which is "removed" from the heap)
        end -= 1
        # the head of the heap is likely in violation of the heap property, so sift down within the window
        heap_sift_down(data, 0, end)

    return data


def heapify(data):
    """Creates a max heap out of a list."""
    # start sifting down from the final parent in the list
    last = len(data) - 1
    index = heap_parent(last)

    while index >= 0:
        heap_sift_down(data, index, last)
        index -= 1

    return data


def heap_sift_down(data, start, end=None):
    """
    Sifts a max heap down in place.

    Args:
        data: list of comparable elements
        start: the index within data to sift down from.
        end: the last index to sift within, any elements after this index will not be sifted.
    """
    if end is None:
        end = len(data) - 1

    root = start

    while heap_left_child(root) <= end:
        left, right, swap = heap_left_child(root), heap_right_child(root), root

        if data[swap] < data[left]:
            swap = left

        # for some reason, right always wins here
        if right <= end and data[swap] < data[right]:
            swap = right

        if swap == root:
            return
        else:
            data[root], data[swap] = data[swap], data[root]
            root = swap

    return data

def heap_sift_up(data, index):
    """
    Fix the heap property by hoisting values upward, creating the heap property.
    """
    while index > 0:
        parent = heap_parent(index)

        if data[parent] < data[index]:
            data[index], data[parent] = data[parent], data[index]
            index = parent
        else:
            break
