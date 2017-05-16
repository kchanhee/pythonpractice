class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        for p in self.permute2(A):
            print p
        # return 


            

    # @param A: Array
    # @param i: index
    # @return array with elements at i, i+1 swapped.
    def permute1(A, i = 0):
        if i + 1 >= len(A):
            yield A
        else:
            for p in permute1(A, i + 1):
                yield p
            for k in range(i + 1, len(A)):
                A[i], A[k] = A[k], A[i]
                for p in permute1(A, i+1):
                    yield p
                A[i], A[k] = A[k], A[i]

    def permute2(xs, low=0):
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in permute(xs, low + 1):
                yield p        
            for i in range(low + 1, len(xs)):        
                xs[low], xs[i] = xs[i], xs[low]
                for p in permute(xs, low + 1):
                    yield p        
                xs[low], xs[i] = xs[i], xs[low]

A = [1, 2, 3]
s = Solution()
for p in s.permute2(A):
    print p