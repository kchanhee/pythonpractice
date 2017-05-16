class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def removeElement(self, A, B):
    #     l = list()
    #     for i in A:
    #         if i != B:
    #             l.append(i)
    #         else: 
    #             continue
    #     A = l
    #     return A
    def removeElement(self, A, B):
        k = 0
        n = len(A)
        if n == 0:
            return A
        for i in range(n):
            if A[i] == B:
                k += 1
            elif k > 0:
                A[i-k] = A[i]
        A = A[:n-k]
        return n - k

# A = "2 0 1 2 0 3 2 2 2 1 0 0 0 1 0 0 2 2 2 3 2 3 1 2 1 2 2 3 2 3 0 3 0 2 1 2 0 0 3 2 3 0 3 0 2 3 2 2 3 1 3 3 0 3 3 0 3 3 2 0 0 0 0 1 3 0 3 1 3 1 0 2 3 3 3 2 3 3 2 2 3 3 3 1 3 2 1 0 0 0 1 0 3 2 1 0 2 3 0 2 1 1 3 2 0 1 1 3 3 0 1 2 1 2 2 3 1 1 3 0 2 2 2 2 1 0 2 2 2 1 3 1 3 1 1 0 2 2 0 2 3 0 1 2 1 1 3 0 2 3 2 3 2 0 2 2 3 2 2 0 2 1 3 0 2 0 2 1 3 1 1 0 0 3 0 1 2 2 1 2 0 1 0 0 0 1 1 0 3 2 3 0 1 3 0 0 1 0 1 0 0 0 0 3 2 2 0 0 1 2 0 3 0 3 3 3 0 3 3 1 0 1 2 1 0 0 2 3 1 1 3 2"
# A = map(int, A.split())
# B = 2
# C = "0 1 0 3 1 0 0 0 1 0 0 3 3 1 1 3 3 0 3 0 1 0 0 3 3 0 3 0 3 3 1 3 3 0 3 3 0 3 3 0 0 0 0 1 3 0 3 1 3 1 0 3 3 3 3 3 3 3 3 1 3 1 0 0 0 1 0 3 1 0 3 0 1 1 3 0 1 1 3 3 0 1 1 3 1 1 3 0 1 0 1 3 1 3 1 1 0 0 3 0 1 1 1 3 0 3 3 0 3 0 1 3 0 0 1 3 1 1 0 0 3 0 1 1 0 1 0 0 0 1 1 0 3 3 0 1 3 0 0 1 0 1 0 0 0 0 3 0 0 1 0 3 0 3 3 3 0 3 3 1 0 1 1 0 0 3 1 1 3"
# C = map(int, C.split())
# s = Solution()
# s.removeElement(A,B) == C
