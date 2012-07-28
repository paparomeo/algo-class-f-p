# encoding:utf-8
import collections


FINAL_NODE = 875714
t = 0
s = None
graph = None
reversed_graph = None
finishing_times = []
leaders = {}


def make_graphs():
    global graph, reversed_graph
    # defaultdict allows the value of the key to be something
    graph = collections.defaultdict(lambda: {'explored': False, 'arcs': []})
    reversed_graph = collections.defaultdict(lambda: {'explored': False, 'arcs': []})
    with open('SCC.txt') as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip().split(' ')
            # Adds nodes to graph
            graph[line[0]]['arcs'].append(line[1])
            reversed_graph[line[1]]['arcs'].append(line[0])


def dfs_loop_reversed():
    print 'dfs loop reversed'
    global reversed_graph

    def dfs(initial):
        global t, s, finishing_times, reversed_graph
        head = reversed_graph[initial]
        # Mark head as explored
        head['explored'] = True
        print 'reversed graph head: ', head
        for tail in head['arcs']:
            if not reversed_graph[tail]['explored']:
                dfs(tail)
            else:
                t += 1
                finishing_times.append((t, tail))
                print 'appending to finishing times'

    i = FINAL_NODE
    while i > 0:
        node = str(i)
        print 'analising node ', node, reversed_graph[node]
        if not reversed_graph[node]['explored']:
            dfs(node)
        i -= 1


def dfs_loop():
    print 'dfs loop'
    global s, graph

    def dfs(initial):
        global s, graph
        head = graph[initial]
        # Mark head as explored
        head['explored'] = True
        for tail in head['arcs']:
            if not graph[tail]['explored']:
                dfs(tail)
            else:
                leaders.append((s, tail))
                print 'appending to leaders'

    order = order_finishing_times()
    for it in order:
        node = it[1]
        if not graph[node]['explored']:
            s = node
            dfs(node)


def order_finishing_times():
    print finishing_times[:10]
    sorted_finishing_times = sorted(finishing_times)
    return sorted_finishing_times.reverse()


def scc():
    """
    Implements the strongly connected components algorithm
    """
    dfs_loop_reversed()
    dfs_loop()


def find_sccs(graph):
    leaders = [node['leader'] for node in graph]
    collections.Counter(leaders)


if __name__ == '__main__':
    # Exercise 4
    make_graphs()
    print len(graph), len(reversed_graph)
    scc()
    find_sccs(graph)
