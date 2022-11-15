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
'''
    def graph_plot(self, data, plot_title):
        # We want the packet number, i.e. 1, 2, 3, ...
        x_axis = [i for i in range(1, len(data) + 1)]
        # Create a bar graph for queuing delay of packets.
        plt.clf()
        plt.style.use('ggplot')
        plt.bar(x_axis, data, width=1, color='cornflowerblue')
        # Formatting 
        plt.title(plot_title)
        plt.xlabel('Packet number')
        plt.ylabel('Queueing delay (seconds)')
        plt.savefig('histograms/' + plot_title + '.png')'''