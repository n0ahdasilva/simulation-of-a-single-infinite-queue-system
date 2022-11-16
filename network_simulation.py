#
#   PROJECT : Simulation of a Single Infinite Queue System
# 
#   FILENAME : network_simulation.py
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


class NetworkSimulation:
    # Receiving data needed to run the simulation.
    def __init__(self, interarrival_time=[0], service_time=[1]):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
    
    # Simulation of a router with a buffer size of Y, X server, and a service rate of Z.
    # NOTE  BUFFER:         System capacity (How many packets are allowed to wait, -1 is infinity).
    #       SERVER_QUEUE:   Amount of queues for packets to be processed (number of servers).
    #       SERVICE RATE:   How many packets can be serviced per second.
    def simulate(self, BUFFER=-1, SERVER_NUM=1):
        try:
            # Since the first packet does not have an interarrival time, we need to initialize it
            # before we start the packet loop/simulation.
            clock_arrival_time = [0.0]
            time_service_begins = [0.0]
            queue_delay = [0.0]
            server_idle_time = [0.0]
            departure_time = [self.service_time[0]]
            time_spent_in_system = [self.service_time[0]]

            # Used to determine when a server will become available.
            server_time_of_availability = [0.0]*SERVER_NUM
            server_time_of_availability[0] = self.service_time[0]

            # Go through each iterable item in datasets, starting on second element.
            for i in range(1, len(self.service_time)):
                # Determine which server will first become available.
                first_available_server = min(server_time_of_availability)

                # Let's calculate the arrival time on clock.
                # Add the previous packet's clock time to the arrive time of the current packet.
                clock_arrival_time.append(self.interarrival_time[i] + clock_arrival_time[i - 1])
                
                # Let's calculate the queue delay.
                if (first_available_server - clock_arrival_time[i]) >= 0:
                    # If there is a queue, add it to the list.
                    queue_delay.append(first_available_server - clock_arrival_time[i])
                else:
                    # If not, append no delay.
                    queue_delay.append(0)

                # Let's increment the 'service time begins' counter. Store in list.
                time_service_begins.append(queue_delay[i] + clock_arrival_time[i])

                # Let's calculate the idle time of the server.
                for j in server_time_of_availability:
                    sum_of_idle_servers = 0
                    # Makes sure we have an idle time for each server.
                    if (time_service_begins[i] - j) > 0:
                        sum_of_idle_servers += (time_service_begins[i] - j)
                # Add the sum as the idle time of server(s).
                server_idle_time.append(sum_of_idle_servers)

                # Let's calculate the time spent in the system.
                time_spent_in_system.append(queue_delay[i] + self.service_time[i])

                # Let's increment the 'departure time' counter. Store in list.
                departure_time.append(clock_arrival_time[i] + time_spent_in_system[i])

                # Update the new server availability time.
                server_time_of_availability[server_time_of_availability.index(first_available_server)] = departure_time[-1]

        except:
            print('There was an error in the simulation.')

        # Return all of our data
        return  {
                'clock_arrival_time': clock_arrival_time,
                'time_service_begins': time_service_begins,
                'queue_delay': queue_delay,
                'server_idle_time': server_idle_time,
                'departure_time': departure_time,
                'time_spent_in_system': time_spent_in_system
                }