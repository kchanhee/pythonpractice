# @param A : string
    # @param B : integer
    # @return a strings
def convert(A, B):
    if B == 1:
        return A
    d = -1 # direction of zig-zag (1 for down, -1 for up)
    row = 0
    zig_dict = {k: '' for k in range(B)}
    # print zig_dict


    for i in range(len(A)):
        zig_dict[row] += A[i]
        if row == B - 1 or row == 0:
            d *= -1
        row += d
    n = ''
    for x in zig_dict.keys():
        # print x
        n += zig_dict[x]
    return n
