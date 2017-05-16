from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        n = len(A)
        minimums = A[n - 1]
        
        for row in reversed(xrange(n - 1)):
            for col, value in enumerate(A[row]):
                minimums[col] = min(minimums[col], minimums[col + 1]) + value
        
        return minimums[0] 

def makeTriangle(A):
    d = deque(A)
    i = 1
    triangle = []
    while len(d) > 0:
        row = []
        for j in range(0, i):
            row.append(d.popleft())
        triangle.append(row)
        i += 1
    return triangle
A = [[2],[1,4],[4,5,6]]
B = [[2],[1,4],[4,5,6],[5,7,2,9]]

A = makeTriangle([2,1,4,4,5,6,7,8,9,7])
print A
s = Solution()
print s.minimumTotal(A)
