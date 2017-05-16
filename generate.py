class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        L = []
        if A == 1:
            return [1]
        if A == 2:
            return [[1], [1,1]]
        L = [[1], [1,1]]
        for i in range(1, A - 1):
            L.append(self.newList(L[i]))
        return L

    # Given two sequences in pascals' triangle:
    # return the next sequence
    def newList(self, A):
        L = [1] * (len(A) + 1)
        for i in range(1, len(A)):
            # if len(A) == 2:
            #     L[i] = A[i - 1] + A[i]
            #     return L
            L[i] = A[i - 1] + A[i]
        return L

s = Solution()
