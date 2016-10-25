import matrix
import math
class Lagrange:
    def __init__(self):
        self.x = 0
        self.m = matrix.Matrix([], "Matrix 2x2")
        self.m.makedimatrix(2)
        self.l = 0

    def set_l(self, values):
        #values - matrix 2X2
        #Yi     Xi
        #Yi + 1 Xi - X
        self.m.setmatrix(values)
        self.l = (1.0 / float(self.m.getel(1, 1) - self.m.getel(0, 1))) * self.m.getminor2(0, 0, vh_r=None)

    def get_l(self):
        return self.l

    def set_x(self, x):
        self.x = x

    def difr(self, num):
        difference = num - self.x
        return difference