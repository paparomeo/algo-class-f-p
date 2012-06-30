# encoding:utf-8

def partition(array, pivot):
    i = j = 1
    while j < len(array):
        el = array[j]
        if el < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    # Put pivot in its place
    pivot_place = i - 1
    array[0], array[pivot_place] = array[pivot_place], array[0]
    return array[:pivot_place], array[i:]

def quicksort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        # Choose a pivot
        pivot = array[0]
        # Partition array around pivot
        left, right = partition(array, pivot)
        print left, right, array
        # Recurse on both sides
        quicksort(left)
        quicksort(right)

    return array
