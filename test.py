#%%
from graph import *
from dijkstra import *
from bfs import *
from dfs import *
from hamilton import *

#%%
G = UndirectedGraph()
G.add_vertex([1,2])
G.add_edge([(1,2)])
G.show_graph()

#%%
DFS = DepthFirstSearch(G)
print(DFS.get_tree_edges())
print(DFS.detect_cycle())

#%%