#consume metro transit API
import sys
import requests
import time
import argparse
'''
sample input
Bus_Route = "METRO Blue Line"
Bus_Stop_Name = "Target Field Station Platform 1"
Direction = "south"

sample command line inits
python3 main.py "METRO Blue Line" "Target Field Station Platform 1" "north"
python3 main.py "METRO Blue Line" "Target Field Station Platform 1" "south"

'''

#function that gets the route_id from a given bus route 
def get_route_id(Bus_Route) :
    all_routes = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    all_routes = all_routes.json()
    for item in all_routes:
        if Bus_Route in item["route_label"] :
            return item["route_id"]
            

#get direction_id from /directions/route_id, 0 = north/east, 1 = south/west
#cheating on direction, could easily implement similar legit queries with tighter input control

#function that gets direction_id from direction string, no API query necessary
def get_direction_id(direction) :
    direction = direction.lower()
    if direction in 'northbound' or direction in 'eastbound':
        return "0"
    elif direction in 'southbound' or direction in 'westbound': 
        return "1"
    else :
        raise RuntimeError("invalid direction parameter")

#get placecode from stop description, route_id and direction
def get_place_code(stop_name, route_id, direction_id) :
    all_stops_on_route = requests.get("https://svc.metrotransit.org/nextripv2/stops/{}/{}".format(route_id, direction_id))
    all_stops_on_route = all_stops_on_route.json()
    for item in all_stops_on_route :
        if stop_name in item["description"] :
            return item["place_code"]
            

#final function to get time to next departure given a route_id, direction_id, and place_code        
def time_to_next_bus(route_id, direction_id, place_code) :
    response = requests.get("https://svc.metrotransit.org/nextripv2/{}/{}/{}".format(route_id, direction_id, place_code))
    response = response.json()
    if response["departures"] == [] :
        sys.exit("No more departures for this route from this stop.")
    next_departure_time = response["departures"][0]["departure_time"]
    current_time = time.time()
    return "Next departure in {} minutes".format(int((next_departure_time-current_time)//60))  

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Bus_Route")
    parser.add_argument("Bus_Stop_Name")
    parser.add_argument("Direction")
    arguments = parser.parse_args()
    inputs = vars(arguments)
    #parsed arguments -> dictionary of arguments
    
    route_id = get_route_id(inputs["Bus_Route"])
    direction_id = get_direction_id(inputs["Direction"])
    place_code = get_place_code(inputs["Bus_Stop_Name"], route_id, direction_id)
    print(time_to_next_bus(route_id, direction_id, place_code))

