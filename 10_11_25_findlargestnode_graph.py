# Find Largest Node, iterative BFS
from collections import deque

# O(V+E) time, O(V) space
def findLargestNode(self,start_vertex):
	if start_vertex not in self.graph: return None
	q = deque([start_vertex])
	largest_node = start_vertex
	visited = set([start_vertex]) #O(1) lookup
	while q:
		vertex = q.popleft()
		largest_node = max(largest_node,vertex)
		for neighbor in self.graph.get(vertex,[]):
			if neighbor not in visited:
				visited.add(neighbor)
				q.append(neighbor)
	return largest_node