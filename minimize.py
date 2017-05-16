# @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
def minimize(A, B, C):
    i,j,k = 0,0,0
    l,m,n = len(A),len(B),len(C)
    r = 2**31 - 1
    while i < l and j < m and k < n:
        tempMin = min(A[i],B[j],C[k])
        tempMax = max(A[i],B[j],C[k])
        r = min(r, tempMax - tempMin)
        if tempMin == A[i]:
            i += 1
        elif tempMin == B[j]:
            j += 1
        else:
            k += 1
    return r
