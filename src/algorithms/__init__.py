#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from math import floor, ceil


def swap(collection, index1, index2):
    """
    Swaps the value of the item at index1 in the collection with the value of
    index2 in the collection.
    """
    n = len(collection)

    # if we're reaching outside of bounds, throw an error which describes it better
    if index1 >= n or index2 >= n:
        raise IndexError("Unable to swap indices that are out of bounds. (list size: %d, index 1: %d, index2: %d)" % (
            n, index1, index2
        ))

    # if index1 == index2, there's nothing to do
    if index1 == index2:
        return

    # get elements at positions
    first, second = collection[index1], collection[index2]

    # swap their positions
    collection[index1] = second
    collection[index2] = first


def bubble_sort(collection):
    """
    Uses the bubble sort algorithm to sort a collection.

    Complexity: best case Ω(1), worst case O(n²)
    """
    # save time if you can, Ω(1)
    if len(collection) <= 1:
        return

    touched_something = True

    while touched_something: # < could be replaced by do-while
        touched_something = False

        for i in range(len(collection)):
            j = i + 1

            # if we're outside of the range, break out
            if j >= len(collection):
                break

            # do comparison and swap
            if collection[i] > collection[j]:
                swap(collection, i, j)
                touched_something = True


def insertion_sort(collection):
    """
    Uses the insertion sort algorithm to sort a collection.

    Complexity: best case Ω(1), worst case O(n²)

    Amount of maximum worst-case iterations is expressed with the following formula:

        n(n - 1)
        ————————
            2

    Eliminating constants, we derive O(n²) iterations.
    """
    # save time if you can
    if len(collection) <= 1:
        return

    # iterate from the second to the last elements in this array
    for i in range(1, len(collection)): # second parameter is non-inclusive
        j = i

        # for each master loop, search downward, provided that the previous
        while j > 0 and collection[j - 1] > collection[j]:
            # j-1 is greater than j because of loop condition
            swap(collection, j - 1, j)

            # decrement j
            j = j - 1


def heap_sort(collection):
    """
    Uses the heap sort algorithm to sort a collection.

    Complexity: best case Ω(n), worst case O(n log n)
    """
    n = len(collection)

    # if there's nothing to sort, leave
    if n <= 1:
        return

    # build the heap data structure in-place in the collection using the heapify method so that the
    # largest value is at index 0
    heapify(collection)

    # now that we have a heap data structure in-place in the collection, iterate backwards through
    # the collection, sorting based on the properties of a heap
    for i in reversed(xrange(0, n)):
        # index 0 is the largest value, swap it in front of the sorted elements.
        swap(collection, i, 0)
        # the swap broke the heap property, so fix it using a sift down.
        # (the sift down will only happen up to i - 1, which matches the algorithm description)
        heap_sift_down(collection, 0, i)


def heap_sift_down(collection, start, n = None):
    """
    Sifts down a collection which is desired to be in a heap format.

    Arguments:
    collection: The heapified collection to sift down.
    start: The start index to begin the sift from.
    n: The maximum non-inclusive limit of how far to go into the collection. If not provided, it defaults
       to the length of the collection.
    """
    if n is None:
        n = len(collection)

    # the root we're going to sift down is the value of start
    root = start

    # while our root has an opposite that isn't out of bounds
    while (root * 2) + 1 < n:
        left = (root * 2) + 1 # left child
        right = left + 1 # right child is located one further than the left
        destination = root # where we'd like to put the current root

        # if left child is greater than the root (which is the current destination)
        if collection[left] > collection[destination]:
            destination = left

        # if there is a right child and that child is greater than the destination
        # (which might be the root) and in bounds, of course
        if right < n and collection[right] > collection[destination]:
            destination = right

        # if the destination is still the root, we're done sifting down
        if destination == root:
            return

        # otherwise, perform our swap and change the root
        swap(collection, root, destination)

        # set the root to the destination and continue
        root = destination


def heapify(collection):
    """
    Converts a collection of sortable items into a heap.

    The heap
    """
    n = len(collection)

    # select the 'middleish' point in the collection as our starting point
    middle = floor((n - 2) / 2.0)

    # iterate from the middle of the array downward to zero
    for i in reversed(xrange(0, int(middle + 1))): # non inclusive, so go one further!
        # repair the heap whose root is at i. we assume that the heaps rooted at its children are
        # valid.
        heap_sift_down(collection, i)
