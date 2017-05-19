class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        n = len(A)-1
        m = len(A[0])-1
        mat= [[0 for i in xrange(102)] for j in xrange(102)]
        for i in xrange(n+1):
            if A[i][0] == 0:
                mat[i][0] = 1
        mat[n][m+1] = 1
        for r in xrange(n,-1,-1):
            for c in xrange(m,-1,-1):
                if A[r][c] == 0:
                    mat[r][c] = mat[r+1][c] + mat[r][c+1]
        return mat[0][0]