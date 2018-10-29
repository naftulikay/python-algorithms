#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cakethief(cakes, capacity: int):
    max_values_at_capacities = [0] * (capacity + 1)

    # for every possible capacity up to the actual capacity
    for current_capacity in range(capacity + 1):
        # determine the max monetary value that can be held at the current capacity
        current_max_value = 0

        for cake_weight, cake_price in cakes:
            if cake_weight == 0 and cake_price != 0:
                return float('inf')

            # find only cakes that are within the current capacity
            if cake_weight <= current_capacity:
                # by iteratively finding the maximum value available for each capacity (build up), we can find the
                # counterpart to this cake. by finding the maximum possible value for a capacity of 1, then finding
                # the maximum possible value for a capacity of 2, etc. we will have built the maximum possible capacity
                # at every possible capacity leading up to and building to the actual capacity
                max_value_using_cake = cake_price + max_values_at_capacities[current_capacity - cake_weight]

                # if this cake yields the greatest value for this capacity, store it
                current_max_value = max(current_max_value, max_value_using_cake)

        max_values_at_capacities[current_capacity] = current_max_value

    # now that we've bult every possible capacity up to and including the target capacity, we now have our answer
    return max_values_at_capacities[capacity]
