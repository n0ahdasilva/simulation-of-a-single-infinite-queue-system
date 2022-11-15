import numpy as np
import matplotlib.pyplot as plt

# Total # of packets to generate and process
packetTotal = 100000

# Parameters used for time generation
serviceRate = 4
interArrivalSeed = 5
serviceTimeSeed = 13
sampleSize = packetTotal

# Arrays for times
interArrivals = [0]      #ri
serviceTimes = []       #si
arrivalTimes = [None] * packetTotal      #ai
delayQueue = [None] * packetTotal        #di
departureTimes = [None] * packetTotal     #ci
waitTime = [None] * packetTotal    #wi

# Function to generate interarrival and service times
def generateTimes(seed, num, var, times):
    np.random.seed(seed)                                    # Set random generator seed
    
    for x in range (num):   
        times.append(np.random.exponential(1/var))          # Generate random exponential value for time

# Function to plot graphs
def Plot_Graph(actual, theoretical, graph): 
    serviceRates = [1,3,5,7]
    
    plt.plot(serviceRates, actual, label = 'Actual')
    plt.plot(serviceRates, theoretical, label = 'Theoretical')
    
    if graph == 0:
        plt.xlabel('Arrival Rates (Lambda)')
        plt.ylabel('Avg # Packets (L)')
        plt.title('Average # of packets vs Arrival Rate')
    elif graph == 1:
        plt.xlabel('Arrival Rates (Lambda)')
        plt.ylabel('Avg Queueing Delay (Wq)')
        plt.title('Average Queueing Delay vs Arrival Rate')
    elif graph == 2:
        plt.xlabel('Arrival Rates (Lambda)')
        plt.ylabel('Avg Wait Time (W)')
        plt.title('Average Wait Time vs Arrival Rate')        
    
    plt.legend()
    plt.show()
    return

def simulation(arrivalRateSel):
    # Parameters used for time generation
    arrivalRate = arrivalRateSel
    serviceRate = 4
    interArrivalSeed = 5
    serviceTimeSeed = 13
    sampleSize = packetTotal
    
    # Arrays for times
    interArrivals = [0]      #ri
    serviceTimes = []       #si
    arrivalTimes = [None] * packetTotal      #ai
    delayQueue = [None] * packetTotal        #di
    departureTimes = [None] * packetTotal     #ci
    waitTime = [None] * packetTotal    #wi
            
    # Populate interarrival and service time arrays
    generateTimes(interArrivalSeed, sampleSize-1, arrivalRate, interArrivals)   
    generateTimes(serviceTimeSeed, sampleSize, serviceRate, serviceTimes)

    # Variables to keep track of the time when each respective server is free
    # Initially, server1 will be busy until the first packet is processed (service time of packet 1). Server2 is set to 0, meaning it is free starting at time 0
    server1 = serviceTimes[0]
    server2 = 0
    
    # Set the interarrival, arrival, and delay of first packet to 0
    interArrivals[0] = 0
    arrivalTimes[0] = 0
    delayQueue[0] = 0
    
    # Populate arrivalTimes array and keep a running simulation clock
    m = 0
    clock = 0.0                                         # begin clock at time 0
    for timeTemp in interArrivals:                      # loop through all interarrival times in array
        if m == 0:
            m += 1
            continue
        clock += timeTemp                               # Aggregate interarrival times to get resulting arrival time of packet
        arrivalTimes[m] = clock                         # Store arrival time in array
        m+= 1

    # Departure time of first packet is simply its arrival time + service time. Has zero delay time because it is the first packet to be processed
    departureTimes[0] = arrivalTimes[0] + serviceTimes[0]
    waitTime[0] = delayQueue[0] + serviceTimes[0]
    #print(f'\n({arrivalTimes[0]})Server 1 processing packet #0')              # DEBUGGING OUTPUT
    #print(f'Packet #0 processed. Delay: {delayQueue[0]}, Wait in the system:{waitTime[0]}, Departure Time: {departureTimes[0]}')              # DEBUGGING OUTPUT
    
    # Main simulation begins here
    for x in range(1,packetTotal):
        # First scenario, either servers are free so packet experiences zero delay. Server 1 by default has higher priority so it processes the packet
        if server1 <= arrivalTimes[x] or server2 <= arrivalTimes[x]:
            delayQueue[x] = 0
            waitTime[x] = serviceTimes[x]
            departureTimes[x] = arrivalTimes[x] + serviceTimes[x]

            #Set server1 and server2 times for next iteration
            # If server1 is free and will be processing packet, set its next available time to the departure time of the current packet, else, set server2 time to departure time            
            if server1 <= arrivalTimes[x]:
                #print(f'\n({arrivalTimes[x]})Server 1 processing packet #{x}')              # DEBUGGING OUTPUT
                server1 = departureTimes[x]
                #print(f'Packet #{x} processed. Delay: {delayQueue[x]}, Wait in system: {waitTime[x]}, Departure Time: {departureTimes[x]}')              # DEBUGGING OUTPUT
            else:
                #print(f'\n({arrivalTimes[x]})Server 2 processing packet #{x}')              # DEBUGGING OUTPUT
                server2 = departureTimes[x]
                #print(f'Packet #{x} processed. Delay: {delayQueue[x]}, Wait in system: {waitTime[x]}, Departure Time: {departureTimes[x]}')              # DEBUGGING OUTPUT
        
        # Server 1 handles packet
        elif server1 <= server2:
            #print(f'\n({arrivalTimes[x]})Server 1 processing packet {x}')              # DEBUGGING OUTPUT
            delayQueue[x] = server1 - arrivalTimes[x]
            waitTime[x] = delayQueue[x] + serviceTimes[x]
            departureTimes[x] = arrivalTimes[x] + waitTime[x]
            server1 = departureTimes[x]
            #print(f'{departureTimes[x]}Packet #{x} processed. Delay: {delayQueue[x]}, Wait in system: {waitTime[x]}, Departure Time: {departureTimes[x]}')              # DEBUGGING OUTPUT
        
        # Server 1 busy, server 2 handles packet
        else:
            #print(f'\n({arrivalTimes[x]})Server 2 processing packet {x}')              # DEBUGGING OUTPUT
            delayQueue[x] = server2 - arrivalTimes[x]
            waitTime[x] = delayQueue[x] + serviceTimes[x]
            departureTimes[x] = arrivalTimes[x] + waitTime[x]
            server2 = departureTimes[x]
            #print(f'{departureTimes[x]}Packet #{x} processed. Delay: {delayQueue[x]}, Wait in system: {waitTime[x]}, Departure Time: {departureTimes[x]}')              # DEBUGGING OUTPUT

    # Calculations 
    avgPackets = np.sum(waitTime)/departureTimes[-1]
    avgDelay = np.average(delayQueue)
    avgWait = np.average(waitTime)
    
    print(f"Average number of packets in system (L): {avgPackets}")
    print(f"Average queueing delay (Wq): {avgDelay}")
    print(f"Average wait time (W): {avgWait}\n")
    
    return avgPackets, avgDelay, avgWait
    

def main():
    avgNum = [None] * 4
    avgDelays = [None] * 4
    avgWait = [None] * 4
    
    # Output statistics, Arrival rate is selected by passing value to the simulation() function
    print('Lambda 1')
    avgNum[0], avgDelays[0], avgWait[0] = simulation(1)
    
    print('Lambda 3')
    avgNum[1], avgDelays[1], avgWait[1] = simulation(3) 
    
    print('Lambda 5')  
    avgNum[2], avgDelays[2], avgWait[2] = simulation(5)
    
    print('Lambda 7')
    avgNum[3], avgDelays[3], avgWait[3] = simulation(7)
    
    '''
    # Debug outputs
    print(f'\nInterarrival times: {interArrivals}\n\n')
    print(f'Arrival times: {arrivalTimes}\n\n')
    print(f'Service times: {serviceTimes}\n\n')
    print(f'Delay in queue time: {delayQueue}\n\n')
    print(f'Departure times: {departureTimes}\n\n')
    print(f'Wait times: {waitTime}\n\n')'''


    # Plot graphs
    # Actual simulation results
    #avgNum = [0.25262656392305005, 0.8672622834555496, 2.0390617078100877, 7.260780606452373]
    #avgDelays = [0.0039072255997701509, 0.04047999449257847, 0.15956430900741356, 0.7909089754473486]
    #avgWait = [0.2533778366363794, 0.28995060553125634, 0.4090349200460915, 1.0403795864860264]
    
    # Calculated theoretical results
    theoreticalNum = [0.253968, 0.872727, 2.05128, 7.46669]
    theoreticalDelay = [0.003968, 0.040909, 0.160256, 0.81667]
    theoreticalWait = [0.253968, 0.290909, 0.410256, 1.06667]
    
    Plot_Graph(avgNum, theoreticalNum, 0)
    Plot_Graph(avgDelays, theoreticalDelay, 1)
    Plot_Graph(avgWait, theoreticalWait, 2)  
    
if __name__ == "__main__":
    main()