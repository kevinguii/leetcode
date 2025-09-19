# 77. Combinations
# https://leetcode.com/problems/combinations/description/

# my thoughts: you keep going recursirve until you hit length k, then the backtrackign starts, so if you go 1 2 3, then 1 2 4, then 1 3 4, like that, no clue how to implement
# my intuition is right but idk how to implement

# so what this does (n=4, k=2):
#	runs backtrack starting with 1, appends 2, since it reaches length, add array to res, pop 2 out, then 1 3, add then pop, 1 4, then 2 3, 2 4, 3 4, done

# further optimization: for i in range(start, n - (k - len(path)) + 2): to prune and stop if the remaining characters can't add to the desired length
# O(C(n,k)*k) time and space because of all combinations
def combine(n,k):
	res = []
	def backtrack(start, path):
		if len(path) == k:
			res.append(path[:]) # shallow copy
			return
		for i in range(start,n+1):
			path.append(i)
			backtrack(i+1,path)
			path.pop()
	backtrack(1,[])
	return res

n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]