#solution1: bruteforce
# 75th percentile runtime and 99th percentile memory
# TC: O((m+n)log(m+n)) SC: O(m+n) (m and n are length of the two arrays)
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
	combined_arr = sorted(nums1+nums2)
	total_len = len(combined_arr)
	if total_len % 2 == 1 :
		return combined_arr[total_len//2]
	else:
		middle1 = combined_arr[total_len // 2 - 1]
		middle2 = combined_arr[total_len // 2]
		return (float(middle1) + float(middle2)) / 2.0

#solution2: two pointers approach
#79th percentile runtime and 30th percentile memory
#TC: O(n+m) SC: O(1)
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0
        for count in range((n+m)//2 + 1):
            m2 = m1
            if i<n and j<m:
                if nums1[i]<nums2[j]:
                    m1 = nums1[i]
                    i +=1
                else:
                    m1 = nums2[j]
                    j+=1
            elif i<n:
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1
        if (n+m) % 2 == 1:
            return float(m1)
        else:
            return (float(m1)+float(m2))/2

#solution3: binary search
#TC: O(log(min(m,n)))
def findMedianSortedArrays(nums1,nums2):
     A,B = nums1,nums2
     total = len(A) + len(B)
     half = total // 2
     
     if len(B)<len(A):
          A,B = B,A
     l,r = 0,len(A)-1
     while True:
          i = (l+r)//2 #pointer for partition for A
          j = half-i-2 #pointer for partition for B
          Aleft = A[i] if i>=0 else float("-infinity")
          Aright = A[i+1] if (i+1)<len(A) else float("infinity")
          Bleft = B[j] if j>=0 else float("-infinity")
          Bright = B[j+1] if (j+1)<len(B) else float("infinity")
          
		  #partition is correct
          if Aleft<= Bright and Bleft <= Aright:
               #oodd
               if total % 2 == 1:
                    return min(Aright,Bright)
               return (max(Aleft,Bleft)+min(Aright,Bright)) / 2
          elif Aleft>Bright:
               r = i - 1
          else:
               l = i + 1
        
          

    

arr1 = [1, 3,5,7]
arr2 = [2,4,6]

print(findMedianSortedArrays2(arr1,arr2))


