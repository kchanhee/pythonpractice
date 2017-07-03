class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1 and A[0] == 1:
            return 0
        elif len(A) == 1 and A[0] == 0:
            return 1
        count = 0
        for i in range(len(A)):
            if A[i] == 0:
                count += 1
                A = convertBulb(A, i)
            print A
        return count

def convertBulb(A, idx):
    while idx < len(A):
        A[idx] ^= 1
        idx += 1
    return A

s = Solution()
X = [[0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [0,1,0,1],
    [1,1,1,1]]
for x in X:
    print s.bulbs(x)