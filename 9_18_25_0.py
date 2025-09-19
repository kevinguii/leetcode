# counting bits
# array of # 1 for each bit representation up to n
def countingBits(n):
	offset = 1
	arr = [0]
	for i in range(1,n+1):
		if offset*2 == i:
			offset = i
		arr.append(1+ arr[i-offset])
	return arr

def countingBits2(n):
	offset = 1
	arr = [0]*(n+1)
	for i in range(1,n+1):
		if offset*2 == i:
			offset = i
		arr[i] = 1 + arr[i-offset]
	return arr

# range sum immutable
class NumArray:
	def __init__(self,nums):
		self.prefix_sum = [0]
		for i in range(len(nums)):
			self.prefix_sum.append(self.prefix_sum[-1]+nums[i])
	def sumRange(self,left,right):
		return self.prefix_sum[right+1] - self.prefix_sum[left]

# letter permutation
def letterCasePermutation(s):
	output = [""]
	for c in s:
		temp = []
		if c.isalpha():
			for o in output:
				temp.append(o+c.upper())
				temp.append(o+c.lower())
		else:
			for o in output:
				temp.append(o+c)
		output = temp
	return output