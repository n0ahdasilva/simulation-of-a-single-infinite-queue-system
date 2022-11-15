#
#   PROJECT : Simulation of a Single Infinite Queue System
# 
#   FILENAME : simulation.py
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


class SingleInfiniteServerQueue:
    # Setting initial availability states for the servers.
    _server_1_availability = True
    _server_2_availability = True

    def __init__(self, interarrival_time=[0], service_time=[1]):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
    
    def simulation():
        pass