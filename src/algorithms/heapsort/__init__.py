#!/usr/bin/env python
# -*- coding: utf-8 -*-

def heapify_max_in_place(data):
    for i in range(len(data)):
        current_i = i

        while current_i > 0:
            parent_i = int((current_i - 1) / 2)

            if data[parent_i] < data[current_i]:
                data[current_i], data[parent_i] = data[parent_i], data[current_i]
                current_i = parent_i
            else:
                break


def heapsort_in_place(data):
    heapify_max_in_place(data)

    for end in reversed(range(len(data))):
        # pop the head off of the heap
        head, current_i = data[0], end

        while current_i < end:
            left_child_i, right_child_i = (current_i * 2) + 1, (current_i * 2) + 2
            left_child, right_child = data[left_child_i], data[right_child_i]

            if left_child >= right_child:
                # prefer the left child
                data[current_i], data[left_child_i] = data[left_child_i], data[current_i]
            else:
                # prefer the right child
                data[current_i], data[right_child_i] = data[right_child_i], data[current_i]

        data[end] = head


def heapsort(data):
    copy = [value for value in data]
    heapsort_in_place(copy)

    return copy
