# encoding:utf-8

def merge_and_count(left, right):
    inv = left[1] + right[1]
    left = left[0]
    right = right[0]
    n_left = len(left)
    n_right = len(right)
    res = []
    i = j = 0
    while True:
        if i == n_left:
            res.extend(right[j:])
            break
        if j == n_right:
            res.extend(left[i:])
            break
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            inv += len(left) - i
    return res, inv

def mergesort(array):
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        # Split array into two
        half = n / 2
        left = array[:half]
        right = array[half:]
        sorted_left = mergesort(left)
        sorted_right = mergesort(right)
        return merge_and_count(sorted_left, sorted_right)
