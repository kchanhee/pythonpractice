class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        num = 0 # Number of times a switch is turned on
        while(sum(A) < len(A)): # once all elements are 1's the sum should equal length
            i = 0 # left-most 0 idx
            if A[i] == 0: # found a zero iterate through the rest of thing
                num += 1
                for j in xrange(len(A) - 1, -1, -1):
                    A[j] ^= 1
                    if A[j] == 0:
                        i == j
            else:
                i += 1
                

