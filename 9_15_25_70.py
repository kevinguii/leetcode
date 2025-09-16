# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# intuition, for each sequential step higher you climb, its either adding on the number of steps from n-1 by taking 1 step or n-2 by taking 2
# so the answer should be for every sequential step, its the sum of the two steps before it, aka fibionacci sequence

# space optimization: O(1) space
def climbStairs(n):
	if n==1:
		return 1
	a,b = 1,2
	for _ in range(3,n+1):
		a,b = b,a+b
	return b

# O(n) time and space
def climbStairs(n):
	if n == 1:
		return 1
	dp = [0] * (n+1)
	dp[1], dp[2] = 1, 2
	for i in range(3,n+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]

print(climbStairs(4))