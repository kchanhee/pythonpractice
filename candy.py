class Solution:
    # @param ratings : list of integers
    # @return an integer
    def candy(self, ratings):
    	num = [1] * len(ratings)
    	for i in range(1, len(ratings)):
    		if ratings[i] > ratings[i-1]:
    			num[i] = num[i - 1] + 1
    	
    	for i in reversed(xrange(len(num) - 1)):
    		if ratings[i] > ratings[i + 1]:
    			num[i] = max(num[i], num[i + 1] + 1)
    	
    	print ratings
    	print num


    	return sum(num)

r1 = [1,2,3,4,5,6]
r2 = [1,2,3,2,3]
r3 = [5,6,5,3,2,1]
s = Solution()
print s.candy(r1)
print s.candy(r2)
print s.candy(r3)