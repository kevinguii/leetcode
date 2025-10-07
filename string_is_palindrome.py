def isPalindrome(s):
	res = ""
	resLen = 0

	# odd length
	for i in range(len(s)):
		l,r = i, i
		while l >=0 and r<len(s) and s[l]==s[r]:
			if (r-l+1) > resLen:
				res = s[l:r+1]
				resLen = r-l+1
			l-=1
			r+=1

	# even length
	for i in range(len(s)-1):
		l,r = i, i+1
		while l >=0 and r<len(s) and s[l]==s[r]:
			if (r-l+1) > resLen:
				res = s[l:r+1]
				resLen = r-l+1
			l-=1
			r+=1
	return resLen
# check even and odd length palindromes

def isPalindroneCleaner(s):
	def expand(left,right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			l-=1
			r+=1
		return r-l+1

	res_len = 0
	for i in range(len(s)):
		len1 = expand(i,i)
		len2 = expand(i,i+1)
		res_len = max(res_len,len1,len2)
	return res_len