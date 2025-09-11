# 448. Find All Numbers Disappeared in an Array 
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

def findDisappearedNumbers(nums):
    
    # O(n) time
    nums_set = set(nums)
    return [num for num in range(1,len(nums)+1) if num not in nums_set]

    # O(n) time
#     return list(set(range(1, len(nums)+1)) - set(nums))
    
    # brute force O(n)
#     missing = []
#     length = len(nums)+1
#     for i in range(1,length):
#         if i not in nums:
#             missing.append(i)
#     return missing



print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  #[5,6]