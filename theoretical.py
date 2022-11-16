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


class TheoreticalVerification:
    def __init__(self, LAMBDA, MU, K):
        self.LAMBDA = LAMBDA
        self.MU = MU
        self.K = K

    def results(self):

        return