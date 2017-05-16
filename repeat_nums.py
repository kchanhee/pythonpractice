# Given arr of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times
# Find these repeating numbers in O(n) and using only constant memory space.
def findDup(A):
    d = {}
    ret_arr = []
    for i in A:
        if i in d:
            ret_arr.append(i)
        else:
            d[i] = 1
    return ret_arr

# 
def findDup1(Arr):
    size = len(Arr)
    for i in range(0,size):
        idx = Arr[i] % size
        Arr[idx] += size
    for i in range(0,size):
        if Arr[i] / size > 1:
            print i
    

A = [4,2,0,5,2,1,0,1]
B = [1,2,3,3,2,5]

print A
findDup1(A)
# print A

print B 
findDup1(B)