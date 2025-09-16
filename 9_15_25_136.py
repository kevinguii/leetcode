# 136. Single Number
# https://leetcode.com/problems/single-number/description/
# you can use double loop or hashmap
# most efficient way is to use bit manipulation
# if each is a duplicate, 1 ^ 1 = 0
# n ^ 0 = n, therefore the only duplicate when we xor all values will remain

def singleNumber(nums):
	xor = 0
	for num in nums:
		xor ^= num
	return xor

nums = [2,2,1] #output should be 1
print(singleNumber(nums))