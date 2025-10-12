# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/
from collections import deque
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

# O(V+E) time for iteration and O(V) spacef or queue and clones dictionary
# safe for duplicate values
def clone(node):
	if not node: return None
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