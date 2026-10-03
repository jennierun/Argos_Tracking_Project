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

#Create a variable pointing to the data file
file_name = 'data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv'

#Read the contents of the file into a list of lines
with open(file_name,'r') as f:
    #Read contents of file into a list
	line_list = f.readlines()

#Pretend we read one line of data from the file
for lineString in line_list[1:]:

    # Use the split command to parse the items in lineString into a list object
    line_data = lineString.split(',')
    
    # Assign variables to specfic items in the list
    event_id = line_data[0]   # Argos tracking event ID ("event-id")
    timestamp = line_data[2]  # Observation date ("timestamp")
    lc  = line_data[14]        # Observation location class ("argos:lc")
    if lc not in ['"1"','"2"','"3"']: continue
    lat = float(line_data[4])        # Observation latitude  ("location-lat")
    lon = float(line_data[3])        # Observation longitude ("location-lon")
    tag_id = line_data[-3]     # Tag identifier ("tag-local-identifier")
    
    #Evaluate latitude and longitude conditions
    lat_condition = the_box['y_min'] < lat < the_box['y_max']
    lon_condition = the_box['x_min'] < lon < the_box['x_max']

    #Report the status of the points
    if lat_condition & lon_condition:
        print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
    else:
        print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')