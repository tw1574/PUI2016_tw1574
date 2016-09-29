# Author: Tyler Woebkenberg, NYU, September 2016
##############################
# Code written for HW2 of PUI2016
# https://github.com/tw1574/PUI2016_tw1574/tree/HW2_tw1574
##############################
# include your MTA Key and preferred bus line as input arguments:
# run the code as
#      python show_bus_locations.py <MTA_KEY> <BUS_LINE>

# the code will be compatible in both python2 and python3
from __future__ import print_function
# the next import allows me to read line input arguments
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# this line checks how many arguments are passed to python
# with the MTA Key and bus line in input it will be a list of 3
if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]

print (mta_key)
print ("Bus Line : ", bus_line)

response = urllib.urlopen("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line)
data = response.read().decode("utf-8")
bus = json.loads(data)

active_buses = (len(bus["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))

print ("Number of Active Buses : ", active_buses)

bus_num = 0
for b in (bus["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]):
    bus_num += 1
    lat = (b["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
    lon = (b["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
    print ("Bus", bus_num, "is at Latitude", lat, "and Longitude", lon)

# http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=205fc806-c752-4def-a376-c7885aa84ee6&VehicleMonitoringDetailLevel=calls&LineRef=B52
