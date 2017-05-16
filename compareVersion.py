class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a_list = A.split('.')
        b_list = B.split('.')
        m = len(a_list)
        n = len(b_list)
        # start at the left most number
        i = 0
        while i < m and i < n:
            # print a_list[i]
            # print b_list[i]
            if cmp(a_list[i], b_list[i]) != 0:
                return cmp(int(a_list[i]), int(b_list[i]))
            i += 1
        else:
            if m > n:
                if a_list[i] != '0':
                    return 1
                else:
                    return 0
            if m < n:
                if b_list[i] != '0':
                    return -1
                else:
                    return 0
            else:
                return 0
