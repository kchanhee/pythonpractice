class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        # even = B % 2 == 0
        n = len(A)
        i = 0
        j = 1

        # base failure case
        if A[-1] < B:
            return 0
        while i < n and j < n:
            if i != j and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
            
        return 0