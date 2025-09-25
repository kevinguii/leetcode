# Reverse First K Elemenets of a Queue Using a Stack

# O(n) time, O(k) space for # elem in array
def reverseFirstK(k,q):
	stack = []
	for i in range(k):
		stack.append(q.popleft())
	
	while stack:
		q.append(stack.pop())
	
	for i in range(len(q)-k):
		q.append(q.popleft())
	return q