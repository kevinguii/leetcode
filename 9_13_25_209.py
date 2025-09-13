# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# my intuition: you can always brute force with double nested loops
# use a sliding window, as i iterate through the array, keep track of the sum and minarrayLength
# WE ARE LOOKING FOR SUM GREATER THAN OR EQUAL TO VALUE
# if sum gets too big move the left pointer over until sum is less than or equal to target, then keep checking by moving right pointer
# if we find a target, that is the max array length we need to check, no more expanding past that

# O(n)
def minSubArrayLen(target,nums):
	window_sum = 0
	min_len = float('inf')
	l = 0
	for r in range(len(nums)):
		window_sum+=nums[r]
		while window_sum >= target:
			min_len = min(min_len,r-l+1)
			window_sum-=nums[l]
			l+=1
			if min_len == 1: return 1
	return 0 if min_len==float('inf') else min_len

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))