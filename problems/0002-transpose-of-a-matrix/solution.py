def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    n, m = len(a), len(a[0])
    transposeA = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            transposeA[j][i] = a[i][j]
    return transposeA

