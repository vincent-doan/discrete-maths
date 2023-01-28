#%%
from graph import *
from dijkstra import *
from bfs import *
from dfs import *
from hamilton import *

#%%
G = WeightedUndirectedGraph()
G.add_vertex([1,2,3,4,5,6,7,8])
G.add_edge([(1,2,8), (1,3,2), (1,8,7), (2,7,5), (3,2,5), (3,4,4), (5,1,4), (5,3,3), (4,5,10), (2,5,6), (8,3,6), (6,7,8), (7,4,7), (8,7,6), (6,2,4)])
G.show_graph()

#%%
UH = UnweightedHamilton(G.get_unweighted_graph())
UH.enumerate_hamilton_cycles(1)

#%%
WH = WeightedHamilton(G)
WH.enumerate_hamilton_weighted_cycles(1)
WH.optimal_hamilton_weighted_cycle(1)

#%%
DA = DijkstraAlgorithm(G)
DA.optimal_path(4,8)

#%%
DFS = DepthFirstSearch(G.get_unweighted_graph())
DFS.path(1,8)

#%%