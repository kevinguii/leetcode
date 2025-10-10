# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/
from collections import Counter, deque
import heapq

# keep a max heap and a wait q
# collect frequencies, then while the max heap or queue is still there, if max heap pop value and add to queue, if the queue hits the time, add it back to the max heap

# O(nlogn) time, O(n) space
# shorter code version
def leastInterval(tasks,n):
	task_count = Counter(tasks)
	max_heap = [-freq for freq in task_count.values()]
	heapq.heapify(max_heap)

	time = 0
	q = deque()
	while max_heap or q:
		time+=1
		if max_heap:
			task = 1 + heapq.heappop(max_heap)
			if task:
				q.append((task,time+n))
		if q and q[0][1] == time:
			heapq.heappush(max_heap,q.popleft()[0])
	return time

def leastInterval(tasks,n):
	task_count = Counter(tasks)
	max_heap = [-freq for freq in task_count.values()]
	heapq.heapify(max_heap)

	time = 0
	wait_queue = deque() # time, time available

	while max_heap or wait_queue:
		time +=1

		if max_heap:
			current_task = heapq.heappop(max_heap)
			current_task+=1 # increase by 1 because we have negative values

			if current_task!=0: # if still more tasks to execute
				wait_queue.append((current_task,time+n))
		
		# check if any tasks in the wait queue can be pushed back to heap
		if wait_queue and wait_queue[0][1] == time:
			heapq.heappush(max_heap, wait_queue.popleft()[0])
	return time