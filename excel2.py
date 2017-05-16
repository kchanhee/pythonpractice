class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        from string import ascii_uppercase as au
        alpha_dic = {x : i for i, x in enumerate(au, 1)}
        s = 0
        for i in range(0, len(A)):
            # print i
            s += alpha_dic[A[i]] * 26 ** (len(A) - 1 - i)
        return s

print Solution().titleToNumber("AAAAA")