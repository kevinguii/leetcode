# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/
# nums[i] == nums[j] and abs(i - j) <= k
# values equal and difference between indexes is at most k

# hash map approach
def containsNearbyDuplicate(nums,k):
	seen = {}
	for i, val in enumerate(nums):
		if val in seen and i-seen[val]<=k:
			return True
		seen[val] = i
	return False

# sliding window
# you can look k+1 indices
# O(n) time, O(n) space
# def containsNearbyDuplicate(nums,k):
# 	seen = set()
# 	for i, val in enumerate(nums):
# 		if val in seen:
# 			return True
# 		seen.add(val)
# 		if len(seen) > k:
# 			seen.remove(nums[i-k])
# 	return False

# brute force: double loop, check if values are equal and if abs(i-j) <=k, O(n^2)
# def containsNearbyDuplicate(nums, k):
# 	for i in range(len(nums)-1):
# 		for j in range(i+1,len(nums)):
# 			if nums[i]==nums[j] and abs(i-j)<=k:
# 				return True
# 	return False

nums = [1,2,3,1]
k = 3

print(containsNearbyDuplicate(nums,k))