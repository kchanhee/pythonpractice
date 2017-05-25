class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

A = [1, 2, 3, 4, 5, 6]
B = [1, 0, 0, 0, 0, 1]
s = Solution()

print s.maxArea(A)
print s.maxArea(B)