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
    connecting_nodes = graph[node_label]
    graph[node_label] = filter(lambda a: a != node_label, 
                               connecting_nodes)


def karger(graph):
    """
    Implements the karger algorithm for finding a minimum cut
    """
    # Stop if number of nodes is 2
    if len(graph) == 2:
        return graph

    # Chose a random edge
    node_label = random.choice(graph.keys())

    # Contract the graph

    # Remove self loops
    remove_self_loops(graph, node_label)

    # Calls again the algorithm
    #karger(graph)


if __name__ == '__main__':
    # Exercise 3
    graph = make_graph()
    karger(graph)
