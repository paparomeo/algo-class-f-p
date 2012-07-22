# dijkstraData.txt
def dikstra(G, s):
	MAX_VAL = 1000000
	visited = set([s])
	frontier = set([])
	A = [MAX_VAL for i in range(len(G))]
	A[s]=0
	
	for v, length in G[s]:
		frontier.add(v)
		A[v] = length
	# initialise shortest paths
	
	while len(visited)!=len(G) and frontier:
		length, end = min([(A[el],el) for el in frontier])
		#print "========="
		#print "Choose node %s" %(end)
		#print "visited %s" %(visited)
		#print "frontier %s" %frontier
		#print " neihbours %s" %G[end] 
		visited.add(end)
		frontier.remove(end)
		for v, lenv in G[end]:
			if v not in visited:
	#			print "Updating node %s: from %s to %s" %(v, A[v], min(A[v], A[end]+lenv)) 
				A[v] = min(A[v], A[end]+lenv)
				frontier.add(v)
	return A
	
G = []
with open('dijkstraData.txt') as fp:
	for line in fp:
		nums = line.strip().split()
		G.append([map(int,el.split(',')) for el in nums[1:]])
		for i in range(len(G[-1])):
			G[-1][i][0]-=1  # fix index to start from 0
			G[-1][i] = tuple(G[-1][i])
#print G
indexes_of_interest = [el-1 for el in (7,37,59,82,99,115,133,165,188,197)]
 
shortest_paths = dikstra(G,0)
print ','.join(map(str,[shortest_paths[indx] for indx in indexes_of_interest]))