class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        # convert to binary
        b = "{0:b}".format(A)
        if b.count('1') > 1:
            return 0
        else:
            return 1
    