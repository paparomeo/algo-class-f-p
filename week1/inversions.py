def cntinversions(lst):
	if len(lst) <= 1:
		return 0, lst
	middle = int(len(lst)/2)
	left, llst = cntinversions(lst[:middle])
	right, rlst = cntinversions(lst[middle:])
	i = 0 
	j = 0
	splitinv = 0
	while (i+j) < len(lst):
		if i>=len(llst):
			lst[i+j] = rlst[j]
			j+=1
		elif j>=len(rlst):
			lst[i+j] = llst[i]
			i+=1
		elif llst[i]<rlst[j]:
			lst[i+j] = llst[i]
			i+=1
		else:
			lst[i+j] = rlst[j]
			j+=1
			splitinv+= len(llst) - i
	return left + right + splitinv , lst

with open('IntegerArray.txt') as fp:
	lst = [int(num) for num in fp]
invs, slst = cntinversions(lst)		
print invs
print len(lst)
print slst == range(1,len(lst)+1)
