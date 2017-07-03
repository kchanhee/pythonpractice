import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 4:
            return [2, 2]
        for n in range(3, A, 2):
            if isPrime(n) and isPrime(A - n):
                return [n, A - n]
            
def isPrime(n):
    if all(n % i != 0 for i in range(2, int(math.sqrt(n))+ 1)): 
        return True
    return False
s = Solution()
print s.primesum(10)
print s.primesum(100)
print s.primesum(44)
