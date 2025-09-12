# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# O(n) time, O(n) space

# better written
def spiralOrder(matrix):
	res = []
	while matrix:
		#first row
		res+=(matrix.pop(0))

		# last col
		if matrix and matrix[0]: #checks first row and entire array
			for row in matrix:
				res.append(row.pop())
		
		# last row in reverse order
		if matrix: 
			res+=(matrix.pop()[::-1])

		# first row
		if matrix and matrix[0]:
			for row in matrix[::-1]:
				res.append(row.pop(0))
	
	return res

# def spiralOrder(matrix):
# 	...
# 	# simulation: first row, last col, last row, first col, repeat, keep track of first row and iterate
# 	# num rows = len(matrix), num cols = len(matrix[0])
# 	# edge cases: one row or one col only
# 	res = []
# 	while matrix:
# 		# first row
# 		res.extend(matrix[0])
# 		matrix.pop(0)

# 		if len(matrix)==0: break

# 		# last col
# 		for col in matrix:
# 			res.append(col[-1])
# 			col.pop(-1)

# 		if len(matrix)==0: break

# 		# last row
# 		res.extend(matrix[-1][::-1])
# 		matrix.pop(-1)
		
# 		if len(matrix) == 0: break

# 		# first col
# 		for row in matrix[::-1]:
# 			res.append(row[0])
# 			row.pop(0)

# 		if len(matrix) == 0: break
# 	return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))