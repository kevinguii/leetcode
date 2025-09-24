# 155. Min Stack
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1780702633/

# approach: append, pop, top are all easy, just getting min in O(1) time
# combat this by storing current_min with every append to the stack

# O(1) for time, O(n) space since we're storing an extra integer for each element (2n)
class MinStack:
	def __init__(self):
		self.stack = []

	def push(self, val: int) -> None:
		if not self.stack:
			current_min = val
		else:
			current_min = min(self.stack[-1][1], val)
		self.stack.append((val,current_min))

	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1][0]

	def getMin(self) -> int:
		return self.stack[-1][1]