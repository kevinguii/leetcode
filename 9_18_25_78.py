# 78. Subsets
# https://leetcode.com/problems/subsets/description/

# better, use backtracking
def subsets(nums):
    res = []

    def backtrack(start, path):
        # Always record the current subset
        res.append(path[:])  

        # Explore further elements
        for i in range(start, len(nums)):
            # choose nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)  # move to next element
            path.pop()  # undo choice (backtrack)

    backtrack(0, [])
    return res

# first attempt, iterate through all possibilities, start with empty array, append to each array
def subsets(nums):
	output = [[]]
	for num in nums:
		temp = []
		for o in output:
			temp.append(o+[num]) # [1] + [2] = [1,2]
		output.extend(temp)
	return output

print(subsets(nums = [1,2,3]))