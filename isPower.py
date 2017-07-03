import math
class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return True
        # x ^ y

        for x in xrange(int(math.sqrt(A) + 1), 1, -1):
            if x % 2 == 0 and A % 2 != 0:
                # if A is odd base cannot be even
                continue
            elif x % 2 != 0 and A % 2 == 0:
                # if A is even base cannot be odd
                continue
            y = 2
            while x ** y <= A:
                if x ** y == A:
                    return True
                elif x ** y > A:
                    break
                y += 1
        return False

s = Solution()
for i in xrange(1,101):
    print "%d is a power: %r" % (i, s.isPower(i))