class MinStack:
    elems = []
    import sys
    mins = []

    def __init__(self):
        self.elems = []
        self.mins = []
    # @param x, an integer
    def push(self, x):
        if len(self.elems) == 0:
            self.elems.append(x)
            self.mins.append(x)
        else:
            self.elems.append(x)
            if x < self.mins[-1]:
                self.mins.append(x)
            else:
                self.mins.append(self.mins[-1])

    # @return nothing
    def pop(self):
        if len(self.elems) > 0:
            self.elems.pop()
            self.mins.pop()


    # @return an integer
    def top(self):
        if len(self.elems) > 0:
            return self.elems[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.elems) > 0:
            return self.mins[-1]
        else:
            return -1

