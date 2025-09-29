# longest mountain: something greater than 3
# iterate through the array, once you find a mountain, extend left and right as much as you can to find continually decreasing values, once done, start the new mountain at the bottom of the right
# O(n^2) time, O(1) space
"""
longestMountain(arr):
longest_mountain = 0
n = len(arr)
for i in range(1,n-1):
	if arr[i-1]<arr[i]>arr[i+1]:
		l = r = i
		while arr[l] and arr[l] > arr[l-1]:
			l-=1
		while arr[r] and arr[r] > arr[r+1]:
			r+=1
		longest_mountain = max(longest_mountain,r-l+1)
return longest_mountain

O(n) time and O(1) space
longest_mountain = 0
n = len(arr)
i = 1
while i < n-1:
	if arr[i-1]<arr[i]>arr[i+1]:
		l,r = i-1, i+1
		while arr[l] and arr[l]>arr[l-1]:
		l-=1
		while arr[r] and arr[r] > arr[r+1]:
		r+=1
		longest_mountain = max(longest_mountain,r-l+1)
		i = r
	else:
	i+=1
return longest_mountain
"""

# threeSum: given int array of nums, return all triplets where sum = 0 
# brute force: triple nested loop, iterates through all numbers and gets all values, put in a set so no duplicates
# better, sort the array, then use two pointers, left is next elemen and right is last value
# if equal to 0, add to result and l+=1
# else if result greater than 0 r-=1
# else if result less than 0 l+=1
def threeSum(nums):
	res = []
	nums.sort()
	for idx, val in enumerate(nums):
		if idx > 0 and val == nums[idx-1]:
			continue
		l,r = idx+1, len(nums)-1
		while l<r:
			three_sum = val + nums[l] + nums[r]
			if three_sum == 0:
				res.append(val,nums[l],nums[r])
				l+=1
				r-=1
				while l<r and nums[l]==nums[l-1]:
					l+=1
			elif three_sum > 0:
				r-=1
			else:
				l+=1
	return res

# buy/sell stock: choose a single day to buy/sell stock that gives max profit
# sliding window
# need to set a buy point and a sell point
# look for the smallest value as we iterate
def maxProfit(prices):
	if not prices:
		return 0
	buy = prices[0]
	maxP = 0
	for i in range(1,len(prices)):
		if prices[i] < buy:
			buy = prices[i]
		elif prices[i]-buy > maxP:
			maxP= prices[i]- buy
	return maxP

# squares of a sorted array: given int arr sorted in non-dec, return arr of squares of each
# split off the negative numbers in one O(n) pass
# square then remerge, slow O(n)
# initialize final array
def sortedSquares(nums):
	n = len(nums)
	res = [0]* n
	idx = n-1
	l,r = 0,n-1
	while l<=r:
		l_val, r_val = abs(nums[l]),abs(nums[r])
		if l_val > r_val:
			res[idx] = l_val*l_val
			l+=1
		else:
			res[idx] = r_val*r_val
			r-=1
		idx-=1
	return res

#contains Nearby Duplicate
# nums[i]==nums[j] and abs(i-j)<=k
# brute force, check all possible subsets and if the length between two indices is less than or equal to k
# better, use a sliding window, keep a set, add i+1 value and remove i-1 value, if in seen, return True
def containsNearbyDuplicate(nums,k):
	if k == 0:
		return False
	seen = set()
	for i, val in enumerate(nums):
		if val in seen:
			return True
		seen.add(val)
		if len(seen) > k:
			seen.remove(nums[i-k])
	return False

# Min Abs Difference
# brute force, double loop to find min abs difference between all terms, then another double loop to find all values equal to that
def minAbsDifference(arr):
	minAbsDiff = float('inf')
	n = len(arr)
	for i in range(n-1):
		for j in range(i+1,n):
			if abs(arr[i]-arr[j]) < minAbsDiff:
				minAbsDiff = abs(arr[i]-arr[j])
	res = []
	for i in range(n-1):
		for j in range(i+1,n):
			if abs(arr[i]-arr[j]) == minAbsDiff:
				res.append([arr[i],arr[j]])
	return res

# single loop between adjacent elements to find min diff, then iterate again
def minAbsDifference(arr):
	arr.sort()
	minAbsDiff = float('inf')
	n = len(arr)
	for i in range(1,n):
		diff = abs(arr[i]-arr[i-1])
		if diff < minAbsDiff:
			minAbsDiff = diff
	
	res = []
	for i in range(1,n):
		if abs(arr[i]-arr[i-1]) == minAbsDiff:
			res.append([arr[i-1],arr[i]])
	return res

# Minimum Size Subarray Sum
# given arr positive int nums and positive int target, return minimal length subarray whose sum is greater than or equal to target, if none return 0
"""
sum = 0
l = 0
min_len = float('inf')
for r in range(len(nums)):
sum+= arr[r]
while sum >= target:
	min_len = min(min_len,r-l+1)
	sum-=arr[l]
	l+=1
	if min_len == 1:
	return 1
return 0 if min_len == float('inf') else min_len
"""
def minSubArrayLen(target,nums):
	window_sum = 0
	l = 0
	min_len = float('inf')
	for r in range(len(nums)):
		window_sum+=nums[r]
		while window_sum >= target:
			min_len = min(min_len,r-l+1)
			window_sum-=nums[l]
			l+=1
			if min_len == 1: return 1
	return 0 if min_len == float('inf') else min_len

# Spiral Matrix
# first row, last col, last row, first col
def spiralMatrix(matrix):
	res = []
	while matrix:
		# first row
		res += matrix.pop(0)

		# last col
		if matrix and matrix[0]:
			for row in matrix:
				res.append(row.pop())
		
		# last row backwards
		if matrix:
			res += matrix.pop()[::-1]
		
		# first col
		if matrix and matrix[0]:
			for row in matrix[::-1]:
				res.append(row.pop(0))
	return res

# max subarray: given int nums, find subarray with largest sum and return sum, each evaluation depends on if we should extend the subarray or start a new one
# sliding window
def maxSubarray(nums):
	current_sum = max_sum = nums[0]
	for num in nums[1:]:
		current_sum = max(num, current_sum+num)
		max_sum = max(max_sum,current_sum)
	return max_sum
# dp: instead of calculating every time, store the max subarray sum up to a value in an array, subproblem to solve larger problem
def maxSubarray(nums):
	dp = [0]*len(nums)
	for i, val in enumerate(nums):
		dp[i] = max(val, dp[i-1]+val)
	return max(dp)

# coin change
# use dp to iterate through all coin amounts up to the target, iterate through each coin to see if better to add it or nah
def coinChange(coins,amt):
	dp = [amt+1] * (amt+1)
	dp[0] = 0
	for i in range(1,amt+1):
		for coin in coins:
			if i - coin >= 0:
				dp[i] = min(dp[i],1+dp[i-coin])
	return -1 if dp[amt] == amt+1 else dp[amt]

# climb stairs
# # distinct ways to get to stair n, dp go up from 1 all the way up, sum values
def climbStairs(n):
	if n==1: return 1
	dp = [0] * (n+1)
	dp[0] = 1
	dp [1] = 1
	for i in range(2,n+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]

def climbStairs(n):
	if n==1: return 1
	a,b = 1,2
	for i in range(3,n+1):
		a,b = b, a+b
	return b


# single number: every element appears twice except for one
# brute force: use set(), O(n) space and O(n) time
def singleNumber(nums):
	seen = set()
	for num in nums:
		if num in seen:
			seen.remove(num)
		else:
			seen.add(num)
	return list(seen)[0]
# better, xor, O(n) time and O(1) space
def singleNumber(nums):
	xor = 0
	for num in nums:
		xor ^= num
	return xor

# counting bits
# dp + bit manipulation: go up to the int n, create arr
# the bit manipulation is 1 + dp[i-offset]
# with the offset being the nearest power of 2
def countBits(n):
	dp = [0] * (n+1)
	offset = 1
	for i in range(1,n+1):
		if offset * 2 == i:
			offset = i
		dp[i] = 1 + dp[i-offset]
	return dp

# range sum immutable
class NumArray:
	def __init__(self,nums):
		self.nums = nums
	def sumRange(self,left,right):
		return sum(self.nums[left:right+1])

# better, use a prefix sum
class NumArray:
	def __init__(self,nums):
		self.prefix_sum = [0]*(len(nums)+1)

		for i in range(len(nums)):
			self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]
	def sumRange(self,left,right):
		return self.prefix_sum[right+1] - self.prefix_sum[left]

# letter permutation
def letterCasePermutation(s):
	output = [""]
	for c in s:
		temp = []
		if c.isalpha():
			for o in output:
				temp.append(o+c.lower())
				temp.append(o+c.upper())
		else:
			for o in output:
				temp.append(o+c)
		output = temp
	return output

# remove elements LL
def removeElements(head,val):
	dummy = ListNode(0,head)
	prev = dummy
	curr = head
	while curr:
		if curr.val == val:
			prev.next = curr.next
		else:
			prev = curr
		curr = curr.next
	return dummy.next

# reverse elements between
# iterate up to left - 1
# prev, curr
# reverse those
"""
def reverseElemen(head,left,right):
dummy = ListNode(0,head)
left_prev = dummy
curr = head
for _ in range(left-1):
left_prev = curr
curr = curr.next

prev = None
for _ in range(right-left+1):
next_node = curr.next
curr.next = prev
prev = curr
curr = curr.next

left_prev.next.next = curr
left_prev.next = prev
return dummy.next
"""
def reverseBetween(head,left,right):
	dummy = ListNode(0,head)
	left_prev = dummy
	curr = head
	for _ in range(left-1):
		left_prev = curr
		curr = curr.next
	
	prev = None
	for _ in range(right-left+1):
		next_n = curr.next
		curr.next = prev
		prev = curr
		curr = next_n
	
	left_prev.next.next = curr
	left_prev.next = prev
	return dummy.next

# using second approach
def reverseBetween(head,left,right):
	dummy = ListNode(0,head)
	prev = dummy
	for i in range(left-1):
		prev = prev.next
	start = prev.next
	then = start.next
	for i in range(right-left):
		start.next = then.next
		then.next = prev.next
		prev.next = then
		then = start.next
	return dummy.next

# Palindrome Linked Lists
def isPalindrome(head):
	# find middle
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	
	#reverse second half
	prev = None
	curr = slow
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	
	# check both halves
	l,r = head, prev
	while r:
		if l.val != r.val:
			return False
		l = l.next
		r = r.next
	return True

# Merge Two Sorted LL
def mergeTwo(list1,list2):
	curr = dummy = ListNode()
	while list1 or list2:
		if list1.val < list2.val:
			curr.next = list1
			list1 = list1.next
		else:
			curr.next = list2
			list2 = list2.next
		curr = curr.next
	if list1:
		curr.next = list1
	elif list2:
		curr.next = list2
	return dummy.next

# Min Stack
class MinStack:
	def __init__(self):
		stack = []
	def push(self,val):
		if not self.stack:
			current_min = val
		current_min = min(self.stack[-1][1],val)
		self.stack.append((val,current_min))
	def pop(self):
		return self.stack.pop()
	def top(self):
		return self.stack[-1][0]
	def getMin(self):
		return self.stack[-1][1]

# Valid Parentheses
# use a stack
# closetoopen
# if in closetoOpen
# pop off of it, and if that == closetoopen[close], then continue iteration
def validParentheses(s):
	closeToOpen = {"}":"{","]":"[",")":"("}
	stack = []
	for c in s:
		if c in closeToOpen:
			if stack and stack.pop() !=closeToOpen[c]:
				return False
		else:
			stack.append(c)
	return not stack
		
## Reverse Polish Notation
# use a stack, if we see an operator, pop off the last two and compute the operation, then append back to the end of the stack
def evalRPN(tokens):
	stack = []
	for token in tokens:
		if token in "+-*/":
			right, left = stack.pop(), stack.pop()
			if token == "+":
				stack.append(left+right)
			elif token == "-":
				stack.append(left-right)
			elif token == "*":
				stack.append(left*right)
			else:
				stack.append(int(float(left)/right))
		else:
			stack.append(token)
	return stack.pop()

# Stack Sorting
def stack_sorting(stack):
	temp = []
	while stack:
		val = stack.pop()
		while temp and temp[-1] > val:
			stack.append(temp.pop())
		temp.append(val)
	return temp

# Stack Using Queues
class Stack:
	def __init__(self):
		self.queue = deque()
	def push(self,val):
		self.queue.append(val)
	def pop(self):
		for i in range(len(self.queue)-1):
			self.queue.append(self.queue.popleft())
		return self.queue.popleft()
	def top(self):
		return self.queue[-1]
	def isEmpty(self):
		return len(self.queue) == 0

# Time Needed to Buy Tickets
# brute force subtract one from everyone, keep track of time, continue iterating until target # ticekts = 0
# better way: everybody before target will get min between their # and target # tivkets
# everyone after will get min between their number and target -1 bc we stop when we finish at target
def timeReqToBuy(tickets,k):
	time = 0
	while True:
		for i in range(len(tickets)):
			if tickets[k]==0:
				return time
			if tickets[i] == 0:
				continue
			tickets[i] -=1
			time+=1
			
def timeReqToBuy(tickets,k):
	time = 0
	for i in range(len(tickets)):
		if i <= k:
			time += min(tickets[i],tickets[k])
		else:
			time += min(tickets[i],tickets[k]-1)
	return time