# 219 contains duplicate two
# return True if nums[i]==nums[j] and abs(i-j) <= k
def containsNearbyDuplicate(nums,k):
	num_set = set()
	for i, val in enumerate(nums):
		if val in num_set:
			return True
		num_set.add(val)
		if len(num_set) >= 3:
			num_set.remove(nums[i-k])
	return False

def containsNearbyDuplicate(nums,k):
	hash_map = {}
	for i, val in enumerate(nums):
		if val in hash_map and i-hash_map[val]<=k:
				return True 
		else:
			hash_map[val] = i
	return False

# 1200. Minimum Absolute Difference
# given array of distinct integers, find all pairs of elements with minimum absolute difference of any two elements, return list of pairs in ascending order, each pair follows
# brute force: double loop to find all abs differences, then get the minimum, then another double loop to find all pairs equal to that, then sort
# better:
# nums.sort() -> find min abs difference by subtracting adjacent elements in one loop -> another loop to find all matches, append to a result
def minimumAbsDiff(arr):
	arr.sort()
	minAbsDiff = float('inf')
	for i in range(1,len(arr)):
		minAbsDiff = min(minAbsDiff,arr[i]-arr[i-1])
	res = []
	for j in range(1,len(arr)):
		if arr[j]-arr[j-1] == minAbsDiff:
			res.append([j-1,j])
	return res

# even better approach, one total for loop
# initialize minAbsDiff, iterate through all vals, if difference < current_min: set new min and new res, otherwise if equal append, otherwise nothing??
def minimumAbsDiff(arr):
	arr.sort()
	res = []
	min_diff = float('inf')
	for i in range(1,len(arr)):
		# check if less than diff
		if arr[i]-arr[i-1] < min_diff:
			min_diff = arr[i]-arr[i-1]
			res = [[arr[i-1],arr[i]]]
		elif arr[i]-arr[i-1] == min_diff:
			res.append([arr[i-1],arr[i]])
	return res
		# if equal append

# 209. Minimum Size Subarray Sum
# given arr positive int nums and positive int target, return minimal length subarray whose sum is greater than or equal to target, if none return 0
# brute force: find all sums of values >= target and return the smallest, double nested loop O(N^2)
# better, use sliding window
# keep a running sum, if value gets greater than or equal to, then subtract values from it until it's less than or equal to the value
def minSubArrayLen(nums,target):
	min_len = float('inf')
	running_sum = 0
	l = 0
	for r in range(len(nums)):
		running_sum+=nums[r]
		while running_sum>=target:
			min_len = min(min_len,r-l+1)
			running_sum-=nums[l]
			l+=1
		if min_len == 1: return 1
	return 0 if min_len==float('inf') else min_len

# 54. Spiral Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

def spiralMatrix(matrix):
	res = []
	while matrix:
		if matrix:
			res.extend(matrix.pop(0))
		if matrix and matrix[0]:
			for row in matrix:
				res.append(row.pop())
		if matrix:
			res.extend(matrix.pop()[::-1])
		if matrix and matrix[0]:
			for row in matrix[::-1]:
				res.append(row.pop(0))
	return res

print(spiralMatrix(matrix))
