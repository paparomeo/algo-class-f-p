#!/usr/bin/env python3


def merge(left, right):
    """
    Generate merged ordered values from two ordered sequences.
    """
    # check trivial cases where at least one of the sequences is empty.
    if not left:
        return right
    if not right:
        return left

    # initialise merged result list and indexes for left and right sequences
    merged = []
    left_index = 0
    right_index = 0
    left_length = len(left)
    right_length = len(right)

    # merge until one of the sub-sequences is empty
    while left_index < left_length and right_index < right_length:
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # append the remaining of the non-empty sub-sequence
    if left_index < left_length:
        merged.extend(left[left_index:])
    else:
        merged.extend(right[right_index:])

    return merged


def merge_sort(numbers):
    """
    Implement the (recursive) merge sort algorithm.
    """
    if len(numbers) <= 1:
        return numbers
    else:
        half = len(numbers) // 2
        return merge(merge_sort(numbers[:half]), merge_sort(numbers[half:]))
