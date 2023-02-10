from graph import *

class KruskalAlgorithm:
    def __init__(self, G):
        self.graph = G.graph
        self.V = G.V
        self.E = G.E
        self.mininum_spanning_tree = WeightedUndirectedGraph()
    
    def show_minimum_spanning_tree(self):
        pass