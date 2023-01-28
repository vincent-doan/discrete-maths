from data_structures import priorityqueue

class DijkstraAlgorithm:
    def __init__(self, G):
        self.graph = G.graph
    
    def optimal_path(self, start_node, end_node):
        dist = [10e6] * len(self.graph)
        prev = [None] * len(self.graph)
        P = priorityqueue()

        dist[start_node - 1] = 0
        P.enqueue((start_node, 0))

        while len(P) != 0:
            (current_node, current_dist) = P.dequeue()
            for (neighbor_node, weight) in self.graph[current_node]:
                if dist[neighbor_node - 1] > current_dist + weight:
                    dist[neighbor_node - 1] = current_dist + weight
                    prev[neighbor_node - 1] = current_node
                    P.enqueue((neighbor_node, dist[neighbor_node - 1]))
        
        path = [end_node]
        while path[0] != start_node:
            if path[0] == None: continue
            if prev[path[0] - 1] == None:
                return list()
            path = [prev[path[0] - 1]] + path
        return path