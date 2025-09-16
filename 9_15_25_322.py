# 322. Coin Change
# https://leetcode.com/problems/coin-change/

#pseudocode
# you can use DFS or BFS to check every possible combination, but that's inefficient because you have to do the same subproblem calculations multiple times
# instead use DP, to calculate minimum # coins for all coin amounts up to the target, then for each incremental subproblem, you can use optimal values from previous
# subproblems to help you quickly calculate new minimum for next value, all the way up to target

def coinChange(coins,amount):
	# initially initialize with a sentinel #, bigger than any possible number
	min_coins = [amount+1] * (amount+1)

	# initialize base case: takes 0 coins to make 0 
	min_coins[0] = 0

	for i in range(1,amount+1):
		for coin in coins:
			if (i-coin) >= 0:
				min_coins[i] = min(min_coins[i],1+min_coins[i-coin])

	return min_coins[amount] if min_coins[amount]!=amount+1 else -1