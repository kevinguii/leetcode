# Counting Bits
# https://leetcode.com/problems/counting-bits/

# intuition
# each i is equivalent to 1 + remainder of i - highest power of 2 up to i
# reason is because since it is in power of 2, 7 for example, will just be 7-4 = 3 in binary with an extra 1 added at the front
# so to calculate, we keep track of the most recent power of 2, then add 1 to the number of bits to the remainder of the number - most recent power of 2

# O(n) time and space
def countBits(n):
	dp = [0]*(n+1)
	offset = 1
	for i in range(1,n+1):
		if offset*2 == i:
			offset = i
		dp[i] = 1 + dp[i-offset]
	return dp

print(countBits(2))