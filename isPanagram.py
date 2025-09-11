#O(n)
def isPanagram(s):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	s = s.lower()
	for char in alphabet:
		if char not in s:
			return False
	return True	

#O(n)
def isPanagram2(s):
	count = 0
	s = set(list(s.lower()))
	for char in s:
		if char.isalpha():
			count += 1
	return count == 26

from collections import Counter
def isPanagram3(s):
	...
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	s = set(s.lower())
	for key in Counter(alphabet).keys():
		if key not in s:
			return False
	return True

def isPanagramOptimal(s):
    s = s.lower()
    letters = set()
    
    for ch in s:
        if 'a' <= ch <= 'z':  # only count letters
            letters.add(ch)
            if len(letters) == 26:  # early exit
                return True
    return False


print(isPanagramOptimal("The quick brown fox jumps over the lazy dog"))