#!/usr/bin/env python3


def merge_and_count_inv((left_inversions, left), (right_inversions, right)):
    """
    Merge values from two ordered sequences and count the split inversions.
    """
    # check trivial cases where at least one of the sequences is empty.
    if not left:
        return (right_inversions, right)
    if not right:
        return (left_inversions, left)

    # initialise merged result list, indexes and lengths for left and right
    # sequences and inversions counter
    merged = []
    left_index = 0
    right_index = 0
    left_length = len(left)
    right_length = len(right)
    inversions = left_inversions + right_inversions

    # merge until one of the sub-sequences is empty
    while left_index < left_length and right_index < right_length:
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            inversions += left_length - left_index

    # append the remaining of the non-empty sub-sequence
    if left_index < left_length:
        merged.extend(left[left_index:])
    else:
        merged.extend(right[right_index:])

    return (inversions, merged)


def sort_and_count_inv(numbers):
    """
    Implement the (recursive) merge sort algorithm.
    """
    if len(numbers) <= 1:
        return (0, numbers)
    else:
        half = len(numbers) // 2
        return merge_and_count_inv(sort_and_count_inv(numbers[:half]),
                                   sort_and_count_inv(numbers[half:]))

if __name__ == '__main__':
    with open('IntegerArray.txt') as array_file:
        numbers = [int(number.strip()) for number in array_file.readlines()]
    print(sort_and_count_inv(numbers)[0])
