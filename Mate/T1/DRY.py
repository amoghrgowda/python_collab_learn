import math

class QuadRoots:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def _root(self, sign):
        d = self.b**2 - 4*self.a*self.c
        return (-self.b + sign * math.sqrt(d)) / (2 * self.a)

    def root1(self):
        return self._root(+1)

    def root2(self):
        return self._root(-1)