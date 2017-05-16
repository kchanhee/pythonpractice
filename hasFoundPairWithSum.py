def hasFoundPairWithSum(arr, s):
    if len(arr) < 2:
        return False
    left_idx = 0
    right_idx = len(arr) - 1
    while left_idx < right_idx:
        if arr[left_idx] + arr[right_idx] == s:
            return True
        elif arr[left_idx] + arr[right_idx] < s:
            left_idx += 1
        else:
            right_idx -= 1
    return False

def hasFoundPairWithSumNotSorted(arr, s):
    if len(arr) < 2:
        return False 
    seen = {}
    for i in arr:
        if s - i in seen:
            return True
        else:
            seen[i] = True
    return False


A = [1, 2, 3, 9]
B = [1, 2, 4, 4]
C = [2, 4, 5, 3]
D = [4, 4, 5, 1]
print hasFoundPairWithSum(A, 8)
print hasFoundPairWithSum(B, 8)

print hasFoundPairWithSumNotSorted(C, 8)
print hasFoundPairWithSumNotSorted(D, 8)