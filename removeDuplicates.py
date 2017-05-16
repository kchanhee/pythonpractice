class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        idx = 0
        i = 1
        while i < len(A):
            if A[i] == A[idx]:
                start, fin = self.searchRange(A,A[i])
                print 'start_i: ' + str(start) + ' end_i: ' + str(fin)
                del A[start:fin]
                print A
                print fin - start
                continue
            else: # different number => delete the previous stuff
                idx = i
            i += 1
        return len(A)

    def searchRange(self, A, B):
        n = len(A)
        i = 0
        j = n - 1
        occ1 = -1
        occ2 = -1
        while i <= j:
            mid = (i + j) / 2
            if A[mid] == B:
                occ1 = mid
                j = mid - 1
            elif A[mid] < B:
                i = mid + 1
            else:
                j = mid - 1

        if occ1 < 0:
            return [-1, -1]
        i = occ1
        j = n - 1
        while i <= j:
            mid = (i + j) / 2
            if A[mid] == B:
                occ2 = mid
                i = mid + 1
            elif A[mid] < B:
                i = mid + 1
            else:
                j = mid - 1
        if occ2 < 0:
            return [occ1, occ1]
        else:
            return [occ1, occ2]