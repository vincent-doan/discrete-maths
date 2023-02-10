from data_structures import stack

class DepthFirstSearch:
    def __init__(self, G):
        self.graph = G.graph
        self.V = G.V
        self.E = G.E
    
    def graph_traversal(self, start_node):
        found = [False] * len(self.V)
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
        found = [False] * len(self.V)
        prev = [None] * len(self.V)
        
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
    
    def get_timestamp(self):
        found = [False] * len(self.V)
        time = [0]
        d = [0] * len(self.V)
        f = [0] * len(self.V)
        
        def dfs(start_node):
            if found[start_node - 1] == True:
                return
            time[0] = time[0] + 1
            found[start_node - 1] = True
            d[start_node - 1] = time[0]
            
            for neighbor_node in self.graph[start_node]:
                dfs(neighbor_node)
            time[0] = time[0] + 1
            f[start_node - 1] = time[0]
        
        for node in self.V:
            dfs(node)
        
        timestamp = dict()
        for i in range(len(self.V)):
            timestamp[i+1] = list(zip(d,f))[i]
        return timestamp
    
    def get_tree_edges(self):
        tree_edges = list()
        found = [False] * len(self.V)
        
        def dfs(start_node):
            if found[start_node - 1] == True:
                return False
            found[start_node - 1] = True
            
            for neighbor_node in self.graph[start_node]:
                if dfs(neighbor_node):
                    tree_edges.append((start_node, neighbor_node))
            return True
        
        for node in self.V:
            dfs(node)
        return tree_edges

    def detect_cycle(self):

        def is_subset(i1, i2):
            return (i1[0] >= i2[0]) and (i1[1] <= i2[1])
        
        timestamp = self.get_timestamp()
        tree_edges = self.get_tree_edges()
        reversed_tree_edges = [(y,x) for (x,y) in tree_edges]

        for edge in self.E:
            if edge in tree_edges or edge in reversed_tree_edges: continue
            interval_initial = timestamp[edge[0]]
            interval_terminal = timestamp[edge[1]]
            if is_subset(interval_initial, interval_terminal):
                return True
        
        return False