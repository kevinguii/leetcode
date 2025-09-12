# 15. 3Sum
# https://leetcode.com/problems/3sum/

# O(n^2) time, O(1) space not accounting for res list, uses two pointers
def threeSum(nums):
	res = []
	nums.sort()
	for idx, val in enumerate(nums):
		# if i same as previous value, continue to next value
		if idx>0 and val == nums[idx-1]:
			continue

		l,r = idx+1, len(nums)-1
		while l<r:
			threesum = val + nums[l]+ nums[r]
			if threesum > 0:
				r-=1
			elif threesum < 0:
				l+=1
			else:
				res.append([val,nums[l],nums[r]])
				l+=1
				r-=1

				# continue evaluating for more solutions
				while l<r and nums[l]==nums[l-1]:
					l+=1
	return res


#brute force approach
#3 nested for loops: 1 for each number
#O(N^3) time complexity, not optimal
# def threeSum(nums):
# 	nums.sort()
# 	res = []
# 	for i in range(len(nums)):
# 		for j in range(i+1,len(nums)):
# 			for k in range(j+1,len(nums)):
# 				if nums[i]+nums[j]+nums[k]==0:
# 					result = res.append([nums[i],nums[j],nums[k]])
# 					if result not in res:
# 						res.append(result)
# 	return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))