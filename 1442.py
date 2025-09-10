# XOR properties: x XOR 0 = x, x XOR x = 0, and x XOR anything else but x = 1
class Solution:
	# brute force: time O(n^4)
	def countTriplets(self,arr:List[int]) -> int:
		n = len(arr)
		res = 0

		for i in range(n-1):
			for j in range(i+1,n):
				for k in range(j,n):
					a,b=0,0
					for idx in range(i,j):
						a ^= arr[idx]
					for idx2 in range(j,k):
						b ^=arr[idx2]
					if a==b:
						res+=1
		return res
	
	#better way: O(n^3) time complexity
	def countTriples2(self,arr:List[int]) -> int:
		n = len(arr)
		res = 0

		for i in range(n-1):
			a=0
			for j in range(i+1,n):
				a ^= arr[j-1]
				b=0
				for k in range(j,n):
					b ^=arr[k]
					if a==b:
						res+=1
		return res
	
	#better way: O(n^2)
	def countTriplets2(self,arr:List[int]) -> int:
		n = len(arr)
		res = 0
		for i in range(n-1):
			cur_xor = arr[i]
			for k in range(i+1,n):
				cur_xor ^= arr[k]
				if cur_xor==0:
					res+=(k-i)
		return res