comparisons = 0

def quicksort(lst):
    return qs(lst, 0, len(lst)-1)

def qs(lst, start, end):
    if end - start< 1:
        return lst
    pivot = partition(lst, start, end)
    qs(lst, start, pivot-1)
    qs(lst, pivot+1, end)
    return lst

def get_pivot(lst, start, end):
    return get_pivot_3median(lst, start, end)
    #return get_pivot_start(lst, start, end)

def get_pivot_start(lst, start, end):
    return start

def get_pivot_end(lst, start, end):
    return end

def get_pivot_3median(lst, start, end):
    middle = (end - start)/2 + start
    ordered = sorted([(lst[end], end), (lst[middle], middle),
        (lst[start], start)])
    median = ordered[1][1]
    return median


def partition(lst, start, end):
    global comparisons
    comparisons+= end - start
    i = start + 1
    pivot = get_pivot(lst, start, end)
    lst[pivot], lst[start] = lst[start], lst[pivot]
    for k in range(start+1,end+1):
        if lst[k] < lst[start]:
            lst[k], lst[i] = lst[i], lst[k]
            i+=1
    lst[start], lst[i-1] = lst[i-1], lst[start]
    return i-1


with open('QuickSort.txt') as fp:
    a = [int(i) for i in fp]
b = sorted(a)
#print "Sorted: ", b
assert a!=b
quicksort(a)
#print "QuickSort: ", a
assert a == b
print comparisons
