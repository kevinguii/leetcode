def containsDuplicate(nums):
	num_set = set(nums)
	return len(num_set) != len(nums)
	# for num in nums:
	# 	if num in num_set:
	# 		return True
	# 	num_set.add(num)
	# return False

print(containsDuplicate([1,2,3,4]))