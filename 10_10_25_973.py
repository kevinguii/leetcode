# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/

# NO: you can put tuples into a heap, it'll just use the first value, and while python default creates a min heap, you can make values negative to change it to a max heap
# also even though you square root to find dist, you dont need to to store values, less calculation
# we have max heap which stores k values, then pop off the largest one

# O(nlogk) time, O(k) space
import heapq
def kClosest(points,k):
	heap = []
	for (x,y) in points:
		dist = -(x*x+y*y)
		if len(heap) == k:
			heapq.heappushpop(heap,(dist,x,y))
		else:
			heapq.heappush(heap,(dist,x,y))
	return [(x,y) for (dist,x,y) in heap]

# my thought, create a heap of the distances and a dict to store the points
# heapify first k, then do remaining ones and return the final heap, store each value in the dictionary and pull when done
# handling duplicates: if two have the same distance, idk