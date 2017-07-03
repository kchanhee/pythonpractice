class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        tree = [0, {}]
        for s in A:
            node = tree
            node[0] += 1
            for c in s:
                node = node[1].setdefault(c, [0, {}])
                node[0] += 1
        l = []
        for s in A:
            prefix = ''
            node = tree
            for c in s:
                if node[0] <= 1:
                    l.append(prefix)
                    break
                prefix += c
                node = node[1][c]
            else:
                l.append(s)
        return l

s = Solution()
x = ["zebra", "dog", "dove", "duck"]

print s.prefix(x)