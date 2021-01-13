import googlemaps
import time
import json
import re
import os

# Placeholder variable; in order to get an API key,
# request Google maps geocoding key from the Google Cloud developer console
gmaps = googlemaps.Client(key='GEOCODE_MAPS_KEY')

# get branch data
old_branch_arr = []
with open("branch_data.json", "r") as read_file:
    old_branch_arr = json.load(read_file)
    
new_branch_arr = []
for branch in old_branch_arr:
	geocode_result = gmaps.geocode(branch.get("fields").get("branch_name"))
	branch_object = {
		"pk": branch.get("pk"),
		"model": branch.get("model"),
		"fields": {
		    "branch_name": branch.get("fields").get("branch_name"),
		    "branch_info": branch.get("fields").get("branch_info"),
		    "lng": geocode_result[0].get("geometry").get("location").get("lng"),
		    "lat": geocode_result[0].get("geometry").get("location").get("lat"),
		},
	    }
	new_branch_arr.append(branch_object)
	
with open('branch_data_with_loc.json', 'w') as outfile:
    json.dump(new_branch_arr, outfile)

