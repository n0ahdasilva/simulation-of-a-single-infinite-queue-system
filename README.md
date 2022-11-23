# simulation-of-a-single-infinite-queue-system
The objective is to simulate a single infinite queue system with two parallel servers, using Little’s law equations to verify the correctness of implementation.

## How to run
To run the simulation, you'll need to specify the arrival rate(s) and the service rate. I.e.:

`python3 -u main.py lambda=1,2,3,4,5 mu=3 k=2`

Graphs will generate in the `/graphs` directory where the program is located.