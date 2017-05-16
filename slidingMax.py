from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        queue = deque()
        if B > len(A):
            return [max(A)]
        maxVals = []
        for i in range(0, len(A) - B + 1):
            print queue
            if i == 0:
                queue.extend(A[i:i + B])
                maxVals.append(max(queue))
            else: #pop left most value on queue and add the next element
                popped = queue.popleft()
                new_val = A[i + B - 1]
                queue.append(new_val)
                if new_val > maxVals[-1]:
                    maxVals.append(new_val)
                elif popped == maxVals[-1]:
                    maxVals.append(max(queue))
                else:
                    maxVals.append(maxVals[-1])
        return maxVals



s = Solution()
A = (1, 3, -1, -3, 5, 3, 6, 7)
B = 3

print s.slidingMaximum(A, B)