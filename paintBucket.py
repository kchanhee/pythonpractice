# Given a 2D bitmap picture, program a paint bucket tool:
import numpy
import sys
from PIL import Image
MAX_X = 0
MAX_Y = 0
pixmap = numpy.array(0)
def getImage(image):
    img = Image.open(image)
    pix = numpy.array(img) # this gives us the bitmap
    MAX_X, MAX_Y = img.size
    return pix
# recursion
def fillImage(x, y, oldColor, newColor):
    if (x,y) in S:
        return
    if list(pixmap[x][y]) != oldColor:
        return
    if y < 0 or y >= MAX_Y:
        print 'y = %d' % y + 'MAX_Y = %d' % MAX_Y
        return
    if x < 0 or x >= MAX_X:
        print 'x = %d' % x + 'MAX_X = %d' % MAX_X
        return
    pixmap[x][y] = newColor
    S.add((x,y))
    print 'x = %d' % x + ', y = %d' % y
    fillImage(x + 1, y, oldColor, newColor) # right
    fillImage(x - 1, y, oldColor, newColor) # left
    fillImage(x, y - 1, oldColor, newColor) # down
    fillImage(x, y + 1, oldColor, newColor) # up

pixmap = getImage("smallCircle.png")
og_image = Image.open("smallCircle.png")
og_image.show()
S = set()
MAX_X, MAX_Y = og_image.size
sys.setrecursionlimit(MAX_Y * MAX_X)
fillImage(MAX_X / 2, MAX_Y / 2, list(pixmap[MAX_X / 2][MAX_Y / 2]), numpy.array([255, 0, 0, 0], pixmap.dtype))
img = Image.fromarray(pixmap)
img.show()