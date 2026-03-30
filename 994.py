from collections import deque

def orangesRotting(self, grid) -> int:
	time = 0
	fresh = 0
	directions = [(0,1),(0,-1),(-1,0),(1,0)]
	q = deque()
	num_rows, num_cols = len(grid),len(grid[0])

	for r in range(num_rows):
		for c in range(num_cols):
			if grid[r][c]==2:
				q.append((r,c))
			elif grid[r][c]==1:
				fresh+=1
	if fresh == 0: return 0

	while q:
		level_len = len(q)
		rotted_this_round = False
		for _ in range(level_len):
			r,c = q.popleft()
			for dr, dc in directions:
				new_r, new_c = dr+r,dc+c
				if 0<=new_r<num_rows and 0<=new_c<num_cols and grid[new_r][new_c]==1:
					grid[new_r][new_c]=2
					fresh-=1
					rotted_this_round = True
					q.append((new_r,new_c))
		if rotted_this_round: time+=1

	return -1 if fresh!=0 else time