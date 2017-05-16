class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        # solve via Catalan numbers: 
        return binomialCoeff(2 * A, A) / (A + 1)
prevDict = {}
def binomialCoeff(n,k):
    # if k in prevDict.keys():
    #     return prevDict[k]
    result = 1
    if (k > n - k):
        k = n - l 
    
    for i in range(0,k):
        result *= n - i
        result /= i + 1
    # prevDict[k] = result
    return result

s = Solution()
print s.numTrees(1) == 1
print s.numTrees(2) == 2
print s.numTrees(3) == 5
print s.numTrees(4) == 14
print s.numTrees(5) == 42
print s.numTrees(6) == 132
