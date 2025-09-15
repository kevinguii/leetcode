# 268. Missing Number
# https://leetcode.com/problems/missing-number/

def missingNumber(nums) -> int:
        # O(1) time
        return sum(range(len(nums)+1)) - sum(nums)

        # O(n^2) time
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

print(missingNumber([3,0,1]))  #2