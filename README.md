# NextBus_MetroTransit
This python script accesses realtime data from the nextripv2 API to compute the time until the next departure from any stop or route in the Metro Transit system. 

Link to the API: https://svc.metrotransit.org/

## Installation
With python3 installed, clone the repository and install pip3 then the requests module.
```
git clone https://github.com/JamesE-T/NextBus_MetroTransit.git
cd NextBus_MetroTransit
sudo apt install python3-pip
python3 -m pip install requests
```
## How To Run 
Inputs can be sub-strings if they are sufficiently specific. BUS_ROUTE & BUS_STOP_NAME are case-sensitive. 
```
# Calling the program
python3 main.py "BUS_ROUTE" "BUS_STOP_NAME" "DIRECTION"

# Example Call
python3 main.py "METRO Blue Line" "Target Field Station Platform 1" "north"

```
The program should print "Next departure in X minutes." where X is an integer, upon successful retrieval of real time data.

### How to run tests
within /NextBus_MetroTransit, run the following command to run tests
```
python3 -m unittest main_test.py
```
## Limitations and next steps
Given the type-sensitivity of two of the inputs, in current form the script is not designed for user ease of use.  
Direction_id is found not by querying the API but based on knowledge of the existing API. Should the API change, the script will no longer function as intended. 
In future iterations these issues should be improved upon, and overall design choices reconsidered.
