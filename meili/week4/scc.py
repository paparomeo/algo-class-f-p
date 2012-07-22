

def get_SCC(Gr, n):
	labeling = range(len(Gr))
	finish, _  = DFSLoop(Gr, labeling)
	G = ReverseGraph(Gr)
	del Gr
	print "graph reversed"
	finish, sizes = DFSLoop(G, finish)
	i = 0
	for s in sizes:
		print finish[i:i+s]
		i += s
	
	sizes.sort()
	return sizes[-n:]
	
def ReverseGraph(G):
	G_r = [set([]) for i in range(len(G))]
	for i, edjes in enumerate(G):
		for v in edjes:
			G_r[v].add(i)
	return G_r


def DFSLoop(G, labeling):
	visited = set([])
	sizes = []
	finish = []
	for n in reversed(labeling):
		if n not in visited:
			before = len(finish)
			DFS(G, n, visited, finish)
			sizes.append(len(finish) - before)
	return finish, sizes

			
def DFS(G, n, visited, finish):
	visited.add(n)
	for j in G[n]:
		if j not in visited:
			DFS(G,j,visited,finish)
	finish.append(n)
			
if __name__ == '__main__':
	N = 875714
	import sys
	sys.setrecursionlimit(N)
	#N = 9
	# To avoide segmentation fault, increase stack size
	# ulimit -s <new_limit>
	# Solution:
	#434821,968,459,313,211
	G = [set([]) for i in xrange(N)]
	#with open('SCC_test.txt') as fp:
	with open('SCC.txt') as fp:
		for line in fp:
			tail, head = map(int,line.strip().split())
			#G[tail-1].add(head-1)
			G[head-1].add(tail-1)
	print "graph initialised"
	print get_SCC(G,5)
