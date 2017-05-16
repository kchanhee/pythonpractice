# @param A : list of integers
# @return an integer
def removeDuplicates(A):
    # count = 1 # if 2 set to 1 again
    curr = A[0]
    i = 1
    while i < len(A):
        # print 'i = %d, A[%d] = %d' % (i, i, A[i])

        print 'Remove A[%d] = %d' % (i, A[i])
        start, fin = searchRange(A, A[i])
        del A[start+1:fin]   
        i += 1
    # print A
    return len(A)

            
def searchRange(A, B):
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
