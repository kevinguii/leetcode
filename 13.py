#best solution
# TC: O(n), SC: O(1)
class Solution:
	def romanToInt(self,s:str) -> int:
		n=len(s)
		res = 0
		roman_dict = {
			'I':1,
			'V':5,
			'X':10,
			'L':50,
			'C':100,
			'D':500,
			'M':1000
		}
		for i in range(n):
			if i<n-1 and roman_dict[s[i]]<roman_dict[s[i+1]]:
				res-=roman_dict[s[i]]
			else:
				res+=roman_dict[s[i]]
		return res


hi = Solution()
print(hi.romanToInt("MCMXCIV"))