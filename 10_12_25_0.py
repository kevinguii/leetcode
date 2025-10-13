# Clone Graph
from collections import deque
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
	if not node: return []
	q = deque([node])
	clones = {node:Node(node.val)}
	while q:
		curr = q.popleft()
		for neighbor in curr.neighbors:
			if neighbor not in clones:
				clones[neighbor] = Node(neighbor.val)
				q.append(neighbor)
			clones[curr].neighbors.append(clones[neighbor])
	return clones[node]

# Graphs Intro (initialize, add, bfs dfs)
class Graph:
	def __init__(self):
		self.graph = {}
	def add(self,from_vertex,to_vertex):
		if from_vertex in self.graph:
			self.graph[from_vertex].append(to_vertex)
		else:
			self.graph[from_vertex] = [to_vertex]
	def bfs(self,start_vertex):
		if start_vertex not in self.graph: return []
		q = deque([start_vertex])
		traversal = []
		while q:
			vertex = q.popleft()
			if vertex not in traversal:
				traversal.append(vertex)
				if vertex in self.graph:
					q.extend(self.graph[vertex])
		return traversal
	def dfs(self,start_vertex):
		if start_vertex not in self.graph: return []
		stack = [start_vertex]
		traversal = []
		while stack:
			vertex = stack.pop()
			if vertex not in traversal:
				traversal.append(vertex)
				if vertex in self.graph: # if it has neighbors
					stack.extend(reversed(self.graph[vertex]))
		return traversal

# count edges
# adjacency list
def count_edges(self):
	edge_count = sum(len(neighbors) for neighbors in self.graph.values())
	return edge_count
	# edge count // 2 if undirected graph

# find cycle, DFS
def findCycle(self,start_vertex):
	if start_vertex not in self.graph: return False
	stack = [(start_vertex,None)]
	visited = set()
	while stack:
		vertex,parent = stack.pop()
		if vertex in visited: return True
		visited.add(vertex)
		for neighbor in self.graph.get(vertex,[]):
			if neighbor != parent:
				stack.append((neighbor,vertex))
	return False

# find largest node
def findLargestNode(self,start_vertex):
	if start_vertex not in self.graph: return None
	q = deque([start_vertex])
	largest_node = start_vertex
	visited = set([start_vertex])
	while q:
		vertex = q.popleft()
		largest_node = max(largest_node,vertex)
		for neighbor in self.graph.get(vertex,[]):
			if neighbor not in visited:
				q.append(neighbor)
				visited.add(neighbor)
	return largest_node