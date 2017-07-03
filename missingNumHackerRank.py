

# t = int(raw_input().strip())

# def printList(L):
#     for line in L:
#         print line

# missing = []]


n = int(raw_input().strip())
arr1 = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
arr2 = map(int,raw_input().strip().split(' '))

max_num = max(arr1 + arr2)

missingList = [0] * (max_num + 1)
for a in arr1:
    missingList[a] += 1

for b in arr2:
    missingList[b] -= 1

vals = [y for y in range(len(missingList)) if missingList[y] != 0]
for v in vals:
    print v