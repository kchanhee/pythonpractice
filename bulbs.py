class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        return self.bulbsHelper(A, 0)
        # return num

    def bulbsHelper(self, A, state):
        if state in A: # checking if state is in A (should be all 1 or 0 depending)
            first_idx = A.index(state)
            return 1 + self.bulbsHelper(A[(first_idx + 1):], int(not state))
        else:
            return 0


