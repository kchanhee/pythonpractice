class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        N = [0 for x in xrange(len(A))]
        A = map(int,list(A))
        if A[0] > 0:
            N[0] = 1
        for i in xrange(1,len(A)):
            if A[i] > 0:
                N[i] += N[i-1]
            if A[i-1]*10 + A[i] <= 26 and A[i-1]*10 + A[i] >= 10:
                if i == 1:
                    N[i] += 1
                else:
                    N[i] += N[i-2]
        return N[len(A)-1]


num1 = "12"
num2 = "123456"
s = Solution()
print s.numDecodings(num1)
print s.numDecodings(num2)
