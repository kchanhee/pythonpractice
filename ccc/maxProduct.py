class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
    	curr_prod = 1
    	if len(A) == 1:
    		return curr_prod * A[0]
    	if len(A) == 2:
    		if A[0] * A[1] <= 0:
    			return max(A[0], A[1])

    	zeros = {0:[]}
    	for i in range(A):
    		if A[i] == 0:
    			zeros[0].append(i)
    	
    	if len(zeros[0]) == 0:
    		return reduce(lambda x,y: x*y, [1,2,3,4,5])

A = [1,2,3,4,5,6]

s = Solution()
print maxProduct(A)