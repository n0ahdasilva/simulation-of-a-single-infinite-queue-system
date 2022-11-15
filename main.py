#
#   PROJECT : Simulation of a Single Infinite Queue System
# 
#   FILENAME : main.py
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


from numpy import random as r
from re import findall
from sys import argv
from sys import exit as sys_exit

import network_simulation as ns

# Generating a list of random numbers for random values needed in simulation.
def exponential_random_number_generation(seed=1, rate=1, size=1):
    r.seed(seed)    # Setting the seed for predicable results.
    return list(r.exponential(scale=1/rate, size=size))


def main():
    arg_err_msg = "Please specify the value of λ and μ with syntax 'lambda=λ' and 'mu=μ'."
    # Check for needed arguments when the file is executed.
    if len(argv) != 3:
        sys_exit(arg_err_msg)

    # Verify if the first argument is either our lambda or mu, then verify if the last argument is the other.
    # If there is no match, or any formatting errors, end the program and inform the user.
    try:
        match argv[1].split('=')[0]:
            case 'lambda':
                LAMBDA = float(argv[1].split('=')[1])
                match argv[2].split('=')[0]:
                    case 'mu':
                        MU = float(argv[2].split('=')[1])
                    case _:
                        sys_exit(arg_err_msg)
            case 'mu':
                MU = float(argv[1].split('=')[1])
                match argv[2].split('=')[0]:
                    case 'lambda':
                        LAMBDA = float(argv[2].split('=')[1])
                    case _:
                        sys_exit(arg_err_msg)
            case _:
                sys_exit(arg_err_msg)
    except:
        sys_exit(arg_err_msg)

    # Initiate the simulation class with appropriate data arrays.
    simulation = ns.SingleInfiniteServerQueue(
        interarrival_time=[0] + exponential_random_number_generation(seed=13, rate=LAMBDA, size=100_000)[1:],
        service_time=exponential_random_number_generation(seed=5, rate=MU, size=100_000),
    )


if __name__ == '__main__':
    main()