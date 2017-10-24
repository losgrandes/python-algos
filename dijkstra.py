#!/usr/bin/python3

import queue

class Graph(object):
    def __init__(self, nodes, previous, distances):
        self.nodes = nodes; 
        self.visited = set()
        self.distances = distances
        self.previous = previous

    def standard(self, target):
        """ Standard Dijkstra's algo. No queue used. """
        print("Looking for shortest path from 0 to {}".format(target))
        iterations = 0
        for i in range(0, len(self.nodes)):
            if target in self.visited:
                break
            for j in range(0, len(self.nodes[i])):
                if j in self.visited or self.nodes[i][j] == 100:
                    continue
                print("From {i} to {j} distance is {w}".format(
                    i=i,
                    j=j,
                    w=self.nodes[i][j]
                ))
                if self.distances[j] > self.distances[i] + self.nodes[i][j]:
                    self.distances[j] = self.distances[i] + self.nodes[i][j]
                    self.previous[j] = i
                iterations += 1
            self.visited.add(i)
        print("Iterations made: {}".format(iterations))

    def priority_queue(self, target):
        """ Dijkstra's algo with priority queue. """
        print("Looking for shortest path from 0 to {}".format(target))
        iterations = 0
        q = queue.PriorityQueue()
        q.put((0,0))
        while(not q.empty() and target not in self.visited):
            node = q.get()
            node_id = node[1]
            node_dist = node[0]
            for j in range(0, len(self.nodes[node_id])):
                if j in self.visited or self.nodes[node_id][j] == 100:
                    continue
                print("From {i} to {j} distance is {w}".format(
                    i=node_id,
                    j=j,
                    w=self.nodes[node_id][j]
                ))
                if self.distances[j] > self.distances[node_id] + self.nodes[node_id][j]:
                    self.distances[j] = self.distances[node_id] + self.nodes[node_id][j]
                    self.previous[j] = node_id
                    q.put((self.distances[j],j))
                iterations += 1
            self.visited.add(node_id)

        print("Iterations made: {}".format(iterations))

    def print_result(self, target):
        prev = [target]
        current = target
        while(0 not in prev):
            prev.insert(0, self.previous[current])
            current = self.previous[current]
        path = " -> ".join(str(x) for x in prev)
        print("""
        Shortest distance from point 0 to {point} is {distance}.
        Path is {path}
        """.format(
            point=target, distance=self.distances[target], path=path
        ))



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
    target = 3
    graph = Graph(nodes, [-1,-1,-1,-1,-1,-1], [0,100,100,100,100,100])
    print("Linear approach")
    graph.standard(target)
    graph.print_result(target)
    graph = Graph(nodes, [-1,-1,-1,-1,-1,-1], [0,100,100,100,100,100])
    print("Priority queue approach")
    graph.priority_queue(target)
    graph.print_result(target)

if __name__ == "__main__":
    main()
