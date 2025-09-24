# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# intuition: keep a stack, append to if number, if operator, pop off last two and do the calculation, then append back onto stack and continue
# O(n) time and space
def evalRPN(tokens):
	stack = []
	for token in tokens:
		if token not in "+-*/":
			stack.append(int(token))
		else:
			right, left = stack.pop(), stack.pop()
			if token == "+":
				stack.append(left+right)
			elif token == "-":
				stack.append(left-right)
			elif token == "*":
				stack.append(left*right)
			elif token == "/":
				stack.append(int(float(left)/right))
	return stack.pop()