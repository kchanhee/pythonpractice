
def maxArea(A):
    area = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                continue
            new_area = min(A[i], A[j]) * abs(A[i] - A[j])
            if new_area >= area:
                area = new_area
    return area