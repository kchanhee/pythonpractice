class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A) == 1:
            if A[0] > 0:
                return A
            else:
                return []
        # dictionary of {idx_start_A:[a_i,a_i+1, ...]}
        d = dict()
        l = list()
        for i in range(0, len(A)):
            if A[i] < 0: # negative: check if sum higher than the prev dictionary entry
                if len(d) == 0:
                    # add the new dictionary entry
                    b = l
                    d[i - 1 - len(l)] = b
                elif sum(l) > sum(d.values()[0]): # New sum is greater than all reset the dictionary and add the new object
                    d.clear()
                    b = l
                    d[i - 1] = b
                elif sum(l) == sum(d.values()[0]) and len(l) > len(d.values()[0]): # equal to previous sum and is longer than the the previous list
                    d.clear()
                    b = l
                    d[i - 1] = b
                l = []
            else: # append the elements to the new list
                l.append(A[i])
        else:
            if len(d) == 0:
                    # add the new dictionary entry
                    b = l
                    d[i - 1 - len(l)] = b
                    l = []
            elif sum(l) > sum(d.values()[0]): # New sum is greater than all reset the dictionary and add the new object
                d.clear()
                d[i - 1] = l
                l = []
                # print d
            elif sum(l) == sum(d.values()[0]) and len(l) > len(d.values()[0]): # equal to previous sum and is longer than the the previous list
                d.clear()
                d[i - 1] = l
                l = []
        return d.values()[0]

