# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# use a heap
import heapq

# approach 1: built in function
# O(nlogk) space, O(k) time
def findKthLargest(nums,k):
	return heapq.nlargest(k,nums)[-1]

# approach 2: manually append and pop
def findKthLargest(nums,k):
	heap = []
	for i in nums:
		heapq.heappush(heap,i)
	for i in range(len(nums)-k):
		heapq.heappop(heap)
	return heapq.heappop(heap)

# approach 3: best approach (approach 1 but better understanding)
# create min heap with first k elements, iterate through remaining elements and if greater replace the root with it, maintains kth largest element at root
def findKthLargest(nums,k):
	heap = nums[:k]
	heapq.heapify(heap) # O(k) time because python optimized
	for num in nums[k:]:
		if num > heap[0]:
			heapq.heapreplace(heap,num) # removes smallest element, inserts new and re-heaps, each in O((n-k)*2logk time) => logk time
	return heap[0]