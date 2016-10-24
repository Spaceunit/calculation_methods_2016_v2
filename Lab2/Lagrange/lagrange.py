import matrix
import math
class Lagrange:
    def __init__(self):
        self.m = matrix.Matrix([], "Matrix 2x2")
        self.m.makedimatrix(2)
        self.l = 0
    def set_l(self, i):
        self.l = (float(1) / float(1)) * self.m.getminor2(0, 0, vh_r=None)
        pass