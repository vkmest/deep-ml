import numpy as np
import math

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    
    def norms(mat, frob = False):
        if mat.ndim not in (1, 2): raise ValueError()

        l1, l2, linf = 0.0, 0.0, 0.0
        
        if mat.ndim == 2:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    l1 += abs(mat[i][j])
                    l2 += float(mat[i][j]) ** 2
                    linf = max(linf, abs(mat[i][j]))
        else:
            if frob: raise ValueError()
            
            for i in range(len(mat)):
                l1 += abs(mat[i])
                l2 += float(mat[i]) ** 2
                linf = max(linf, abs(mat[i]))
        
        return (float(l1), math.sqrt(l2), float(linf))
    
    match norm_type:
        case "l1":
            return norms(arr)[0]
        case "l2":
            return norms(arr)[1]
        case "linf": 
            return norms(arr)[2]
        case "frobenius":
            return  norms(arr, frob = True)[1]
        case _:
            raise ValueError()
    













