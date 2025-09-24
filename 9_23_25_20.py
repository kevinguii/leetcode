# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# intuition: use a stack and check the open/close
# if open, append
# if close, pop off the last value and check if it matches
# if stack is empty by the end its true otherwise false

# O(n) time and space
def isValid(s):
	stack = []
	closeToOpen = {')':'(','}':'{',']':'['}
	for c in s:
		if c in closeToOpen:
			if stack and stack[-1] == closeToOpen[c]:
				stack.pop()
			else:
				return False
		else:
			stack.append(c)
	return False if stack else True

