class Graph:
    
    def __init__(self):
        self.graph = dict()
        self.V = list() # vertex list
        self.E = list() # edge list
    
    def __str__(self):
        res = ''
        for vertex in self.graph:
            res += str(vertex) + ' ' + str(self.graph[vertex]) + '\n'

class UndirectedGraph(Graph):
    
    def add_vertex(self, V: list):
        for vertex in V:
            if vertex in self.graph:
                print(vertex, 'is already an existing vertex.')
            else:
                self.graph[vertex] = list()
                self.V.append(vertex)
    
    def add_edge(self, E: list):
        for (first_endpoint, second_endpoint) in E:
            if first_endpoint not in self.graph:
                print(first_endpoint, 'is not an existing vertex.')
            elif second_endpoint not in self.graph:
                print(second_endpoint, 'is not an existing vertex.')
            elif second_endpoint in self.graph[first_endpoint]:
                print(str((first_endpoint, second_endpoint)) + ' is already an existing edge.')
            elif first_endpoint in self.graph[second_endpoint]:
                print(str((first_endpoint, second_endpoint)) + ' is already an existing edge.')
            else:
                self.graph[first_endpoint].append(second_endpoint)
                self.graph[first_endpoint].sort()
                self.graph[second_endpoint].append(first_endpoint)
                self.graph[second_endpoint].sort()
                self.E.append((first_endpoint, second_endpoint))
                self.E.append((second_endpoint, first_endpoint))

    def show_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        
        lines = []
        for vertex in sorted(self.graph.keys()):
            lines.append(str(vertex) + ' ' + ' '.join(list(map(str, self.graph[vertex]))))
        
        G = nx.parse_adjlist(lines, nodetype=int)
        pos = nx.spring_layout(G, seed=9)
        nx.draw_networkx(G, pos, with_labels=True)
        plt.show()

class DirectedGraph(Graph):

    def add_vertex(self, V: list):
        for vertex in V:
            if vertex in self.graph:
                print(vertex, 'is already an existing vertex.')
            else:
                self.graph[vertex] = list()
                self.V.append(vertex)
    
    def add_edge(self, E: list):
        self.E.extend(E)
        for (initial, terminal) in E:
            if initial not in self.graph:
                print(initial, 'is not an existing vertex.')
            elif terminal not in self.graph:
                print(terminal, 'is not an existing vertex.')
            elif terminal in self.graph[initial]:
                print(str((initial, terminal)) + ' is already an existing edge.')
            else:
                self.graph[initial].append(terminal)
                self.graph[initial].sort()
                self.E.append((initial, terminal))
    
    def show_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        
        lines = []
        for vertex in sorted(self.graph.keys()):
            lines.append(str(vertex) + ' ' + ' '.join(list(map(str, self.graph[vertex]))))
        
        G = nx.parse_adjlist(lines, create_using=nx.DiGraph, nodetype=int)
        pos = nx.spring_layout(G, seed=9)
        nx.draw_networkx(G, pos, arrows=True, with_labels=True)
        plt.show()

class WeightedDirectedGraph(Graph):
    
    def __init__(self):
        self.graph = dict()
        self.unweighted_graph = DirectedGraph()
        self.V = list() # vertex list
        self.E = list() # edge list
    
    def add_vertex(self, V: list):
        for vertex in V:
            if vertex in self.graph:
                print(vertex, 'is already an existing vertex.')
            else:
                self.graph[vertex] = list()
                self.V.append(vertex)
    
    def add_edge(self, E: list):
        for (initial, terminal, weight) in E:
            if initial not in self.graph:
                print(initial, 'is not an existing vertex.')
            elif terminal not in self.graph:
                print(terminal, 'is not an existing vertex.')
            elif terminal in self.graph[initial]:
                print(str((initial, terminal)) + ' is already an existing edge.')
            else:
                self.graph[initial].append((terminal, weight))
                self.graph[initial].sort()
                self.E.append((initial, terminal, weight))
    
    def show_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        
        lines = []
        for initial in sorted(self.graph.keys()):
            for (terminal, weight) in self.graph[initial]:
                lines.append(str(initial) + ' ' + str(terminal) + ' ' + str(weight))
        
        G = nx.parse_edgelist(lines, create_using=nx.DiGraph, nodetype=int, data=(("weight", float),))
        pos = nx.spring_layout(G, seed=9)
        nx.draw_networkx(G, pos, arrows=True, with_labels=True)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.show()
    
    def get_unweighted_graph(self):
        V = [v for v in self.graph.keys()]
        self.unweighted_graph.add_vertex(V)
        
        E = list()
        for initial in self.graph:
            for (terminal, _) in self.graph[initial]:
                E.append((initial, terminal))
        self.unweighted_graph.add_edge(E)

        return self.unweighted_graph

class WeightedUndirectedGraph(Graph):

    def __init__(self):
        self.graph = dict()
        self.unweighted_graph = UndirectedGraph()
        self.V = list() # vertex list
        self.E = list() # edge list

    def add_vertex(self, V: list):
        for vertex in V:
            if vertex in self.graph:
                print(vertex, 'is already an existing vertex.')
            else:
                self.graph[vertex] = list()
                self.V.append(vertex)
    
    def add_edge(self, E: list):
        for (first_endpoint, second_endpoint, weight) in E:
            if first_endpoint not in self.graph:
                print(first_endpoint, 'is not an existing vertex.')
            elif second_endpoint not in self.graph:
                print(second_endpoint, 'is not an existing vertex.')
            elif second_endpoint in self.graph[first_endpoint]:
                print(str((first_endpoint, second_endpoint)) + ' is already an existing edge.')
            elif first_endpoint in self.graph[second_endpoint]:
                print(str((first_endpoint, second_endpoint)) + ' is already an existing edge.')
            else:
                self.graph[first_endpoint].append((second_endpoint, weight))
                self.graph[first_endpoint].sort()
                self.graph[second_endpoint].append((first_endpoint, weight))
                self.graph[second_endpoint].sort()
                self.E.append((first_endpoint, second_endpoint, weight))
                self.E.append((second_endpoint, first_endpoint, weight))
    
    def show_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        
        lines = []
        for initial in sorted(self.graph.keys()):
            for (terminal, weight) in self.graph[initial]:
                lines.append(str(initial) + ' ' + str(terminal) + ' ' + str(weight))
        
        G = nx.parse_edgelist(lines, nodetype=int, data=(("weight", float),))
        pos = nx.spring_layout(G, seed=9)
        nx.draw_networkx(G, pos, with_labels=True)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.show()
    
    def get_unweighted_graph(self):
        V = [v for v in self.graph.keys()]
        self.unweighted_graph.add_vertex(V)
        
        E = list()
        for first_endpoint in self.graph:
            for (second_endpoint, _) in self.graph[first_endpoint]:
                if(second_endpoint, first_endpoint) in E:
                    continue
                E.append((first_endpoint, second_endpoint))
        self.unweighted_graph.add_edge(E)

        return self.unweighted_graph