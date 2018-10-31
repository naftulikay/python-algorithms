#!/usr/bin/env python
# -*- coding: utf-8 -*-

def heap_left_child(index):
    return (index * 2) + 1


def heap_right_child(index):
    return (index * 2) + 2


def heap_parent(index):
    return int((index - 1) / 2)


def heapify_max_in_place(data):
    start = heap_parent(len(data) - 1)

    while start >= 0:
        heap_sift_down(data, start)

        start -= 1


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


def heap_sift_down(data, index, end=None):
    if end is None:
        end = len(data) -1

    while heap_left_child(index) <= end:
        left, right = heap_left_child(index), heap_right_child(index)

        if left < end and data[left] > data[index]:
            data[index], data[left] = data[left], data[index]
            index = left
            continue

        if right < end and data[right] > data[index]:
            data[index], data[right] = data[right], data[index]
            index = right
            continue

        break


def heapsort_in_place(data):
    heapify_max_in_place(data)

    for end in reversed(range(len(data))):
        data[0], data[end] = data[end], data[0]

        heap_sift_down(data, 0, end)

def heapsort(data):
    copy = [value for value in data]
    heapsort_in_place(copy)

    return copy
