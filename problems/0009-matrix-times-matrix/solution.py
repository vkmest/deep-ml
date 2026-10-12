def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b): return -1
    
    n, m= len(a), len(b[0])

    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            cur = 0
            for k in range(len(a[0])):
                cur += a[i][k]*b[k][j]
            c[i][j] = cur
    return c