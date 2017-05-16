def nextSmallInt(A):
    if len(A) == 1:
        return A[0] + 1
    elif len(A) == 2:
        if abs(A[0] - A[1]) > 1:
            return min(A[0],A[1]) + 1
        else:
            return max(A[0],A[1]) + 1

    d = dict()


    min_val = A[0]
    max_val = A[1]
    next_min = 0

    for i in A:
        d[i] = True
        # print str(max_val)
    for i in range(1, len(A) + 1):
        if i == 0:
            continue
        if not i in d:
            return i
    else:
        if not i in d:
            return i
        else:
            return i+1

def O_1_smallInt(A):
    if len(A) == 1:
        if A[0] != 1:
            return 1
        return A[0] + 1
    # elif len(A) == 2:
    #     if abs(A[0] - A[1]) > 1:
    #         return min(A[0],A[1]) + 1
    #     else:
    #         return max(A[0],A[1]) + 1
    for i in range(0,len(A)):
        print "A[i] = " + str(abs(A[i]) - 1)
        print abs(A[i]) - 1 
        if (abs(A[i]) - 1 < len(A)) and (A[abs(A[i]) - 1] > 0):
            A[abs(A[i]) - 1] = -A[abs(A[i]) - 1]

    for i in range(0,len(A)):
        if A[i] > 0:
            return i + 1
    else:
        return len(A) + 1

