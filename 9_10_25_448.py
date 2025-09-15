# 448. Find All Numbers Disappeared in an Array 
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# best approach, since we know that each number is in range [1,n], use indexes as a marker
def findDisappearedNumbers(nums):
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    return [i+1 for i, num in enumerate(nums) if num > 0 ]

def findDisappearedNumbers(nums):
    # O(n^2) time
    nums_set = set(nums)
    return [num for num in range(1,len(nums)+1) if num not in nums_set]

    # O(n) time
#     return list(set(range(1, len(nums)+1)) - set(nums))
    
    # brute force O(n^2), O(n) space
#     missing = []
#     length = len(nums)+1
#     for i in range(1,length):
#         if i not in nums:
#             missing.append(i)
#     return missing



print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  #[5,6]