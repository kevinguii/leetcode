# Max Subarray
# given nums, find max value of a subarray, and return the value
# brute force: iterate through all possible subarrays and return the max, O(n^2)
# use dp/sliding window up to len of array
# find the largest sum for each subarray
# either extending the subarray from the current sum, or creating a new subarray
def maxSubArray(nums):
	current_sum = max_sum = nums[0]
	for num in nums[1:]:
		current_sum = max(num,current_sum+num)
		max_sum = max(max_sum,current_sum)
	return max_sum

def maxSubArray(nums):
	dp = [0] * len(nums)
	for i, val in enumerate(nums):
		dp[i] = max(dp[i],dp[i-1]+val)
	return max(dp)

# Coin Change
# give different denominations of coins and a target amount, find least amount of coins to make up target and -1 if you can't
# intuition: you can check through all combos, inefficient
# use dp to find min # coins for each number up to target
# dp = [some large #] * target+1
# dp[0] = 0
# for each value from 1 to end of dp
# 	for each coin denomination:
#		if the current index - coin amount is greater than or equal to 0:
#			dp[value] = min(dp[val],1+dp[value-coin denomination])
# return dp[target] if not equal to large # otherwise -1
def coinChange(coins,amount):
	dp = [amount+1]*(amount+1)
	dp[0] = 0
	for i in range(1,amount+1):
		for coin in coins:
			if (i-coin)>=0:
				dp[i] = min(dp[i],1+dp[i-coin])
	return -1 if dp[amount+1]==amount+1 else dp[amount+1]

# Climb Stairs
# climbing a staircase with n steps, takes 1 or 2 steps every time, max # of ways to climb to the top
# 1 = 1, 2 = 2, 3 = 3, 4 = 5
# intuition: every sequential step is the sum of taking one step or two from previous ones, therefore we just add, f(n) = f(n-1) + f(n-2), which is fibionacci
def climbStairs(n):
	arr = [0]*n+1
	arr[1],arr[2] = 1,2
	for i in range(3,len(arr)):
		arr[i] = arr[i-1] + arr[i-2]
	return arr[n]

# Single Number
# you can brute force with hashmap or set, will be O(n^2) time and O(n) space
# better way is to use XOR, apply it to every number in the array, the only one that will remain is the one that is not duplicated, because x ^ x = 0, n ^ 0 = n
def singleNumber(nums):
	...
	xor = 0
	for num in nums:
		xor ^= num
	return xor