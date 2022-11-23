#
#   PROJECT : Simulation of a Single Infinite Queue System
# 
#   FILENAME : theoretical.py
# 
#   DESCRIPTION :
#       Simulate a single infinite queue system with two parallel servers, 
#       using Little’s law equations to verify the correctness of implementation.
# 
#   FUNCTIONS :
#       main()
# 
#   NOTES :
#       - ...
# 
#   AUTHOR(S) : Noah Arcand Da Silva    START DATE : 2022.10.11 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.10.11  Noah            Creation of project.
#


from math import e
from math import factorial


class TheoreticalEquations:
    def __init__(self, LAMBDA=None, MU=None, k=None):
        self.LAMBDA = LAMBDA
        self.MU = MU
        self.k = k

        self._p = None
        self._P0 = None
        self._C = None
        self._Lq = None
        self._Wq = None
        self._W = None
        self._L = None
        
    def p(self):
        self._p = self.LAMBDA / self.MU

        return self._p

    def P0(self):
        summation = 0
        for n in range(self.k):
            summation += ((self.LAMBDA / self.MU) ** n) / factorial(n)

        self._P0 = (summation + (((self.LAMBDA / self.MU) ** self.k) * self.k * self.MU) / \
            (factorial(self.k) * ((self.k * self.MU) - self.LAMBDA))) ** (-1)
 
        return self._P0

    def C(self):
        if self._p is None:
            self.p()
        if self._P0 is None:
            self.P0()

        self._C = (self.k * (self._p ** self.k) * self._P0) / \
            (factorial(self.k) * (self.k - self._p))

        return self._C

    def Lq(self):
        if self._C is None:
            self.C()
        if self._p is None:
            self.p()

        if self.k >= 2:
            self._Lq = (self.LAMBDA * self._C) / \
                ((self.MU * self.k) - self.LAMBDA)
        else:
            self._Lq = (self._p ** 2) / (1 - self._p)

        return self._Lq

    def Wq(self):
        if self._Lq is None:
            self.Lq()
        if self._p is None:
            self.p()

        if self.k >= 2:
            self._Wq = self._Lq / self.LAMBDA
        else:
            self._Wq = self._p / (self.MU - self.LAMBDA)

        return self._Wq

    def W(self):
        if self._Wq is None:
            self.Wq()

        if self.k >= 2:
            self._W = self._Wq + (1 / self.MU)
        else:
            self._W = 1 / (self.MU - self.LAMBDA)

        return self._W

    def L(self):
        if self._W is None:
            self.W()
        if self._Lq is None:
            self.Lq()

        if self.k >= 2:
            self._L = self.LAMBDA * self._W
        else:
            self._L = (self.LAMBDA / self.MU) + self._Lq

        return self._L