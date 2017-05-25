import numpy
import sys
from PIL import Image

def getImage(image):
    img = Image.open(image)
    pix = img.load()
    return pix

def paintBucket(bitmap, row, col, oldcolor, newcolor, visited = None):
    if visited is None:
        visited = set()
    if (row,col) in visited:
        return
    if bitmap[row][col] != oldcolor:
        return
    if row < 0 and row >= len(bitmap):
        return
    if col < 0 and col >= len(bitmap[row]):
        return
    print(row,col)
    bitmap[row][col] = newcolor
    
    visited.add((row,col))

    paintBucket(bitmap, row - 1, col, oldcolor, newcolor, visited)
    paintBucket(bitmap, row + 1, col, oldcolor, newcolor, visited)
    paintBucket(bitmap, row, col - 1, oldcolor, newcolor, visited)
    paintBucket(bitmap, row, col + 1, oldcolor, newcolor, visited)

def printList(bitmap):
    for row in bitmap:
        print(row)


# bitmap = numpy.array(0)
bitmap = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]
# og_image = Image.open("smallCircle.png")
# og_image.show()
MAX_X, MAX_Y = len(bitmap), len(bitmap[0])
print(MAX_X, MAX_Y)
printList(bitmap)
# print(bitmap[MAX_X/2][MAX_Y/2])
# print(bitmap[MAX_X/2][MAX_Y/2])

paintBucket(bitmap, int(MAX_X / 2), int(MAX_Y / 2), 0, 8)
printList(bitmap)
# img = Image.fromarray(bitmap)
# img.show()