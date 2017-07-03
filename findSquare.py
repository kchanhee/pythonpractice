def findSquare(N):
    sq = 0
    for i in xrange(N):
        sq += N
    return sq

nums = [3, 5, 100, 1000, 15]
for n in nums:
    sq = findSquare(n)
    print "Square of %d = %d. Should be %d | Test Passed: %r" % (n, sq, n * n, sq == n * n)
