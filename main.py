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
#       exp_rand_num_gen()
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
from sys import argv
from sys import exit as sys_exit

import network_simulation as ns
import analytics as a


# Generating a list of random numbers for random values needed in simulation.
def exp_rand_num_gen(seed=1, rate=1, size=1):
    r.seed(seed)    # Setting the seed for predicable results.
    return list(r.exponential(scale=1/rate, size=size))


def main():
    arg_err_msg = "Please specify the value of λ (arrival rate) and μ (service rate) with syntax 'lambda=λ' and 'mu=μ'. (i.e. 'python3 -u main.py lambda=1 mu=3')"
    # Check for needed arguments when the file is executed.
    if len(argv) != 3:
        sys_exit(arg_err_msg)

    # Verify if the first argument is either our lambda or mu, then verify if the last argument is the other.
    # If there is no match, or any formatting errors, end the program and inform the user.
    try:
        match argv[1].split('=')[0]:
            case 'lambda':
                LAMBDA = list(map(float, argv[1].split('=')[1].split(',')))
                match argv[2].split('=')[0]:
                    case 'mu':
                        MU = float(argv[2].split('=')[1])
                    case _:
                        sys_exit(arg_err_msg)
            case 'mu':
                MU = float(argv[1].split('=')[1])
                match argv[2].split('=')[0]:
                    case 'lambda':
                        LAMBDA = list(map(float, argv[2].split('=')[1].split(',')))
                    case _:
                        sys_exit(arg_err_msg)
            case _:
                sys_exit(arg_err_msg)
    except:
        sys_exit(arg_err_msg)

    avg_n_packets = []
    avg_queue_delay = []
    avg_waiting_time = []
    netsim_data = a.NetworkSimulationAnalytics
    # Initiate the simulation class with appropriate data arrays.
    for l in LAMBDA:
        netsim = ns.NetworkSimulation(
            interarrival_time=[0] + exp_rand_num_gen(seed=5, rate=l, size=99_999),
            service_time=exp_rand_num_gen(seed=13, rate=MU, size=100_000),
        )
        results = netsim.simulate(
            BUFFER=-1,
            SERVER_NUM=2,
        )

        avg_n_packets.append(netsim_data.\
            average_number_of_packets_in_system(results['time_spent_in_system'], 
                                                results['departure_time']))
        avg_queue_delay.append(netsim_data.\
            average_queuing_delay(results['queue_delay']))

        avg_waiting_time.append(netsim_data.\
            average_time_spent_in_system(results['time_spent_in_system']))

    netsim_graph = a.NetworkSimulationGraphs

    netsim_graph.average_number_of_packets_in_system(
        arrival_rates=LAMBDA,
        theoretical_results=[1,1,1,1,1,1],
        simulation_results=avg_n_packets
    )
    netsim_graph.average_queuing_delay(
        arrival_rates=LAMBDA,
        theoretical_results=[1,1,1,1,1,1],
        simulation_results=avg_queue_delay
    )
    netsim_graph.average_waiting_time_delay(
        arrival_rates=LAMBDA,
        theoretical_results=[1,1,1,1,1,1],
        simulation_results=avg_waiting_time
    )


# Execute the program.
if __name__ == '__main__':
    main()