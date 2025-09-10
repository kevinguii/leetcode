#solution 1: take up too much memory, 70th percentile runtime, 34th percentile memory
# TC: O(n) SC: O(n)
def longestPalindrome(s: str) -> int:
	all_letters = {}
	longest_pal = 0
	for letter in range(len(s)):
		if s[letter] not in all_letters:
			all_letters[s[letter]] = 1
		else:
			all_letters[s[letter]] += 1
			if all_letters[s[letter]] % 2 == 0:
				longest_pal += 2
				all_letters[s[letter]] = 0
	longest_pal = longest_pal + (1 if 1 in all_letters.values() else 0)
	return longest_pal

#solution2: use a set instead of a dict
# 95th percentile runtime, 80th percentile memory
def longestPalindrone2(s:str)->int:
	all_letters = set()
	longest_pal = 0
	for letter in range(len(s)):
		if s[letter] not in all_letters:
			all_letters.add(s[letter])
		else:
			longest_pal += 2
			all_letters.remove(s[letter])
	longest_pal = longest_pal + (1 if len(all_letters)!=0  else 0)
	return longest_pal


print(longestPalindrone2('abccccdd'))
