# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/description/
# O(n) time, O(1) space

def minTimeToVisitAllPoints(points):
	res = 0
	x1, y1 = points.pop()
	while points:
		x2, y2 = points.pop()
		res += max(abs(x2-x1),abs(y2-y1))
		x1, y1 = x2, y2
	return res

# usually looked down upon to alter the list itself, version that doesn't do that
def minTimeToVisitAllPoints(points):
	res = 0
	for i in range(1,len(points)):
		x1, y1 = points[i-1]
		x2, y2 = points[i]
		res += max(abs(x2-x1),abs(y2-y1))
	return res

print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))

# O(n) is optimal since every point must be visited