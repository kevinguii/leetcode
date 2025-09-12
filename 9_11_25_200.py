# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/
# O(m*n) time for rows and cols
# # O(m*n) space

from collections import deque

# further optimizations:
# O(1) check if in range rather than using the whole thing which is O(n)
# initialize the directions just once rather than every bfs check
# don't use a set, just set the grid value to 0 when done checking
# for directions, use tuples instead of brackets, since its immutable and you're not planning to change it

def numIslands(grid):
	if not grid:
		return 0
	
	count = 0
	num_rows,num_cols = len(grid), len(grid[0])
	directions = [(0,-1), (0,1), (-1,0), (1,0)]

	# implement bfs
	def bfs(r,c):
		q = deque()
		grid[r][c]="0"
		q.append((r,c))

		while q:
			row, col = q.popleft()
			for dr, dc in directions:
				new_row, new_col = row+dr, col+dc
				if (0<=new_row<num_rows and 
				0<=new_col<num_cols and 
				grid[new_row][new_col]=="1"):
					q.append((new_row,new_col))
					grid[new_row][new_col]="0"

	# implement overall algo
	# iterate through all rows and cols
	for row in range(num_rows):
		for col in range(num_cols):
			if grid[row][col]=="1":
				bfs(row,col)
				count+=1
	return count

# def numIslands(grid):

# 	if not grid:
# 		return 0
	
# 	# bfs
# 	# create a double ended queue for O(1) operations
# 	# add row,col to visited and to start the queue
# 	# loop through all possible directions for each point in the queue
# 	# check if valid point (within range), not in visited yet, and equal to 1 -> if so, add to queue, add to visited
# 	def bfs(r,c):
# 		q = deque()
# 		visit.add((r,c))
# 		q.append((r,c))
# 		while q:
# 			directions = [[-1,0],[1,0],[0,-1],[0,1]]
# 			row,col = q.popleft()
# 			for dr, dc in directions:
# 				new_row,new_col = row+dr, col+dc
# 				# if within scope and equal to 1, add it to queue and visited
# 				if (new_row in range(num_rows) and new_col in range(num_cols) and grid[new_row][new_col]=="1") and (new_row,new_col) not in visit:
# 					q.append((new_row,new_col))
# 					visit.add((new_row,new_col))

# 	# iterate through all rows and columns, use visited to check 1's, once BFS is done, it'll find all 1's associated with the first one you found, then increase count when done
# 	num_rows = len(grid)
# 	num_cols = len(grid[0])
# 	count = 0
# 	visit = set()
# 	for row in range(num_rows):
# 		for col in range(num_cols):
# 			if grid[row][col]=="1" and (row,col) not in visit:
# 				bfs(row,col)
# 				count+=1
# 	return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))

