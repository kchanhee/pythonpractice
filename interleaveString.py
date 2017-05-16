class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    # def isInterleave(self, A, B, C):
    #     if len(C) == 1:
    #         return (len(B) > 1 and B[0] == C[0]) or (len(A) > 1 and A[0] == C[0])
    #     elif len(A) > 1 and len(B) > 1:
    #         return (C[0] == A[0] or self.isInterleave(A[1:],B,C[1:])) or (C[0] == B[0] or self.isInterleave(A,B[1:],C[1:]))
    #     elif len(A) > 1:
    #         return (C[0] == A[0] or self.isInterleave(A[1:],B,C[1:]))
    #     elif len(B) > 1:
    #         return (C[0] == B[0] or self.isInterleave(A,B[1:],C[1:]))
    def isInterleave(self, A, B, C):
        if len(C) == 0:
            return True
        a_path = False
        b_path = False
        if len(A) != 0 and C[0] == A[0]:
            a_path = self.isInterleave(A[1:], B, C[1:])
        if len(B) != 0 and C[0] == B[0]:
            b_path = self.isInterleave(A, B[1:], C[1:])
        return a_path or b_path

a = "abcdef"
b = "ddeded"
c = "abcdefddeded"
c1 = "abddedcdeedf"

c2 = "ddededadbcef"

s = Solution()
print s.isInterleave(a,b,c) # should work
print s.isInterleave(a,b,c1) # should work
print s.isInterleave(a,b,c2) # should fail
