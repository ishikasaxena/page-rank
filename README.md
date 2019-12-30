# page-rank
A Python implementation of the Page Rank algorithm with Markov Chains

## Key Terms
#### Directed Graph </br>
A directed graph is a collection of nodes and edges (the edges are the connections between the nodes, or objects). A web graph is a specific type of directed graph, in which the nodes are web pages and the edges are the hyperlinks between/on pages (ex: a hyperlink on an HTML web page represents this page linking to some other external page).

#### Adjacency Matrix for a Directed Graph
n x n matrix (n = number of nodes) where the A_ij entry is 1 if there's an edge from node j to node i and 0 otherwise.

#### Stochastic Matrix (i.e. Transition Matrix, Markov Matrix)
Describes the transitions from one state to another according to certain probabilistic tendencies. A_ij entry describes the transition of some input transitioning from its current state *j* to state *i*. Since the total transition probability from state j to all other states must equal 1, the columns sum to 1 in a stochastic matrix.

#### Markov Chains
A set of transitions that follow the Markov property i.e. the probability of transitioning to a particular state is entirely dependent on the current state rather than preceding states.

#### Steady State Vector (of a Stochastic Matrix)
The vector *x* such that A*x* = *x* (i.e. the vector that describes the convergence of probabilities). Displays the ranks of the pages by showing how the probabilities of some random walker converge.

#### Perron-Frobenius Theorem (from [here])
If M is a positive Markov matrix, then it has a unique maximum eigenvalue of 1, whose corresponding eigenvector has only positive values (this is the steady state vector). 

#### Dangling Node
A node that has no outgoing edges is a dangling node so no other state can be reached once this node is reached. Viewed as a column of zeros in the matrix representation of the web graph. This is amended by making each entry 1/n, where n is the number of nodes in the graph. This represents that the random walker, upon reaching this node, can travel to any node with equal probability.

#### Irreducible & Reducible Graphs
An irreducible graph is when any node is reachable from any other node following the links of the web graph. A reducible graph is the opposite: it has a set of nodes that have no out-links, causing the random walker to become stuck once it reaches any node part of this set.

#### Damping Matrix (also called the Google Matrix)
A matrix that accounts for the possibility of a reducible graph and remedies the situation by having a damping factor *d* that allows the random walker to move to any random node from its current node with probability *d* and, to account for reducibility, the walker surfs to a random page (from a set of "stuck" nodes) with probability *1-d*. </br>
Formula: Damping Matrix = *d*A + *1-d*Q  </br>
where A is a square stochastic matrix (altered for dangling nodes) and Q is a square matrix (with the same dimensions as A), with each entry as *1/n* (n = number of nodes).

## Web Graph from Test Case 1 from pageRank.py
<img width="352" alt="Screen Shot 2019-12-28 at 8 39 26 PM" src="https://user-images.githubusercontent.com/56605721/71570159-5f962c80-2aa1-11ea-88f6-00cfde82fcbf.png">

[here]:https://stanford.edu/class/ee363/lectures/pf.pdf
