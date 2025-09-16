# 784. Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/description/

# first try: iterate through all letters/nums, if is letter, for each output we currently have, append the upper and lower versions, for numbers, just append
# to our current output
def letterCasePermutation(s):
	output=[""]
	for c in s:
		temp = []
		if c.isalpha():
			for o in output:
				temp.append(o+c.lower())
				temp.append(o+c.upper())
		else:
			for o in output:
				temp.append(o+c)
		output = temp
	return output
