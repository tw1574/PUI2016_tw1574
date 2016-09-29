## PUI2016_tw1574
## HW2
For this homework, I was unfortunately away, so I had to complete it on my own, but I hope to be able to work with others, and help others on future assignments.  The specifics of the assignments are below

### Assignment 1 - tracking each vehicle for a line
This assignment is a python script that takes exactly 2 arguments (MTA_KEY and BUS_LINE).  It then fetches data from the MTA website through the SIRI API using the provided key and returns information on all available vehicles for the bus line (e.g. B52). 

It outputs the following to the console:
```
- the bus name, 
- the number of vehicles
- their current position
```

### Assignment 2 - next stop information
This assignment is a python script that takes exactly 3 arguments (MTA_KEY, BUS_LINE, and BUS_LINE_CSV).  It then fetches data from the MTA website through the SIRI API using the provided key and returns information on the next stop location of all busses of a given line. 

For buses that do not have this information, “N/A” is set as the output in the stop information fields

The output is in the following format and is written to the specified CSV file:
```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```
