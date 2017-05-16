class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = self.mergeSort(A)
        for i in range(0, len(A), 2):
            # print i
            if i == len(A) - 1:
                return A
            A[i], A[i+1] = A[i+1], A[i]

        return A

    # @param L : list of integers
    # @return a list of integers sorted
    def mergeSort(self, L):
        if len(L) < 2:
            return L
        else:
            result = []
            left = L[:len(L)/2]
            right = L[len(L)/2:]
            # print left
            # print right

            left = self.mergeSort(left)
            right = self.mergeSort(right)

            i = 0
            j = 0
            while  i < len(left) and j < len(right):
                if (left[i] <= right[j]):
                    # print left[i], right[j]
                    result.append(left[i])
                    # print "result: " + str(result)
                    i += 1
                else:
                    # print left[i], right[j]
                    result.append(right[j])
                    # print "result: " + str(result)
                    j += 1

            result += left[i:]
            result += right[j:] 
            return result

