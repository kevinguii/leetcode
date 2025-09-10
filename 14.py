strs = ["flower","flow","flight"]

#solution 1: TC: O(N x L), SC: O(L), 
# N = number of strings, L = length of longest common substring
# 80th percentile runtime, 9th percentile memory
def longestCommonPrefix(strs) -> str:
        if len(strs)==1:
            return strs[0]
        curr_longest = strs[0]
        for i in range(1,len(strs)):
            len_prev,len_current = len(curr_longest),len(strs[i])
            new_longest=''
            for j in range(min(len_prev,len_current)):
                if(curr_longest[j]==strs[i][j]):
                    new_longest = new_longest + curr_longest[j]
                else:
                    break
            curr_longest = new_longest
        return curr_longest

#solution 2: only compares first and last string of the array
# TC: O(NlogN x L) to sort and compare
# SC: O(N+L) to sort and find longest common
# 75th percentile runtime, 85th percentile memory
def longestCommonPrefix2(strs):
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    common = ''
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return common
        common+=first[i]
    return common