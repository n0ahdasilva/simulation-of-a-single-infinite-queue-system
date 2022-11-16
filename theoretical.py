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

    def p(self):
        return self.LAMBDA / self.MU

    def P0(self):
        summation = 0
        for n in range(self.k):
            summation += ((self.LAMBDA / self.MU) ** n) / factorial(n)
        return (summation + (((self.LAMBDA / self.MU) ** self.k) * self.k * self.MU) / \
            (factorial(self.k) * ((self.k * self.MU) - self.LAMBDA))) ** -1

    def C(self):
        return (self.k * (self.p() ** self.k) * self.P0()) / \
            (factorial(self.k) * (self.k - self.p()))

    def Lq(self):
        if self.k >= 2:
            return (self.LAMBDA * self.C()) / \
                ((self.MU * self.k) - self.LAMBDA)
        else:
            return self.LAMBDA * self.Wq()

    def Wq(self):
        if self.k >= 2:
            return self.Lq() / self.LAMBDA
        else:
            if self.p() != 1:
                return self.p() / (self.MU - self.LAMBDA)

    def W(self):
        if self.k >= 2:
            return self.Wq() + (1 / self.MU)

    def L(self):
        if self.k >= 2:
            return self.LAMBDA * self.W()
        else:
            return (self.LAMBDA / self.MU) + self.Lq()