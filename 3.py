#solution 1: kind of slow
#runtime: 30th percentile, memory 99th percentile
# Time complexity: O(n), space complexity: O(min(len of string, len of longest substring))
def lengthOfLongestSubstring(s:str)->int:
	n = len(s)
	maxLength = 0
	charset = set()
	left = 0
	for right in range(n):
		if s[right] not in charset:
			charset.add(s[right])
			maxLength = max(maxLength,right-left+1)
		else:
			while s[right] in charset:
				charset.remove(s[left])
				left+=1
			charset.add(s[right])
	return maxLength


#solution 2: use a unordered map
# 83rd percentile runtime, 92nd percentile memory
# O(n) TC and O(n) SC
def lengthOfLongestSubstring2(s:str)->int:
	n = len(s)
	left = 0
	charMap = {}
	maxlength = 0
	for right in range(n):
		if s[right] not in charMap or charMap[s[right]]<left:
			charMap[s[right]] = right
			maxlength = max(maxlength,right-left+1)
		else:
			left = charMap[s[right]] + 1
			charMap[s[right]] = right
	return maxlength

print(lengthOfLongestSubstring2("tmmzuxt"))

