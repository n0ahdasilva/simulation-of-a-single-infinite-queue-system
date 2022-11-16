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
import theoretical as th


# Generating a list of random numbers for random values needed in simulation.
def exp_rand_num_gen(seed=1, rate=1, size=1):
    r.seed(seed)    # Setting the seed for predicable results.
    return list(r.exponential(scale=1/rate, size=size))


def main():
    arg_err_msg = "Please specify the value of λ (arrival rate), μ (service rate), and k (parallel servers) with syntax 'lambda=λ', 'mu=μ', and 'k=k'. (i.e. 'python3 -u main.py lambda=1,2,3 mu=3 k=2')"
    # Check for needed arguments when the file is executed.
    try:
        args_dict= {}
        # Go through each given argument, start at second argument (first is the filename).
        for arg in argv[1:]:
            # Split the argument as name and value.
            arg_split = arg.split('=')
            # Check for the values' name, if there is a match, set the value.
            if arg_split[0] == 'lambda':
                LAMBDA = list(map(float, arg_split[1].split(',')))
            elif arg_split[0] == 'mu':
                MU = float(arg_split[1])
            elif arg_split[0] == 'k':
                k = int(arg_split[1])
            # If argument does not match wanted names, inform the user of issue.
            else:
                sys_exit(arg_err_msg)
    # Try will fail if user did not input proper argument values (float vs int vs char).
    except:
        sys_exit(arg_err_msg)

    simulation_avg_n_packets = []
    simulation_avg_queue_delay = []
    simulation_avg_waiting_time = []

    theoretical_avg_n_packets = []
    theoretical_avg_queue_delay = []
    theoretical_avg_waiting_time = []
    
    sim_data = a.NetworkSimulationAnalytics

    # Initiate the simulation class with appropriate data arrays.
    for lmbd in LAMBDA:
        netsim = ns.NetworkSimulation(
            interarrival_time=[0] + exp_rand_num_gen(seed=5, rate=lmbd, size=99_999),
            service_time=exp_rand_num_gen(seed=13, rate=MU, size=100_000),
        )
        results = netsim.simulate(
            BUFFER=-1,
            SERVER_NUM=k,
        )

        simulation_avg_n_packets.append(sim_data.\
            average_number_of_packets_in_system(results['time_spent_in_system'], 
                                                results['departure_time']))
        simulation_avg_queue_delay.append(sim_data.\
            average_queuing_delay(results['queue_delay']))

        simulation_avg_waiting_time.append(sim_data.\
            average_time_spent_in_system(results['time_spent_in_system']))
        
        th_data = th.TheoreticalEquations(LAMBDA=lmbd, MU=MU, k=k)
        theoretical_avg_n_packets.append(th_data.L())
        theoretical_avg_queue_delay.append(th_data.Wq())
        theoretical_avg_waiting_time.append(th_data.W())

    netsim_graph = a.NetworkSimulationGraphs

    netsim_graph.average_number_of_packets_in_system(
        arrival_rates=LAMBDA,
        theoretical_results=theoretical_avg_n_packets,
        simulation_results=simulation_avg_n_packets
    )
    netsim_graph.average_queuing_delay(
        arrival_rates=LAMBDA,
        theoretical_results=theoretical_avg_queue_delay,
        simulation_results=simulation_avg_queue_delay
    )
    netsim_graph.average_waiting_time_delay(
        arrival_rates=LAMBDA,
        theoretical_results=theoretical_avg_waiting_time,
        simulation_results=simulation_avg_waiting_time
    )

    print(th.TheoreticalEquations(LAMBDA=1, MU=4, k=k).L())
    print(th.TheoreticalEquations(LAMBDA=3, MU=4, k=k).L())
    print(th.TheoreticalEquations(LAMBDA=5, MU=4, k=k).L())
    print(th.TheoreticalEquations(LAMBDA=7, MU=4, k=k).L())
    print()
    print(th.TheoreticalEquations(LAMBDA=1, MU=4, k=k).Wq())
    print(th.TheoreticalEquations(LAMBDA=3, MU=4, k=k).Wq())
    print(th.TheoreticalEquations(LAMBDA=5, MU=4, k=k).Wq())
    print(th.TheoreticalEquations(LAMBDA=7, MU=4, k=k).Wq())
    print()
    print(th.TheoreticalEquations(LAMBDA=1, MU=4, k=k).W())
    print(th.TheoreticalEquations(LAMBDA=3, MU=4, k=k).W())
    print(th.TheoreticalEquations(LAMBDA=5, MU=4, k=k).W())
    print(th.TheoreticalEquations(LAMBDA=7, MU=4, k=k).W())
    print()


# Execute the program.
if __name__ == '__main__':
    main()