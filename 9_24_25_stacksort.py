# Stack Sorting
# Not Leetcode: given a stack, sort in asc or desc order

# intuition: create a temp stack, while input stack is not empty, push the number of, while temp stack is not empty, for all # greater than popped #, pop that and put into input stack
# then put the input stack value and push onto temp stack
# continue through the entire thing and return temp stack

# O(n^2) time, O(n) space
def sorted_stack_asc(stack):
	temp_stack = []
	while stack:
		input_val = stack.pop()
		while temp_stack and temp_stack[-1] > input_val:
			stack.append(temp_stack.pop())
		temp_stack.append(input_val)
	return temp_stack

# for descending, flip the greater than sign to a less than sign

# recursive solution
def insert_sorted(stack, val):
    # Base case: stack empty OR val should be placed on top
    if not stack or stack[-1] <= val:
        stack.append(val)
        return
    # Otherwise, pop and recurse
    top = stack.pop()
    insert_sorted(stack, val)
    stack.append(top)

def sort_stack_recursive(stack):
    # Base case
    if not stack:
        return
    # Pop top and sort the rest
    top = stack.pop()
    sort_stack_recursive(stack)
    # Insert popped element in sorted order
    insert_sorted(stack, top)
    return stack
