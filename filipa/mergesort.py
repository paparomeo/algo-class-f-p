# encoding:utf-8

def merge(a, b):
    n = len(a)
    res = []
    i = j = k = 0
    while k < n * 2:
        if i == n:
            res.extend(b[j:])
            break
        if j == n:
            res.extend(a[i:])
            break
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
        k += 1
    return res

def mergesort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        # Split array into two
        a = array[: n / 2]
        b = array[n / 2:]
        sorted_a = mergesort(a)
        sorted_b = mergesort(b)
        return merge(sorted_a, sorted_b)

