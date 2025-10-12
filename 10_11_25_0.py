import heapq
from collections import Counter, deque
# Kth Largest Element in Array
def kthLargest(nums,k):
	return heapq.nlargest(k,nums)[-1]

# O(nlogk) time and O(N) space
def kthLargest(nums,k):
	heap = heapq.heapify(nums[:k])
	for num in nums[k:]:
		if num > heap[0]:
			heapq.heapreplace(heap,num)
	return heap[0]

# K Closest Points to Origin
# find the distance, store as negative so the smallest (aka largest distance) always gets popped off

# O(nlogk) time and O(k) space
def kClosest(points,k):
	heap = []
	for (x,y) in points:
		dist = -(x*x+y*y)
		if len(heap) == k:
			heapq.heappushpop(heap,(dist,x,y))
		else:
			heapq.heappush(heap,(dist,x,y))
	return [(x,y) for (dist,x,y) in heap]

# Top K Frequent Elements
# store freq, number
# O(nlogk) time, O(k) space
def topKFrequent(nums,k):
	count = Counter(nums)
	heap = []
	for num, freq in count.items():
		if len(heap) == k:
			heapq.heappushpop(heap,(freq,num))
		else:
			heapq.heappush(heap,(freq,num))
	return [num for (freq,num) in heap]

# Task Scheduler
# implement a wait queue with a heap, heap will store most frequent task, want max heap so negative
# values, add one to task then check if its 0, if not add to queue, if queue reaches its spot put back in heap
# O(nlogn) time, O(n) space
def leastInterval(tasks,n):
	tasks_count = Counter(tasks) # {A:3,B:2}
	max_heap = [-freq for freq in tasks_count.values()]
	heapq.heapify(max_heap)

	time = 0
	q = deque()
	while q or max_heap:
		time+=1
		if max_heap:
			current_task = heapq.heappop(max_heap)
			current_task+=1
			if current_task:
				q.append((current_task,time+n))
		if q and q[0][1] == time:
			heapq.heappush(max_heap,q.popleft()[0])
	return time
