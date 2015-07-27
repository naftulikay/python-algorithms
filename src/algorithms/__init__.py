#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


def bubble_sort(collection):
    """
    Uses the bubble sort algorithm to sort a collection.
    """
    touched_something = True

    while touched_something:
        touched_something = False

        for i in range(len(collection)):
            j = i + 1

            # if we're outside of the range, break out
            if j >= len(collection):
                break

            # do comparison and swap
            a, b = collection[i], collection[j]

            if a > b:
                # swap places
                collection[i] = b
                collection[j] = a
                touched_something = True
