class Solution:
    def calculate_binary(self, s: str) -> int:
        if s == "0":
            return 0
        
        sum = 0
        pos = 0
        str_s = str(s)
        n = len(str_s)
        for x in range(n-1, -1, -1):
            sum += (2**x) * (int(str_s[pos]))
            pos += 1
        return sum
    def numSteps(self, s: str) -> int:
        count = 0
        s = self.calculate_binary(s)
        if s == 0:
            return 1
        while s != 1:
            if s % 2 == 0:
                s //= 2
            else:
                s += 1
            count += 1
        return count
    
# runtime: 91% percentile
# memory: 6% percentile
# O(n) time complexity and O(n) space complexity

#######
# better solution
class Solution2:
    def numSteps(self, s: str) -> int:
        count = 0
        carry = 0
        steps = 0
        n = len(s)-1
        for x in range(n,0,-1):
            if int(s[x]) + carry ==1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
    
#runtime: 68th percentile
#memory: 94th percentile
# O(n) time complexity, O(1) space complexity

#explaination
# how this algorithm works is how we convert binary numbers to 1, starting to look at the right most bit first and moving left.
# we have a carry variable to keep track of the times when we need to add one and then divide by 2 (odd #) and we iterate through the binary number  once keeping track
# of the number of steps and the carry value. If the carry + the bit = 1, then we know it's odd and we need to add one and divide by 2 (two operations), moving the index left
# just signifies the time when we delete the 0 hanging at the end of the bit. For ex, to go from "10" to "1", we chop off the 1 at the end. Keep doing this until we reach the left
# most bit and then add the carry with the current number of steps because if carry was 0, then we would leave the remaining 1, otherwise we have to do one more step to go from 10 to 1.