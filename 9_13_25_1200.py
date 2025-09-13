# 1200. Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/description/

# most optimal, do it in one pass
def minimumAbsDifference(arr):
    arr.sort()
    res = []
    minAbsDiff = float('inf')

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < minAbsDiff:
            minAbsDiff = diff
            res = [[arr[i-1], arr[i]]]
        elif diff == minAbsDiff:
            res.append([arr[i-1], arr[i]])

    return res

# initial intuition: first, find the minimum abs difference between numbers
# second iteration: if adjacent numbers equal it, append
# O(n) time, O(nlogn) sorting
def minimimAbsDifference(arr):
	minAbsDiff = float('inf')
	arr.sort()
	for i in range(len(arr)-1):
		minAbsDiff = min(minAbsDiff,abs(arr[i+1]-arr[i]))
	res = []
	for i in range(1,len(arr)):
		left_val, right_val = arr[i-1],arr[i]
		if right_val-left_val==minAbsDiff:
			res.append([left_val,right_val])
	return res

print(minimimAbsDifference([4,2,1,3]))

# brute force: you can just do a double nested loop to find min abs difference, then another double nested loop to find all values equal to that, O(n^2)