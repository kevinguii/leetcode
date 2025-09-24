# 2073. Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

# better approach
# optimize, for everyone before, add to the result at most the min between tickets[k] and tickets[i], for everyone after min between tickets[i] and tickets[k] - 1 since
# we stop when we reach 0 tickets for k
# O(n) time and O(1) space
def timeRequiredToBuy(tickets,k):
	result = 0
	for i in range(len(tickets)):
		if i <= k:
			result += min(tickets[i],tickets[k])
		else:
			result += min(tickets[i],tickets[k]-1)
	return result

# brute force, iterate through all
# O(n*m) n people and m tickets for position k
def timeRequiredToBuy(tickets, k):
	result = 0
	while True:
		for i in range(len(tickets)):
			if tickets[k] == 0:
				return result
			if tickets[i] == 0:
				continue
			if tickets[i] >= 1:
				tickets[i] -=1
				result +=1