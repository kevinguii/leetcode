# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

# my thought: build a counter, then min heap and replace for every one after

from collections import Counter
import heapq

# O(nlogk) time, O(N) space
def topKFrequent(nums,k):
	count = Counter(nums)
	heap = []
	for num,freq in count.items():
		if len(heap) < k:
			heapq.heappush(heap,(freq,num))
		elif freq > heap[0][0]:
			heapq.heapreplace(heap,(freq,num))
	return [num for (freq,num) in heap]

# brute force, do a counter, sort items, return first k
# this way is O(n)
def topKFrequent(nums,k):
	count = {}
	freq = [[] for i in range(len(nums)+1)]
	for num in nums:
		count[num] = 1 + count.get(num,0) #add one if its there, add 1 to 0 if not there
	for n,c in count.items():
		freq[c].append(n)
	res = []
	for i in range(len(freq)-1,0,-1):
		for n in freq[i]:
			res.append(n)
			if len(res)==k:
				return res