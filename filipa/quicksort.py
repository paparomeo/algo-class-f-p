# encoding:utf-8

def first(array, l):
    try:
        return array[l]
    except IndexError:
        pass

def partition(array, l, r):
    pivot = first(array, l) 
    i = j = l + 1
    while j <= r:
        el = array[j]
        if el < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    
    # Put pivot in its place
    pp = i - 1
    if pp >= 1:
        array[l], array[pp] = array[pp], array[l]
        return l, pp - 1, i, r
    else:
        return l, l, i, r

def quicksort(array):
    """
    Implements the quick sort algorithm
    """
    def quick(array, l, r):
        n = r - l
        if n < 1:
            return array
        else:
            # Partition array
            ll, lr, rl, rr = partition(array, l, r)
            # Recurse on both sides
            quick(array, ll, lr)
            quick(array, rl, rr)
            return array

    # Prepares call to the recursive part
    n = len(array)
    return quick(array, 0, n - 1)
