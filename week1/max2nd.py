import math
comparisons = 0

def tournament(lst):
	global comparisons
	if len(lst) == 1:
		return lst[0], []
	
	w1, loosers1 = tournament(lst[:len(lst)/2])
	w2, loosers2 = tournament(lst[len(lst)/2:])
	comparisons +=1
	if w1>w2:
		
		return w1, loosers1 + [w2]
	return w2 , loosers2 + [w1]

def max2ndfast(lst):
"""
Find 2nd maximum, with n + logn - 2 comparisons
"""
	w, loosers = tournament(lst)
	second, looosers = tournament(loosers)
	return second

def max2nd(lst):
"""
Find 2nd maximum, divide and conquer with 3n/2 comparisons
"""
	global comparisons
	if len(lst) == 2:
		comparisons +=1
		if lst[0]>lst[1]:
			return lst
		return lst[1], lst[0]
		
	l1, l2 = max2nd(lst[:int(len(lst)/2)])
	r1, r2 = max2nd(lst[int(len(lst)/2):])
	comparisons +=2
	if l1 > r1:
		if l2 > r1:
			return l1, l2
		else:
			return l1, r1
	else:
		if l1 > r2:
			return r1, l1
		else:
			return r1, r2

lst = range(1024)			
print max2ndfast(lst)
print comparisons
print 3*len(lst)/2 -2
print len(lst) + math.log(len(lst),2) - 2
