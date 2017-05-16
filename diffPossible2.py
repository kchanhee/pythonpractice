class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 2:
            return 0
        d = {}
        for i in A:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in A:
            d1 = i - B
            d2 = B + i
            if (d1 >= 0 and d1 in d) or (d2 in d):
                if B == 0:
                    if d[i] >= 2:
                        return 1
                else:
                    return 1

            elif d2 in d:
                return 1
            elif i in d:
                del d[i]

        return 0


# A = '11 85 100 44 3 32 96 72 93 76 67 93 63 5 10 45 99 35 13'
# A = map(int,A.split(''))

