class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        L = [1] * (A + 1)
        for i in range(1, A / 2 + 1):
            L[i] = self.comb(A, i)
            L[A - i] = self.comb(A, i)
        return L

    def comb(self, n, k):
        if n == k or k == 0:
            return 1
        n_k = n - k
        x = 1
        y = 1
        i = n
        j = k
        if n_k < k:
            while i > n_k:
                x *= i
                i -= 1
            while j > 1:
                y *= j
                j -= 1
            return x / y
        else:
            j = n_k
            while i > k:
                x *= i
                i -= 1
            while j > 1:
                y *= j
                j -= 1
            return x / y

s = Solution()