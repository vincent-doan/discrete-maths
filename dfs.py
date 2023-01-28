from data_structures import stack

class DepthFirstSearch:
    def __init__(self, G):
        self.graph = G.graph
    
    def graph_traversal(self, start_node):
        found = [False] * len(self.graph)
        visited = list()
        
        def dfs(start_node):
            if found[start_node - 1] == True:
                return
            found[start_node - 1] = True
            visited.append(start_node)
            for neighbor_node in self.graph[start_node]:
                dfs(neighbor_node)
        
        dfs(start_node)
        return visited
    
    def path(self, start_node, end_node):
        found = [False] * len(self.graph)
        prev = [None] * len(self.graph)
        
        def dfs(start_node):
            if found[start_node - 1] == True:
                return
            found[start_node - 1] = True
            for neighbor_node in self.graph[start_node]:
                if prev[neighbor_node - 1] == None:
                    prev[neighbor_node - 1] = start_node
                dfs(neighbor_node)
        
        dfs(start_node)
        
        path = [end_node]
        while path[0] != start_node:
            if path[0] == None: continue
            if prev[path[0] - 1] == None:
                return list()
            path = [prev[path[0] - 1]] + path
        return path