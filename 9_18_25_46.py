# 46. Permutations
# https://leetcode.com/problems/permutations/

# intuition: you run the same backtrack algorithm with the stop condition being if start = end (aka we got to the end of our array)
# the idea behind getting the numbres in a different order is to switch i and start as we iterate i, then call backtrack to get the same order of nums just that
# the numbers are in different order now, then when the backtracking is done, the array is reversed back to normal
# on the indices where the i and start is the same (aka new loop), the switching of numbers wont do anything since they're the same value

# O(N*N!) time and space because N! permutations, and takes N time to build each permutation
def permute(nums):
	res = []
	def backtrack(start, end):
		if start == end:
			res.append(nums[:])
		for i in range(start,end):
			nums[start], nums[i] = nums[i], nums[start]
			backtrack(start+1,end)
			nums[start], nums[i] = nums[i], nums[start]
	backtrack(0,len(nums)) # start 0 because we want first index
	return res

nums = [1,2,3]
print(permute(nums))