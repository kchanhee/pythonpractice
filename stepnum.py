class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        nums = []
        for i in xrange(A,B + 1):
            if isStepNum(i):
                nums.append(i)
        return nums


def isStepNum(num):
    if num < 10:
        return True
    for i in xrange(1, len(str(num))):
        if abs(int(str(num)[i]) - int(str(num)[i-1])) != 1:
            return False
    return True