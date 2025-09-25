# Evaluate Reverse Polish Notation
# O(n) time, O(n) space because appending
def evalRPN(tokens):
	stack = []
	for token in tokens:
		if token not in '+-*/':
			stack.append(int(token))
		else:
			right, left = stack.pop(), stack.pop()
			if token == "+":
				stack.append(left+right)
			elif token == "-":
				stack.append(left-right)
			elif token == "*":
				stack.append(left*right)
			else:
				stack.append(int(float(left)/right))
	return stack.pop()

# Stack Sorting
# O(n) time and space
def stackSort(stack):
	temp = []
	while stack:
		val = stack.pop()
		while temp and temp[-1] > val:
			stack.append(temp.pop())
		temp.append(val)
	return temp

# recursion way
def sort_stack_recursive(stack):
	if not stack:
		return
	top = stack.pop()
	sort_stack_recursive(stack)
	insert_sorted(stack,top)
	return stack
def insert_sorted(stack,val):
	if not stack or stack[-1] <= val:
		stack.append(val)
		return
	top = stack.pop()
	insert_sorted(stack,val)
	stack.append(top)

# Implement Stack Using Queues
from collections import deque
class Stack:
	def __init__(self):
		self.stack = deque()
	def push(self,val):
		self.stack.append(val)
	def pop(self):
		for i in range(len(self.stack)-1):
			self.stack.append(self.stack.popleft())
		return self.stack.popleft()
	def top(self):
		return self.stack[-1]
	def isEmpty(self):
		return len(self.stack) == 0

# Time Needed To Buy Tickets

# better: everyone before k will get all their tickets, find min between them and # tickets k needs, for people after, same except # tickets k needs -1
# since we'll stop when k gets their tickets
def timeRequiredToBuy(tickets,k):
	time = 0
	for i in range(len(tickets)):
		if i <= k:
			time += min(tickets[i],tickets[k])
		else:
			time += min(tickets[i],tickets[k]-1)
	return time

# brute force, go through as many iterations subtracting 1 then returning if tickets[k] == 0
# O(m*n) time, O(1) space
def timeRequiredToBuy(tickets,k):
	time = 0
	while True:
		for i in range(len(tickets)):
			if tickets[k] == 0:
				return time
			if tickets[i] == 0:
				continue
			tickets[i] -=1
			time +=1