class UnweightedHamilton:
    def __init__(self, G):
        self.graph = G.graph
    
    def enumerate_hamilton_paths(self):
        n = len(self.graph)
        path = [0] * n
        def Try(i):
            if i == 0:
                for v in sorted(self.graph.keys()):
                    path[i] = v
                    Try(i+1)
            elif i != 0:
                for v in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    if i == n-1:
                        print(path)
                    else:
                        Try(i+1)
        Try(0)

    def enumerate_hamilton_cycles(self, start_node):
        n = len(self.graph)
        path = [start_node] + [0] * (n-1)
        def Try(i):
            if i == 0:
                Try(i+1)
            elif i != 0:
                for v in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    if i == n-1 and start_node in self.graph[path[n-1]]:
                        cycle = path[:] 
                        cycle = cycle + [path[0]]
                        print(cycle)
                    elif i < n-1:
                        Try(i+1)
                    else:
                        return
        Try(0)

class WeightedHamilton:
    def __init__(self, G):
        self.graph = G.graph # dictionary: key = int (node), value = list of tuples (node, weight)

    def enumerate_hamilton_weighted_paths(self): # backtracking
        n = len(self.graph)
        path = [0] * n # global mutable variable, accessed throughout recursive run
        cumulative_dist = [0] * n 
        def Try(i):
            if i == 0:
                for v in sorted(self.graph.keys()):
                    path[i] = v
                    Try(i+1)
            elif i != 0:
                for (v, w) in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    cumulative_dist[i] = cumulative_dist[i-1] + w
                    if i == n-1:
                        print(path,end='')
                        print(" - Cost: " + str(cumulative_dist[-1]))
                    else:
                        Try(i+1)
        Try(0)

    def enumerate_hamilton_weighted_cycles(self, start_node): # backtracking
        n = len(self.graph)
        path = [start_node] + [0] * (n-1)
        cumulative_dist = [0] * n
        def Try(i):
            if i == 0:
                Try(i+1)
            elif i != 0:
                for (v, w) in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    cumulative_dist[i] = cumulative_dist[i-1] + w
                    if i == n-1:
                        accepted = False
                        for (node, weight) in self.graph[path[n-1]]:
                            if node == start_node:
                                accepted = True
                                cycle = path[:]
                                cycle = cycle + [start_node]
                                print(cycle,end='')
                                print(" - Cost: " + str(cumulative_dist[-1] + weight))
                        if not accepted:
                            return
                    else:
                        Try(i+1)
        Try(0)
    
    def optimal_hamilton_weighted_path(self): # branch and bound
        n = len(self.graph) 
        # compute min_weight
        min_weight = None
        for node in self.graph:
            for (_, weight) in self.graph[node]:
                if min_weight == None or min_weight > weight:
                    min_weight = weight
        # initialization
        path = [0] * n
        cumulative_dist = [0] * n
        current_optimal_path = []
        current_optimal_dist = [10e6]
        
        def Try(i):
            if i == 0:
                for v in sorted(self.graph.keys()):
                    path[i] = v
                    Try(i+1)
            elif i != 0:
                for (v, w) in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    cumulative_dist[i] = cumulative_dist[i-1] + w
                    g = cumulative_dist[i] + (n-i-1)*min_weight
                    if g > current_optimal_dist[-1]:
                        return 
                    if i == n-1:
                        if cumulative_dist[-1] < current_optimal_dist[-1]:
                            current_optimal_path.append(path[:])
                            current_optimal_dist.append(cumulative_dist[-1])
                    else:
                        Try(i+1)
        
        Try(0)
        return (current_optimal_path[-1], current_optimal_dist[-1])
    
    def optimal_hamilton_weighted_cycle(self, start_node): # branch and bound
        n = len(self.graph)
        # compute min_weight
        min_weight = None
        for node in self.graph:
            for (_, weight) in self.graph[node]:
                if min_weight == None or min_weight > weight:
                    min_weight = weight
        # initialization
        path = [start_node] + [0] * (n-1)
        cumulative_dist = [0] * n
        current_optimal_cycle = []
        current_optimal_dist = [10e6]
        
        def Try(i):
            if i == 0:
                Try(i+1)
            elif i != 0:
                for (v, w) in self.graph[path[i-1]]:
                    if v in path[:i]:
                        continue
                    path[i] = v
                    cumulative_dist[i] = cumulative_dist[i-1] + w
                    g = cumulative_dist[i] + (n-i)*min_weight
                    if g > current_optimal_dist[-1]:
                        return
                    if i == n-1:
                        accepted = False
                        for (node, weight) in self.graph[path[n-1]]:
                            if node == start_node:
                                accepted = True
                                cycle = path[:]
                                cycle = cycle + [start_node]
                                if cumulative_dist[-1] + weight < current_optimal_dist[-1]:
                                    current_optimal_cycle.append(cycle)
                                    current_optimal_dist.append(cumulative_dist[-1] + weight)
                        if not accepted:
                            return
                    else:
                        Try(i+1)
        
        Try(0)
        return (current_optimal_cycle[-1], current_optimal_dist[-1])