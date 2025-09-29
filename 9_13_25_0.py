# longest Mountain
# a mountain is length>=3, return longest subarray length that's a mountain, 0 if no mountain
# find a peak: extend left and right for as long as its still a mountain, calculate legnth of mountain compare to max length
# don't have to iterate through all values, we can just start at the end of the right side of the peak
# initialize res = 0
# iterate for i in range(1,len(nums)-1)
# look for a value where nums[i-1]< nums[i] > nums[i+1]
# if that's the case, initialize l=i-1 and r=i+1
# while l>0 and r<len(nums)-1: if nums[l]>nums[l-1], l-=1, if nums[r+1]<nums[r], r+=1
# when done, new length is max(current, r-l+1)
# set i equal to r
def longestMountain(arr):
	res = 0
	for i in range(1,len(arr)-1):
		if arr[i-1] < arr[i] > arr[i+1]:
			l,r = i-1, i+1
			while l > 0 and arr[l-1]<arr[l]:
				l-=1
			while r < len(arr) - 1 and arr[r+1] < arr[r]:
				r+=1
			res = max(res, r-l+1)
			i = r
	return res
arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))


# threeSum
# integer array, return all triplets where the sum = 0
# brute force: O(n^3) triple nested loop to calculate all combos and return them (probably need to account for duplicates)
# better way: similar to two sum
# initialize: sort the array, res = []
# outside loop: iterate through all values
# inside loop: initialize left and right, while l<r: compare the total sum, if greater than 0 r-=1, less l+=1, if equal, add to res keep iteratint
def threeSum(nums):
	res=[]
	nums.sort()
	for idx, val in enumerate(nums):
		if idx > 0 and nums[idx]==nums[idx-1]:
			continue
		l,r = idx+1, len(nums)-1
		while l<r:
			s = val + nums[l] + nums[r]
			if s > 0:
				r-=1
			elif s < 0:
				l+=1
			else:
				res.append([val,nums[l],nums[r]])
				l+=1
				r-=1
				while l<r and nums[l]==nums[l-1]:
					l+=1
	return res

# buy/sell stock
# intuition: need to find best time to buy and best time to sell
# brute force: O(n^2) iterate through all possibilities, find the largest difference
# initialize: maxP=0, buy price=0, 
def maxProfit(prices):
	max_P = 0
	buy = prices[0]
	for i in range(1,len(prices)-1):
		if prices[i] < buy:
			buy = prices
		else:
			max_P = max(max_P,prices[i]-buy)
	return max_P


# squares of a sorted array
# intuition: easy way: square all the values, then sort it: O(nlogn)
# better way: better way of sorting
# two pointers: one at the beginning other at the end
# array to hold the values, initialize all as 0 first
# we compare abs value of the left and right values, if left is bigger, we append to the end, l+=1 otherwise right, r-=1, l<r
def sortedSquares(nums):
	res = [0] * len(nums)
	idx = len(nums)-1
	l,r = 0, len(nums)-1
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
	# nums = [num**2 for num in nums]
	# return nums.sort()
	