#!/usr/bin/python3

class Graph(object):
    def __init__(self, nodes, previous, distances):
        self.nodes = nodes; 
        self.visited = set()
        self.distances = distances
        self.previous = previous


def main():
    """
        This is array representation of graph
        100 means no connection between nodes
        Other value is a weight
        This is undirected graph
    """
    nodes = [
        [100,3,100,100,3,6],
        [3,100,1,3,100,100],
        [100,1,100,3,100,1],
        [100,3,3,100,100,1],
        [3,100,100,100,100,2],
        [6,100,1,1,2,100],
    ]
    graph = Graph(nodes, [-1,-1,-1,-1,-1,-1], [0,100,100,100,100,100])
    for i in range(0, len(graph.nodes)):
        for j in range(0, len(graph.nodes[i])):
            if j in graph.visited or graph.nodes[i][j] == 100:
                continue
            print("From {i} to {j} is {w}".format(
                i=i,
                j=j,
                w=graph.nodes[i][j]
            ))
            if graph.distances[j] > graph.distances[i] + graph.nodes[i][j]:
                graph.distances[j] = graph.distances[i] + graph.nodes[i][j]
                graph.previous[j] = i
        graph.visited.add(i) 
    print(graph.distances)
    print(graph.previous)

if __name__ == "__main__":
    main()
