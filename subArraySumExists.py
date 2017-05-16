# @param A : array of positive and negative numbers
# @n       : desired sum
# @return true if such sum exists, false otherwise
def subArraySumExists(A, n):
    if len(A) == 0:
        return False
    if len(A) == 1:
        if A[0] == n:
            return True
        else:
            return False
    prev_sums = {}
    curr_sum = 0
    for i in range(0, len(A)):
        curr_sum += A[i]
        if curr_sum == n:
            return True
        if (curr_sum - n) in prev_sums:
            return True
        prev_sums[curr_sum] = i
    return False

A = (1, 3, -1, -3, 5, 3, 6, 7)
B = (-1, 4, 20, 3, 10, 5)
C = (10,2,-2,-20,10)
D = (-10, 0, 2, 2,-20,10)

print subArraySumExists(A, 10)
print subArraySumExists(A, 4003)
print subArraySumExists(B, 33)
print subArraySumExists(C, -10)
print subArraySumExists(D, 20)