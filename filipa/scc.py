# encoding:utf-8
import collections
import sys

FINAL_NODE = 875715
t = 0
s = None
graph = collections.defaultdict(lambda: [])
reversed_graph = collections.defaultdict(lambda: [])
finish_order = []
sizes = []
reverse_explored = set()
explored = set()
finish_2 = []

def make_graphs():
    global graph, reversed_graph
    with open('SCC.txt') as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip().split(' ')
            # Adds nodes to graphs
            head = int(line[0])
            tail = int(line[1])
            graph[head].append(tail)
            reversed_graph[tail].append(head)


def dfs(graph, initial, is_reversed=False):
    explored.add(initial)
    for tail in graph[initial]:
        if tail not in explored:
            dfs(graph, tail, is_reversed)
    if is_reversed:
        #print 'appending to finishing times ', initial
        finish_order.append(initial)
    else:
        finish_2.append(initial)


def dfs_loop(graph, order, is_reversed=False):
    for it in order:
        if it not in explored:
            before = len(finish_2)
            dfs(graph, it, is_reversed)
            if not is_reversed:
                sizes.append(len(finish_2) - before)

def scc():
    dfs_loop(reversed_graph, reversed(xrange(1, FINAL_NODE)), True)
    global explored, finish_2
    explored = set()
    finish_2 = []
    dfs_loop(graph, reversed(finish_order))


if __name__ == '__main__':
    # Exercise 4
    sys.setrecursionlimit(27000)
    make_graphs()
    print len(graph), len(reversed_graph)
    scc()
    print 'number of sccs: ', len(sizes)
    sccs = sorted(sizes)
    sccs.reverse()
    print sccs[:10]
