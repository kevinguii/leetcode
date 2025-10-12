# Count Number of Edges
# easily count total # edges in the graph by iterative through each vertex and summing up lengths of
# their adjacency lists
# O(V+E) time, O(1) space

# FOR DIRECTED GRAPH
def count_edges(self):
	edge_count = 0
	for vertex in self.graph:
		edge_count += len(self.graph[vertex])
	return edge_count

# FOR UNDIRECTED
def count_edges(self):
	edge_count = sum(len(neighbors) for neighbors in self.graph.values())
	if not self.directed:
		edge_count //= 2  # undirected edges counted twice
	return edge_count