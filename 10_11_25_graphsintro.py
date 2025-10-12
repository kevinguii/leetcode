from collections import deque
# creating a graph
class Graph:
	def __init__(self):
		self.graph = {}
	
	# O(1) time, O(V+E) space for the whole graph
	def add(self,from_vertex,to_vertex):
		# add edge
		if from_vertex in self.graph:
			self.graph[from_vertex].append(to_vertex)
		else:
			self.graph[from_vertex] = [to_vertex]
# BFS traversal
# O(V+E) time to visit all vertices and check all edges
# O(V) space for queue + visited
	def bfs(self,start_vertex):
		if start_vertex not in self.graph:
			return []
		q = deque()
		q.append(start_vertex)
		traversal = []
		while q:
			vertex = q.popleft()
			if vertex not in traversal:
				traversal.append(vertex)
				if vertex in self.graph:
					q.extend(self.graph[vertex])
		return traversal

# DFS traversal
# O(V+E) time, O(V) space
	def dfs(self,start_vertex):
		if start_vertex not in self.graph:
			return []
		
		stack = [start_vertex]
		traversal = []

		while stack:
			vertex = stack.pop()
			if vertex not in traversal:
				traversal.append(vertex)
				if vertex in self.graph:
					stack.extend(reversed(self.graph[vertex]))
		return traversal