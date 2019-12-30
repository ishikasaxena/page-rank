# page-rank
A Python implementation of the Page Rank algorithm with Markov Chains

## Key Terms
#### Directed Graph </br>
A directed graph is a collection of nodes and edges (the edges are the connections between the nodes, or objects). A web graph is a specific type of directed graph, in which the nodes are web pages and the edges are the hyperlinks between/on pages (ex: a hyperlink on an HTML web page represents this page linking to some other external page).

#### Adjacency Matrix for a Directed Graph
n x n matrix (n = number of nodes) where the A_ij entry is 1 if there's an edge from node j to node i and 0 otherwise.

#### Stochastic Matrix (i.e. Transition Matrix, Markov Matrix)
Describes the transitions form one state to another according to certain probabilistic tendencies. A_ij entry describes some 
