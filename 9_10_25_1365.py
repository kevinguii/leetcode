# 1365. How Many Numbers are Smaller than The Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

def smallerThanCurrent(nums):
	# optimal, using prefix counts, O(n) time, O(n) space
	count = [0]*101
	for num in nums:
		count[num]+=1
	for i in range(1,101):
		count[i]+=count[i-1]
	result = []
	for num in nums:
		if num==0:
			result.append(0)
		else:
			result.append(count[num-1])
	return result
	

	# O(nlogn) time, O(n) space
	# use index
	# sort values, add to dictionary (key = number, value = index)
	# run another loop to grab dictionary value of each one in original array
	nums_sorted = sorted(nums) #O(nlogn)
	num_index = {}
	final_arr = []
	for i,num in enumerate(nums_sorted):
		if num not in num_index:
			num_index[num] = i
	for num in nums:
		final_arr.append(num_index[num])
	return final_arr
			

	# brute force, O(n^2), space O(n)
	smallerThan = []
	for num in nums:
		count = 0
		for i in range(len(nums)):
			if nums[i]<num:
				count+=1
		smallerThan.append(count)
	return smallerThan

print(smallerThanCurrent([8,1,2,2,3])) #[4,0,1,1,3]