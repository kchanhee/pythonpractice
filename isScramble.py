from collections import Counter
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B, dp={}):
        if (not A) or (not Counter(A) == Counter(B)):
            return 0
        if A == B:
            return 1
        if A not in dp:
            dp[A] = {}
        if B not in dp[A]:
            dp[A][B] = int(
                            any([
                                    (
                                        (
                                            self.isScramble(A[:i], B[:i], dp)
                                            and
                                            self.isScramble(A[i:], B[i:], dp)
                                        )
                                        or
                                        (
                                            self.isScramble(A[:i], B[-i:], dp)
                                            and
                                            self.isScramble(A[i:], B[:-i], dp)
                                        )
                                    )
                                    for i in xrange(len(B))
                                ])
                            )
        return dp[A][B]