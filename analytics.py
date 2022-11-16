#
#   PROJECT : Simulation of a Single Infinite Queue System
# 
#   FILENAME : analytics.py
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


import matplotlib.pyplot as plt


class NetworkSimulationAnalytics:
    def average_queuing_delay(queue_delay):
        return sum(queue_delay) / len(queue_delay)

    def average_time_spent_in_system(time_spent_in_system):
        return sum(time_spent_in_system) / len(time_spent_in_system)
        
    def waiting_probability(queue_delay):
        num_waiting_packets = 0
        for i in queue_delay:
            if i != 0:
                num_waiting_packets += 1
        return num_waiting_packets / len(queue_delay)

    def average_number_of_packets_in_system(time_spent_in_system, departure_time):
        return sum(time_spent_in_system) / departure_time[-1]


class NetworkSimulationGraphs:
    def average_number_of_packets_in_system(arrival_rates=None, 
                                            theoretical_results=None, 
                                            simulation_results=None):
        plt.clf()
        plt.style.use('ggplot')
        # Plotting the data.
        plt.plot(
            arrival_rates,
            theoretical_results,
            label='Theoretical Results',
            color='sandybrown',
        )
        plt.plot(
            arrival_rates,
            simulation_results,
            label='Simulation Results',
            color='cornflowerblue',
        )
        # Formatting for visuals
        plt.title('Average Number of Packets in the System vs. Arrival Rate')
        plt.xlabel('Arrival rate (λ)')
        plt.ylabel('Average number of packets (L)')
        plt.legend()
        # Save graph for accessible reference.
        plt.savefig('graphs/' 'avg_num_packets_in_sys' + '.svg')

    def average_queuing_delay(arrival_rates=None, 
                              theoretical_results=None, 
                              simulation_results=None):
        plt.clf()
        plt.style.use('ggplot')
        # Plotting the data.
        plt.plot(
            arrival_rates,
            theoretical_results,
            label='Theoretical Results',
            color='sandybrown',
        )
        plt.plot(
            arrival_rates,
            simulation_results,
            label='Simulation Results',
            color='cornflowerblue',
        )
        # Formatting for visuals
        plt.title('Average Queuing Delay vs. Arrival Rate')
        plt.xlabel('Arrival rate (λ)')
        plt.ylabel('Average Queing Delay (Wq)')
        plt.legend()
        # Save graph for accessible reference.
        plt.savefig('graphs/' 'avg_queuing_delay' + '.svg')

    def average_waiting_time_delay(arrival_rates=None, 
                                   theoretical_results=None, 
                                   simulation_results=None):
        plt.clf()
        plt.style.use('ggplot')
        # Plotting the data.
        plt.plot(
            arrival_rates,
            theoretical_results,
            label='Theoretical Results',
            color='sandybrown',
        )
        plt.plot(
            arrival_rates,
            simulation_results,
            label='Simulation Results',
            color='cornflowerblue',
        )
        # Formatting for visuals
        plt.title('Average Waiting Time Delay vs. Arrival Rate')
        plt.xlabel('Arrival rate (λ)')
        plt.ylabel('Average Waiting Time (W)')
        plt.legend()
        # Save graph for accessible reference.
        plt.savefig('graphs/' 'avg_waiting_time' + '.svg')