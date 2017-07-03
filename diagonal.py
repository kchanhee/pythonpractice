class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        n = len(a)
        diags = []

        # for i in xrange(2 * n - 1):
        #     curr = []
        #     for j in xrange(i % n + 1):
        #         curr.append(A[i % n - j][j])
        #     diags.append(curr)
       
        for j in xrange(n):
            curr = []
            for i in xrange(j + 1):
                curr.append(a[i][j - i])
            diags.append(curr)

        for i in xrange(n - 1):
            curr = []
            for j in xrange(i + 1, n):
                curr.append(a[j][n - j + i])
            diags.append(curr)

        return diags

def printMat(mat):
    for line in mat:
        print line

s = Solution()
import random
for i in xrange(2,10):
    A = [[random.randint(0,9) for n in range(i)] for m in range(i)]
    print "--------- Matrix ------------"
    printMat(A)
    print "-------- Anti-Diag ----------"
    printMat(s.diagonal(A))

