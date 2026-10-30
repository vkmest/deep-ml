import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    m, n = len(a), len(a[0])
    new_m, new_n = new_shape
    if new_m * new_n != m * n:
        return []

    mat = []
    for i in range(m):
        for j in range(n):
            mat.append(a[i][j])

    matrix = []
    for i in range(new_m):
        new_row = []
        for j in range(new_n):
            new_row.append(mat[i * new_n + j])
        matrix.append(new_row)

    return np.array(matrix).tolist()