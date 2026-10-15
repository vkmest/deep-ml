def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	trace = 0
	n = len(matrix)

	for i in range(n):
		trace += matrix[i][i]
	
	def determinant(mat):
		n = len(mat)

		if n == 1: return mat[0][0]
	
		if n == 2: return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

		det = 0
		for j in range(n):
			# we remove row 0 and column j
			minor = [[mat[i][k] for k in range(n) if k!=j] for i in range(1, n)]
			cofactor = ((-1) ** j) * mat[0][j] * determinant(minor)
			det += cofactor
		return det

	return (determinant(matrix), trace)