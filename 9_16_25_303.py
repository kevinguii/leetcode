# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

#better approach: use prefix sums and the sum of the range from 0-2 is just prefix sum to 2 - prefix sum at 0
class NumArray:
	def __init__(self,nums):
		self.prefix_sum = [0]
		for i in range(len(nums)):
			self.prefix_sum.append(self.prefix_sum[-1]+nums[i])
	def sumRange(self,left,right):
		return self.prefix_sum[right+1] - self.prefix_sum[left]

# will take O(n) every time you run it
class NumArray:
	def __init__(self,nums):
		self.nums = nums
	def sumRange(self,left,right):
		return sum(self.nums[left:right+1])

