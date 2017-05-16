class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        m = len(A[0]) # number of columns
        n = len(A) # of rows
        b_coords = {} # black coordinates
        w_coords = {} # white coordinates
        num_shapes = 0
        for i in xrange(0, m):
            for j in xrange(0, n):
                if A[i][j] == 'X' and (i,j) not in b_coords.keys():
                    bs_coords, ws_coords = self.getFullShape(b_coords, w_coords, (i,j))
                    b_coords.update(bs_coords) 
                    w_coords.update(ws_coords)

    # @params b_coords : current dictionary of black coordinates so we don't do double work
    # @params w_coords : current dictionary of white coordinates so we don't do double work
    # @params curr_coord : current coordinate
    # @params A : matrix A
    # @returns: updated new black & white coordinates, and the shape

    def getFullShape(self, b_coords, w_coords, curr_coord, A):
        # we go up down left right and go recursively to find the shape
        x, y = curr_coord
        if x < len(A) - 1: # can go right
