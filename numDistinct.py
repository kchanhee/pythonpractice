class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        matches = [1] + [0] * len(T)
        for i in range(len(S)):
            for j in reversed(range(len(T))):
                if T[j] == S[i]:
                    matches[j+1] += matches[j]
        return matches[-1]

S = "122333345"
T = "123"
s = Solution()
print s.numDistinct(S,T)
