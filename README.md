# discrete-maths

## preliminaries
**data_structures.py** contains classes of data structures: queue, stack, priority queue<br>
**graph.py** contains classes of graphs: (un)directed (un)weighted graphs; weighted graphs have corresponding unweighted graphs as getable attributes; .show_graph() uses *networkx* to draw graphs

## algorithms
**bfs.py** contains class BreadthFirstSearch: graph_traversal & shortest_path<br>
**dfs.py** contains class DepthFirstSearch: graph_traversal & path<br>
**dijkstra.py** contains class DijkstraAlgorithm: optimal_path<br>
**hamilton.py** contains class UnweightedHamilton: enumerate_hamilton_paths & enumerate_hamilton_cycles (using ***backtracking***); contains class WeightedHamilton: enumerate_hamilton_weighted_paths & enumerate_hamilton_weighted_cycles & optimal_hamilton_weighted_path & optimal_hamilton_weighted_cycle (using ***branch-and-bound***)

## running
**sample-graphs.py** contains examples of readily-used graphs<br>
**test.py** contains script for drawing graphs and running algorithms
