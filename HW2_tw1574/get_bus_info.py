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
if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info.py <MTA_KEY> <BUS_LINE> <BUS_LINE_CSV>")
    sys.exit()

mta_key = sys.argv[1]
bus_line = sys.argv[2]
bus_line_csv = sys.argv[3]

fout = open(bus_line_csv, "w")

print ("Latitude, Longitude, Stop Name, Stop Status")
fout.write("Latitude, Longitude, Stop Name, Stop Status\n")

response = urllib.urlopen("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line)
data = response.read().decode("utf-8")
bus = json.loads(data)

for b in (bus["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]):
    lat = (b["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"])
    lon = (b["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
    stop_name = (b["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]) or "N/A"
    stop_status = (b["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]) or "N/A"

    line = str(lat) + ", " + str(lon) + ", " + str(stop_name) + ", " + str(stop_status)
    print (line)
    fout.write(line + "\n")

# http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=205fc806-c752-4def-a376-c7885aa84ee6&VehicleMonitoringDetailLevel=calls&LineRef=B52
