# Find Cycle, iterative DFS
# O(V+E) time, O(V) space

# FOR UNDIRECTED GRAPH
def findCycle(self,start_vertex):
	if start_vertex not in self.graph: return False
	stack = [(start_vertex,None)]#(vertex,parent)
	visited = set()
	while stack:
		vertex,parent = stack.pop()
		if vertex in visited: return True
		visited.add(vertex)
		for neighbor in self.graph.get(vertex,[]):
			if neighbor != parent:
				stack.append((neighbor,vertex))
	return False

# FOR DIRECTED GRAPH, USE ITERATIVE DFS
def find_cycle(self):
	visited = set()

	def dfs(start):
		stack = [(start, None)]  # (vertex, parent)
		while stack:
			vertex, parent = stack.pop()
			if vertex in visited:
				return True
			visited.add(vertex)
			for neighbor in self.graph.get(vertex, []):
				if self.directed or neighbor != parent:
					if neighbor not in visited:
						stack.append((neighbor, vertex))
					elif self.directed:
						# For directed graphs, cycle detected if neighbor already visited in current path
						return True
		return False

	for vertex in self.graph:
		if vertex not in visited:
			if dfs(vertex):
				return True
	return False