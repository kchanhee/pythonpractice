class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        # Formula is Sum of (A - i) C (i) from i = 0 to A / 2
        numSteps = 0
        for i in xrange(0, A / 2 + 1):
            numSteps += self.nCr(A - i, i)
            print 'For ( ' + str(A - 2 * i) + ' ones and ' + str(i) + ' twos): ' + str(self.nCr(A - i, i))

        return numSteps
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
    # @param n : integer
    # @return combination
    def nCr(self, n, r):
        if n == 0:
            return 0
        else:
            a = 1
            for i in xrange(n, n - r, -1):
                # print i
                a *= i
            return a / self.factorial(r)
