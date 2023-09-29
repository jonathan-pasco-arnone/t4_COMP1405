def mult_scalar(matrix, scale):
	""" Multiplies the matrix by a scalar """
	new_matrix = []
	row = 0
	for row_values in matrix:
		new_matrix.append([])
		for value in row_values:
			(new_matrix[row]).append(scale * value)
		row += 1
	return new_matrix

def mult_matrix(a, b):
	return [[]]
	
def euclidean_dist(a,b):
	return -1