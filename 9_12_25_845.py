# 845. Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/description/

# O(n) time, don't run a for loop instead just track i as the whole array goes on
def longestMountain(arr):
	# intuition:
	# look for peak, then use left and right pointers to continually extend until you find max length, store as max_length
	max_length = 0
	n = len(arr)
	i = 1

	# look for peak, can't be on the edges
	while i < n-1:
		if arr[i-1] < arr[i] > arr[i+1]:
			left, right = i-1, i+1
			while left>0 and arr[left-1] < arr[left]:
				left-=1
			while right<n-1 and arr[right+1] < arr[right]:
				right+=1
			max_length = max(max_length,right-left+1)
			i = right
		else:
			i+=1
	return max_length

# O(n^2) time
# def longestMountain(arr):
# 	# intuition:
# 	# look for peak, then use left and right pointers to continually extend until you find max length, store as max_length
# 	max_length = 0
# 	n = len(arr)

# 	# look for peak, can't be on the edges
# 	for i in range(1,n-1):
# 		if arr[i-1] < arr[i] > arr[i+1]:
# 			left = right = i
# 			while left>0 and arr[left-1] < arr[left]:
# 				left-=1
# 			while right<n-1 and arr[right+1] < arr[right]:
# 				right+=1
# 			max_length = max(max_length,right-left+1)
# 	return max_length

arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))

