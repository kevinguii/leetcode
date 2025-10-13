# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# bellman ford algorithm: we're gonna check all options up to k stops, keep a prices array and a temp array
# for every iteration, compare prices and update prices to be temp, then iterate, finally
# return prices[destination]
# O(k*E) time, O(N) space
def findCheapestPrice(n,flights,src,dst,k):
	prices = [float('inf')]* n
	prices[src] = 0
	for i in range(k+1): # at most k stops (0-k)
		tmp = prices.copy()
		for from_node,to_node,price in flights:
			if prices[from_node] == float('inf'):
				continue
			if prices[from_node] + price < tmp[to_node]:
				tmp[to_node] = prices[from_node] + price
		prices = tmp
	return prices[dst] if prices[dst] != float('inf') else -1
	
# faster, dijkstras style min heap algorithm
# O(ElogN) time, O(E+N*k) space
import heapq
def findCheapestPrice(n, flights, src, dst, k):
	# Build adjacency list: graph[u] = [(v, w)]
	graph = {i: [] for i in range(n)}
	for u, v, w in flights:
		graph[u].append((v, w))

	# Min-heap: (cost so far, current city, stops used)
	heap = [(0, src, 0)]

	# Dictionary to store the best cost seen with x stops at a node
	visited = {}

	while heap:
		cost, city, stops = heapq.heappop(heap)
		
		# If destination found, return the cost
		if city == dst:
			return cost
		
		# If too many stops, skip
		if stops > k:
			continue
		
		# If we’ve already found a cheaper way to this city with ≤ this many stops, skip
		if (city, stops) in visited and visited[(city, stops)] <= cost:
			continue
		
		visited[(city, stops)] = cost
		
		# Explore neighbors
		for nei, price in graph[city]:
			heapq.heappush(heap, (cost + price, nei, stops + 1))

	return -1
