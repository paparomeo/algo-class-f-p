import random
import copy
import itertools



graph = [[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]]

def rc_mincut(V):
    """
    :param V: adjacency list graph format. List of lists,
              in each position of the initial list there
               is a list of adjancent nodes
    Returns number of crossing edges in computed cut.
    """
    Vcurrent = [dict(zip(neighbours,itertools.repeat(1))) for neighbours in copy.deepcopy(V)]

    # groupings are the nodes contractions
    # When two nodes are contracted, the one
    # node group is updated with destination and append to the other
    groupings = [set([i]) for i in range(len(V))]
    remaining = set(range(len(V)))
    while len(remaining) > 2:
        #v1 = remaining.pop()
        v1 = random.sample(remaining, 1)[0]
        #print "Choosing %s"  % v1 ,
        #remaining.remove(v1)
        v2 = random.sample(Vcurrent[v1].keys(), 1)[0]
        #print " with %s" % v2

        while v2 not in remaining:
            # v2 is merged already, it will contain only one node
            v2new = groupings[v2].pop()
            groupings[v2].add(v2new) # do i need it?
            v2 = v2new
        remaining.remove(v2)
        groupings[v1] |= groupings[v2] # union of sets
        groupings[v2] = set([v1])
        #remaining.add(v1)

        for node in Vcurrent[v2]: # added edges of merged node
            Vcurrent[v1].setdefault(node, 0)
            Vcurrent[v1][node] += Vcurrent[v2][node]

        for node in groupings[v1]:
            if Vcurrent[v1].get(node):
                del Vcurrent[v1][node] # delete self loops

    p1 = remaining.pop()
    p2 = remaining.pop()
    if sum(Vcurrent[p1].values())  != sum(Vcurrent[p2].values()):
        print "Error"
        print p1, p2
        print Vcurrent
        print groupings
    return sum(Vcurrent[p2].values())

graph = []
with open('kargerMinCut.txt') as fp:
    for line in fp:
        graph.append([int(el)-1 for el in line.split()[1:]])
print min([rc_mincut(graph) for i in range(80000)])

"""
Benchmark @i5 8GB ram
>time python mincut.py 17

real    17m26.473s
user    16m45.610s
sys 0m36.260s
"""
