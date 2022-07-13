#consume metro transit API
import sys
import requests
import time
import argparse
'''
Bus_Route = "METRO Blue Line"
Bus_Stop_Name = "Target Field Station Platform 1"
Direction = "south"
'''
#response = requests.get("https://svc.metrotransit.org/nextripv2/routes")

# function to carry out API GET requests
# build generalized function after working on individual get requests
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Bus_Route")
    parser.add_argument("Bus_Stop_Name")
    parser.add_argument("Direction")
    arguments = parser.parse_args()
#parsed arguments -> dictionary of arguments
inputs = vars(arguments)
  
def time_to_next_bus(route, direction, place) :
    response = requests.get("https://svc.metrotransit.org/nextripv2/{}/{}/{}".format(route, direction, place))
    response = response.json()
    next_departure_time = response["departures"][0]["departure_time"]
    current_time = time.time()
    return "{} minutes".format(int((next_departure_time-current_time)//60))  

#get route_id 
all_routes = requests.get("https://svc.metrotransit.org/nextripv2/routes")
all_routes = all_routes.json()
for item in all_routes:
    if inputs["Bus_Route"] in item["route_label"] :
        route_id = item["route_id"]
        print(route_id)
#route_id acquired, no error checking

#get direction_id from /directions/route_id, 0 = north/east, 1 = south/west

'''
route_directions = requests.get("https://svc.metrotransit.org/nextripv2/directions/{}".format(route_id))
for item in route_directions:
    if inputs["Direction"].lower() in item["direction_name"].lower() :
        direction_id = item["direction_id"]
        print(direction_id)
'''       
        #cheating on direction
if inputs["Direction"].lower() == 'north' or 'east':
    direction_id = 0
if inputs["Direction"].lower() == 'south' or 'west': 
    direction_id = 1
if direction_id is None :
    raise RuntimeError("invalid direction parameter")
print(direction_id)

#get placecode from stop description, route_id and direction
all_stops_on_route = requests.get("https://svc.metrotransit.org/nextripv2/stops/{}/{}".format(route_id, direction_id))
all_stops_on_route = all_stops_on_route.json()
for item in all_stops_on_route :
    if inputs["Bus_Stop_Name"] in item["description"] :
        place_code = item["place_code"]
        print(place_code)
        # no case checking still...
        
#now we have route_id, direction_id, and place_code!

print(time_to_next_bus(route_id, direction_id, place_code))
'''
    parser = argparse.ArgumentParser()
    parser.add_argument("Bus_Route")
    parser.add_argument("Bus_Soute_Name")
    parser.add_argument("Direction")
    arguments = parser.parse_args()
    print(time_to_next_bus(route_id, direction_id, place_code))
'''
#lets test first consuming the api hardcoded before accepting
#inputs, then move to inputting from the command line

#we will need to transform the input to one that is acceptable parameters for the api

#direction_id is 0 or 1, string direction_name: "Northbound"

#so we query /nextripv2/routes for the route_id, and find the similar one to the input string
#or we could expedite this by checking their input route string for a "Route XX" number and taking that as our route_id


# final query /nextripv2/route_id/direction_id/placecode
# get route_id number from bus number or compare string with api /nextripv2/routes
# get direction_id from /directions/route_id, could hardcode 0 = north/east, 1 =south/west
# get placecode from string compare description 

