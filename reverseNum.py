class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        max_int = 2**31 - 1
        min_int = -max_int
        if abs(A) < 10: # single digit
            return A
        is_neg = False
        if A < 0:
            is_neg = True
        n = 1
        b = 10 # find the digits
        A = abs(A)
        while b < A:
            b *= 10
            n += 1
        newNum = 0
        for i in range(n - 1, -1, -1):
            newNum += (A / (10 ** i)) * (10 ** (n - 1 - i))
            if newNum > max_int:
                return 0
            # print newNum
            A -= (A / (10 ** i)) * 10 ** (i)
        if is_neg:
            return -newNum
        else:
            return newNum

s = Solution()
