# Subsets
# want to find all possible subsets of all numbers
# start with empty list, backtrack from start
# 1, 1 2, 1 2 3 then pops all the way back to 1 then 1 3, then etc
# O(n*2^n) time and space
def subsets(nums):
	output = [[]]
	for num in nums:
		temp = []
		for o in output:
			temp.append(o+[num])
		output.extend(temp)
	return output

def subsets(nums):
	res = []
	def backtrack(start, path):
		res.append(path[:])
		for i in range(start,len(nums)):
			path.append(nums[i])
			backtrack(i+1,path)
			path.pop()

	backtrack(0,[])
	return res

# Permutations
# return all permutations of numbers given an array
# backtrack should be switching numbers and appending when we reach the end
# O(N!*N) time and space to run and store arrays
def permute(nums):
	res = []
	def backtrack(start,end):
		if start == end:
			res.append(nums[:])
			return
		for i in range(start,end):
			nums[start], nums[i] = nums[i], nums[start]
			backtrack(start+1,end)
			nums[start],nums[i] = nums[i], nums[start]
	backtrack(0,len(nums))
	return res


# Combinations
# given n and k, return all possible of k numbres chosen from range 1 to n
# O(C(n,k)*n) time and space
def combine(n,k):
	res = []
	def backtrack(start,path):
		if len(path)==k:
			res.append(path[:])
			return
		for i in range(start,n-(k-len(path))+2):
			path.append(i)
			backtrack(i+1,path)
			path.pop()
	backtrack(1,[])
	return res
