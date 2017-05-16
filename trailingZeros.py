class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):

        x = 5
        count = 0
        while x <= A:
            count += A / x
            x *= 5
        return count

        


def factorial(A):
    if A == 1:
        return 1

    f = 1
    for x in range(A, 1, -1):
        f *= x
    return f