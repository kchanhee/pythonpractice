class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    # def reverse(self, A):
    #     a = "{0:b}".format(A)
    #     x = ''
    #     for i in range(0, 32):
    #         if i <= len(a) - 1:
    #             x += a[len(a) - 1 - i]
    #         else:
    #             x += '0'
    #     return int(x, 2)
    def reverse(self, A):
            i = 31
            ret = 0
            while i >= 0:
                temp = ((A & 1<<i) >> i)&1
                ret = ret | temp << (31-i)
                i -= 1
            return ret