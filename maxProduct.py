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

    	zeros = []
    	for i in range(len(A)):
    		if A[i] == 0:
    			zeros.append(i)

    	if len(zeros) == 0:
    		return reduce(lambda x,y: x*y, [1,2,3,4,5])

    	for i in range(1,len(zeros)):
    		print zeros[i]
    		print A[zeros[i-1]+1:zeros[i]]
    		curr_prod = max(curr_prod, reduce(lambda x,y: x*y, A[zeros[i-1]+1:zeros[i]]))

    	return curr_prod


    	



A = (1,2,3,4,5,6)
B = (1,0,0,0,1)
C = (0,1,2,3,4,0)
s = Solution()
print s.maxProduct(C)