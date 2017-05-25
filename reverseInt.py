class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_num = 0
        is_neg = False
        if x < 0:
            x *= -1
            is_neg = True
        while x > 0:
            rev_num *= 10
            rev_num += x % 10
            x /= 10
            # print x
        if is_neg:
            rev_num *= -1
        return rev_num


s = Solution()
print s.reverse(100)
print s.reverse(-123)
print s.reverse(1534236469)