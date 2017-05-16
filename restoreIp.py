class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        A = A.strip()
        n = len(A)
        if n > 12 and n < 4:
            return []
        ret = []
        i = 1
        while i <= 3 and i < n:
            j = i+1
            while j <= i + 3 and j < n:
                k = j + 1
                while k <= j + 3 and k < n:
                    #print A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:]
                    a = int(A[:i])
                    b = int(A[i:j])
                    c = int(A[j:k])
                    d = int(A[k:])
                    if (A[0] == '0' and (i > 1or a != 0)) or (A[i] == '0' and (j > i+1 or b != 0)) or (A[j] == '0' and (k > j + 1 or c != 0)) or (A[k] == '0' and (n > k+1 or d != 0)):
                        # Do Nothing
                        k += 1
                        continue
                    elif a <= 255 and a >= 0 and b <= 255 and b >= 0 and c <= 255 and c >= 0 and d <= 255 and d >= 0:
                        ret.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
                    k += 1
                j += 1
            i += 1
        return ret