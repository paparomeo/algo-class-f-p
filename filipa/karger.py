# encoding:utf-8
import random


def make_graph():
    graph = {}
    with open('kargerMinCut.txt') as f:
        for i, line in enumerate(f.readlines()):
            nodes = line.strip().split('\t')
            # Adds nodes to graph
            graph[nodes[0]] = nodes[1:]
    return graph


def remove_self_loops(graph, node_label):
    """
    Remove edges from any node to itself
    """
    graph[node_label] = filter(lambda a: a != node_label, 
                               graph[node_label])


def karger(graph):
    """
    Implements the karger algorithm for finding a minimum cut
    """
    # Stop if number of nodes is 2
    if len(graph) == 2:
        for node in graph:
            print len(graph[node])
            return

    # Chose a random edge
    node_label = random.choice(graph.keys())

    # Contract the graph
    node_label2 = graph[node_label][0]
    # Removes the node that will eat this one 
    # from connections. All occurences
    graph[node_label] = filter(lambda a: a != node_label2,
                               graph[node_label])
    # Removes the node to disapear from the second
    # All occurences
    graph[node_label2] = filter(lambda a: a != node_label,
                                graph[node_label2])
    # Adds the connections of the first to the second
    graph[node_label2].extend(graph[node_label])
    
    # Changes first node into second node in all other nodes
    for node in graph:
        if node_label in graph[node]:
            graph[node] = [x if x != node_label else node_label2 for x in graph[node]]
    
    # Removes the first node
    del graph[node_label]
                            
    # Calls again the algorithm
    karger(graph)


if __name__ == '__main__':
    # Exercise 3
    i = 0
    while i < 200 ** 2:
        graph = make_graph()
        n = len(graph)
        karger(graph)
        i += 1
