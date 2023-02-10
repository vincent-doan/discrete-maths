# discrete-maths

## preliminaries
**data_structures.py**<br>
### contains classes of data structures:<br>
- queue<br>
- stack<br>
- priority queue<br>
**graph.py**<br>
### contains classes of graphs:<br>
- undirected unweighted graphs<br>
- directed unweighted graphs<br>
- undirected weighted graphs<br>
- directed weighted graphs<br>
### each type of graph contains:<br>
- add_vertex(V:list)<br>
- add_egde(E:list)<br>
- show_graph() uses *networkx* to draw graphs<br>
- (weighted graphs) get_unweighted_graphs()<br>

## algorithms
**bfs.py**<br>
### contains class BreadthFirstSearch:<br>
- graph_traversal(start_node)<br>
- shortest_path(start_node, end_node)<br>
- count_connected_components()<br>
**dfs.py**<br>
### contains class DepthFirstSearch:<br>
- graph_traversal(start_node)<br>
- path(start_node, end_node)<br>
- get_timestamp()<br>
- get_tree_edges()<br>
- detect_cycle()<br>
**dijkstra.py** 
### contains class DijkstraAlgorithm:<br>
- optimal_path(start_node, end_node)<br>
**hamilton.py** 
### contains class UnweightedHamilton:<br>
- enumerate_hamilton_paths()<br>
- enumerate_hamilton_cycles(start_node) (using ***backtracking***)<br>
### contains class WeightedHamilton:<br>
- enumerate_hamilton_weighted_paths()<br>
- enumerate_hamilton_weighted_cycles(start_node)<br>
- optimal_hamilton_weighted_path() (using ***branch-and-bound***)<br>
- optimal_hamilton_weighted_cycle(start_node) (using ***branch-and-bound***)<br>

## running
**sample-graphs.py** contains examples of readily-used graphs<br>
**test.py** contains script for drawing graphs and running algorithms
