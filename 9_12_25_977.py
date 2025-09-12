# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# actual best, no deque
def sortedSquares(nums):
	n = len(nums)
	res = [0]*n
	idx = n-1
	l, r = 0, n-1
	if nums[0]>=0:
		return [n**2 for n in nums]
	while l<=r:
		left, right = abs(nums[l]), abs(nums[r])
		if left > right:
			res[idx] = left*left
			l+=1
		else:
			res[idx] = right*right
			r-=1
		idx-=1
	return res

# best approach, use deque
# from collections import deque
# def sortedSquares(nums):
# 	q = deque()
# 	l, r = 0, len(nums)-1
# 	if nums[0]>=0:
# 		return [n**2 for n in nums]
# 	while l<=r:
# 		left, right = abs(nums[l]), abs(nums[r])
# 		if left > right:
# 			q.appendleft(left*left)
# 			l+=1
# 		else:
# 			q.appendleft(right*right)
# 			r-=1
# 	return list(q)

# second approach, split and merge
# O(n) time, O(n) space
# def sortedSquares(nums):
# 	# edge cases
# 	if not nums:
# 		return nums
# 	if nums[0]>=0:
# 		return [n**2 for n in nums]
	
# 	# split negatives and non-negatives into two separate lists
# 	idx = len(nums)
# 	for i in range(1,len(nums)):
# 		if nums[i]>=0:
# 			idx = i
# 			break
# 	matrix_A = [num*-1 for num in nums[:idx][::-1]] #exclusive
# 	matrix_B = nums[idx:] #inclusive

# 	final_nums = []
# 	# re-merge
# 	a,b = 0,0
# 	while a<len(matrix_A) and b<len(matrix_B):
# 		if matrix_A[a] < matrix_B[b]:
# 			final_nums.append(matrix_A[a])
# 			a+=1
# 		else:
# 			final_nums.append(matrix_B[b])
# 			b+=1
# 	if a<len(matrix_A):
# 		final_nums.extend(matrix_A[a:])
# 	else:
# 		final_nums.extend(matrix_B[b:])
# 	return [num**2 for num in final_nums]



# first approach
# turn all positive, sort then square
# O(n) for absolute value and squaring, O(nlogn) for sorting, overall O(nlogn) time, O(n) space
# def sortedSquares(nums):
# 	nums = [num**2 for num in nums]
# 	nums = sorted(nums)

# 	return nums

nums = [-5,-3,-2,-1]
print(sortedSquares(nums))