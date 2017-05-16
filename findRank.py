class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A) == 0:
            return 1
        first_chr = A[0]
        n = 0 # this is the number of letters with smaller lexical score
        for i in xrange(1, len(A)):
            print 'current letter: ' + A[i]
            if A[i] < first_chr:
                n += 1
        print 'A: ' + A + ' n: ' + str(n)
        # print self.factorial(len(A))
        return n * self.factorial(len(A) - 1) + self.findRank(A[1:])



    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

