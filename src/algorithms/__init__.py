#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
    
def swap(collection, index1, index2):
    """
    Swaps the value of the item at index1 in the collection with the value of 
    index2 in the collection.
    """
    # get elements at positions
    first, second = collection[index1], collection[index2]
    
    # swap their positions
    collection[index1] = second
    collection[index2] = first


def bubble_sort(collection):
    """
    Uses the bubble sort algorithm to sort a collection.
    """
    # save time if you can
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
