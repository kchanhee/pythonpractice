import sys
class Solution:
    # @param A : string
    # @return an integer
    # def minCut(self, A):
    #     if isPalindrome(A):
    #         return 0
    #     num_cuts = sys.maxint
    #     for i in range(1, len(A)):
    #         if isPalindrome(A[0:i]): 
    #             num_cuts = min(num_cuts, self.minCut(A[i:]))
    #     return num_cuts + 1


    def minCut(self, s):
        if len(s) == 0: return 0
        n = len(s)
        dp = [[False for x in range(n)] for x in range(n)]
        d = [0 for x in range(n)]
        for i in range(n-1,-1,-1):
            d[i] = n-i-1
            for j in range(i,n):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j == n-1:
                        d[i] = 0
                    elif d[j+1] + 1 < d[i]:
                        d[i] = d[j+1] + 1
        return d[0]

palindrome_set = set()
def isPalindrome(s):
    if s in palindrome_set:
        return True
    if len(s) == 1:
        palindrome_set.add(s)
        return True
    for i in range(0,len(s) / 2):
        if s[i] != s[-i - 1]:
            return False
    palindrome_set.add(s)
    return True


s = Solution()
print s.minCut("abcdefg") == len("abcdefg")
print s.minCut("aaaaa") == 0
print s.minCut("aba") == 0
print s.minCut("abcedecba") == 0