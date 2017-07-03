#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    arr_set = set(a)
    answer = set()
    for i in a:
        if (i - k) in arr_set:
            answer.add((i, i - k))
        if (i + k) in arr_set:
            answer.add((i + k, i))
    return len(answer)


# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
