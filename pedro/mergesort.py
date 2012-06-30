#!/usr/bin/env python3


def merge_gen(left, right):
    """
    Generate merged ordered values from two ordered iterables.
    """
    left_values = iter(left)
    right_values = iter(right)

    try:
        left = left_values.next()
    except StopIteration:
        while True:
            yield right_values.next()
    try:
        right = right_values.next()
    except StopIteration:
        while True:
            yield left_values.next()

    while True:
        if left < right:
            yield left
            try:
                left = left_values.next()
            except StopIteration:
                yield right
                while True:
                    yield right_values.next()
        else:
            yield right
            try:
                right = right_values.next()
            except StopIteration:
                yield left
                while True:
                    yield left_values.next()


def merge(left, right):
    return list(merge_gen(left, right))


def merge_sort(numbers):
    """
    Implement the (recursive) merge sort algorithm.
    """
    if len(numbers) <= 1:
        return numbers
    else:
        half = len(numbers) // 2
        return merge(merge_sort(numbers[:half]), merge_sort(numbers[half:]))
