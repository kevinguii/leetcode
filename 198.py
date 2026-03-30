def rob(nums):
	odd = sum([num for num in nums[::2]])
	even = sum([num for num in nums[1::2]])
	return max(odd,even)

print(rob([2,1,1,2]))