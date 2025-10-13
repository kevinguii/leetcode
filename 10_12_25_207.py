# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/description/

# first, build an adjacency list (graph) for all of the prerequisites (course to take: prerequisites)
# then iterate DFS and check for any cycle (cycle = circular dependency)
# O(V+E) time and O(V+E) space
def canFinish(numCourses,prerequisites):
	adj = {course: [] for course in range(numCourses)}
	for course, pre in prerequisites:
		adj[course].append(pre)
	
	# iterative DFS to check for cycles
	for course in range(numCourses):
		stack = [(course,set())]
		while stack:
			cur_course, visited = stack.pop()
			if cur_course in visited: return False
			visited.add(cur_course)
			for pre in adj[cur_course]:
				stack.append((pre,visited.copy()))
		adj[course] = [] # remove course, faster
	return True


# recursive DFS
# O(V+E) time and O(V) space
def canFinish(numCourses, prerequisites):
	adj = {i: [] for i in range(numCourses)}
	for course, pre in prerequisites:
		adj[course].append(pre)

	state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

	def dfs(course):
		if state[course] == 1:  # Found a cycle
			return False
		if state[course] == 2:  # Already checked
			return True
		
		state[course] = 1  # Mark as visiting
		for pre in adj[course]:
			if not dfs(pre):
				return False
		
		state[course] = 2  # Mark as fully visited
		return True

	for course in range(numCourses):
		if not dfs(course):
			return False

	return True
