#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Jennie Bahramian (Jennie.bahramian@duke.edu)
# Date:   Fall 2026
#--------------------------------------------------------------
  
#Create the geographic selection box
the_box = {
    "x_min" : 34.0,
    "y_min" : -76.0,
    "x_max" : 34.5,
    "y_max" : -75.00
}

# Copy and paste a line of data as the lineString variable value
lineString = '10154641232,true,2019-05-14 13:37:52.000,-75.49356999999998,34.86216,,0.0,-127.0,4.0167976787E8,5141.0,424,"40",34.86216,34.86216,"0",-75.49356999999998,-75.49356999999998,6,0,3,61.0,381.0,10718.0,2466.0,150,187,2,0,"1",,,"argos-doppler-shift","Pterodroma hasitata","174441","HA09","Satellite tracking of black-capped petrels, 2019"'
    
# Use the split command to parse the items in lineString into a list object
line_data = lineString.split(',')
  
# Assign variables to specfic items in the list
event_id = line_data[0]   # Argos tracking event ID ("event-id")
timestamp = line_data[2]  # Observation date ("timestamp")
lat = float(line_data[4])        # Observation latitude  ("location-lat")
lon = float(line_data[3])        # Observation longitude ("location-lon")
lc  = line_data[14]        # Observation location class ("argos:lc")
tag_id = line_data[-3]     # Tag identifier ("tag-local-identifier")

#Evaluate latiturde and lignitude conditions
lat_condition = the_box['y_min'] < lat < the_box['y_max']
lon_condition = the_box['x_min'] < lon < the_box['x_max']

#Report the status of the points
if lat_condition & lon_condition:
    print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
else:
    print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')