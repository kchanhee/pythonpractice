class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A[-1] += 1
        # if len(A) == 1:
        #     return A
        # Need to handle the significant figures at beginning
        carry = False # if 9 carry over 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == 10:
                carry = True
                A[i] = 0
            else:
                if carry:
                    A[i] += 1
                    carry = False
                    if A[i] == 10:
                        A[i] = 0
                        if i != 0:
                            carry = True
                        else:
                            A.insert(0, 1)

        return strip_leading_zero(A)



def strip_leading_zero(A):
    while True:
        if A[0] == 0:
            del A[0]
        else:
            # this is an actual number we want to keep so return the array
            return A


A = [0, 0, 0, 0, 1, 0, 3, 4]
# A = [9, 9, 9, 9, 9]

print Solution().plusOne(A)