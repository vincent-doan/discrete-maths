#%%
from graph import *

#%%
G = WeightedDirectedGraph()
G.add_vertex([1,2,3,4,5])
G.add_edge([(1,2,8), (1,3,2), (2,4,4), (3,2,5), (3,4,4), (5,1,4), (5,3,3), (4,5,10), (2,5,6)])
G.show_graph()

#%%
G = UndirectedGraph()
G.add_vertex([1,2,3,4,5,6])
G.add_edge([(1,2), (1,3), (1,5), (4,2), (4,3), (4,5), (6,2), (6,3), (6,5)])
G.show_graph()

#%%
G = UndirectedGraph()
G.add_vertex([1,2,3,4,5,6,7,8])
G.add_edge([(1,2), (1,3), (1,5), (2,4), (2,6), (3,4), (3,6), (3,7), (4,5), (4,8), (5,6), (5,7), (6,8), (7,8)])
G.show_graph()

#%%
G = DirectedGraph()
G.add_vertex([1,2,3,4,5,6])
G.add_edge([(1,2), (2,3), (2,4), (3,5), (3,6), (4,1), (5,2), (5,6), (6,4)])
G.show_graph()

#%%
G = WeightedDirectedGraph()
G.add_vertex([1,2,3,4,5,6,7,8])
G.add_edge([(1,2,8), (1,3,2), (1,8,7), (2,7,5), (3,2,5), (3,4,4), (5,1,4), (5,3,3), (4,5,10), (2,5,6), (8,3,6), (6,7,8), (7,4,7), (8,7,6), (6,2,4)])
G.show_graph()

#%%