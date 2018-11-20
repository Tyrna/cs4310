Program must run using: Python3.

The following program solves the stablished Equalizing problem in n^3 time.

The premise of my solution consists of:

> Start from the Source Vertex (The starting vertex of the path we are trying to find the smoothest)
> Consider all edges from the Source Vertex and ADD all Vertices directly connected to the Source into a list.
> Within the same list, ADD the ratios from going from the Source to said Vertex (speed/speed).
> For all the vertices added on the list, consider all edges that lead to a vertex that eventually leads to the Source vertex. We MUST do this twice in order to truly find all paths that lead to Source.
> Add the ratios of said paths to the initial vertex that discovered said paths, and for edges that lead to vertices that does NOT have a path to source, add them to a queue for later discovery.
> For each vertex added to the queue, dequeue them and find the best path from already connected paths that lead to Source.
> Once finished, simply look at all paths that connect to the End Vertex and pick the best one.

This solution takes a look at ALL edges of ALL vertices ONCE. Meaning that at worst, it takes O(n^3) time in order to execute.