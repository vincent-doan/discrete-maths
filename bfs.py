from data_structures import queue

class BreadthFirstSearch:
    def __init__(self, G):
        self.graph = G.graph
        self.V = G.V
        self.E = G.E
    
    def graph_traversal(self, start_node):
        visited = list()
        Q = queue()
        Q.enqueue(start_node)
        while len(Q) != 0:
            current_node = Q.dequeue()
            for neighbor_node in self.graph[current_node]:
                if neighbor_node in Q.queue or neighbor_node in visited:
                    continue
                Q.enqueue(neighbor_node)
            visited.append(current_node)
        return visited

    def shortest_path(self, start_node, end_node):
        prev = [None] * len(self.V)
        prev[start_node - 1] = 'null'
        
        visited = list()
        Q = queue()
        Q.enqueue(start_node)
        while len(Q) != 0:
            current_node = Q.dequeue()
            for neighbor_node in self.graph[current_node]:
                if neighbor_node in Q.queue or neighbor_node in visited:
                    continue
                Q.enqueue(neighbor_node)
                prev[neighbor_node - 1] = current_node
            visited.append(current_node)
        
        path = [end_node]
        while path[0] != start_node:
            if path[0] == 'null': continue
            if prev[path[0] - 1] == None:
                return list()
            path = [prev[path[0] - 1]] + path
        return path
    
    def count_connected_components(self):
        id = [0] * len(self.V)
        count = 0
        for start_node in self.V:
            if id[start_node - 1] != 0: continue
            count += 1
            visited = list()
            Q = queue()
            Q.enqueue(start_node)
            id[start_node - 1] = count
            while len(Q) != 0:
                current_node = Q.dequeue()
                for neighbor_node in self.graph[current_node]:
                    if neighbor_node in Q.queue or neighbor_node in visited:
                        continue
                    Q.enqueue(neighbor_node)
                    id[neighbor_node - 1] = count
                visited.append(current_node)
        print(id)
        return count