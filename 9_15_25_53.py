# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# better approach: use sort of a sliding window
# keep track of a current sum, which should be equal to the first value, and a max_sum
# for every value after that, evaluate whether the current sum should include the new val by doing max(val,curr_sum+new_val)
# at each index, you evaluate whether to extend the current subarray, or start a completely new one from the current number, maintain running sum and track global max
# then evaluate whether to change that to the max sum by doing max(max_sum, curr_sum)

# O(n) time and O(1) space
def maxSubArray(nums):
	max_sum = curr_sum = nums[0]
	for num in nums[1:]:
		curr_sum = max(num, curr_sum+num)
		max_sum = max(max_sum,curr_sum)
	return max_sum

# you can use sliding window/dynmaic programming to solve this
# intuition is: for each consecutive value in the sequence starting from the beginning, create a new array of equal length that stores max subarray val at each index
# then you continue on through the indices and keep the maximum between the current_sum, the value itself, or adding the value to the max subarray already
# iterate through the whole thing and return the max value in that new array

# O(n) time and space
def maxSubArray(nums):
	dp = [0] * (len(nums))
	for i, val in enumerate(nums):
		dp[i] = max(val,dp[i-1]+val)
	return max(dp)

# divide and conquer approach:
# find max subarray in left half and right half and max subarray that crosses middle point, answer = max of all three of these
def maxSubArray(nums):
    def helper(l, r):
        if l == r:
            return nums[l]
        
        mid = (l + r) // 2
        left_sum = helper(l, mid)
        right_sum = helper(mid+1, r)
        
        # compute cross sum
        left_max = float('-inf')
        total = 0
        for i in range(mid, l-1, -1):
            total += nums[i]
            left_max = max(left_max, total)
        
        right_max = float('-inf')
        total = 0
        for i in range(mid+1, r+1):
            total += nums[i]
            right_max = max(right_max, total)
        
        cross_sum = left_max + right_max
        return max(left_sum, right_sum, cross_sum)
    
    return helper(0, len(nums)-1)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))