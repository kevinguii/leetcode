# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# O(n) as well
def maxprofit(prices):
	buy = prices[0]
	profit = 0
	for i in range(1, len(prices)):
		if prices[i] < buy:
			buy = prices[i]
		elif prices[i] - buy > profit:
			profit = prices[i] - buy
	return profit
#O(n) TC and O(1) SC


# sliding window, O(n) time, O(1) space
def maxProfit(prices) -> int:
	# initialize a min, max, set both to first element
	# initialize a maxProfit
	# as you go through the array, if greater than max or smaller than min, change val, recalculate max profit
	l,r = 0,1
	maxProfit = 0
	while r!=len(prices):
		if prices[l]<prices[r]:
			maxProfit=max(maxProfit,prices[r]-prices[l])
		else:
			l = r
		r+=1
	return maxProfit


# brute force, O(n^2) time
# def maxProfit(prices):
# 	res = 0
# 	for i in range(len(prices)-1):
# 		for j in range(i+1,len(prices)):
# 			res = max(res, prices[j]-prices[i])
# 	return res

prices = [7,1,5,3,6,4]
print(maxProfit(prices))