import json
import urllib2
import re
from math import radians, cos, sin, asin, sqrt  
from haversine import haversine
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCnXTXPt3cXDjVmP-PLcA3dvhlIC9KPs_E')

city_name_dict = {
	"georgetown": "Washington, dc",
	"gwu": "Washington, dc",
	"howard" : "Washington, dc",
	"american" : "Washington, dc",
	"cornell" : "Ithaca, ny",
	"dartmouth" : "Dartmouth, nh",
	"yale" : "New Haven, ct",
	"princeton" : "Princeton, nj",
	"brown" : "Providence, ri",
	"colgate" : "Hamilton, ny",
	}

cityCoordinateDict = {
	'colgate': '42.8270136,-75.5446238',
	'georgetown': '38.9071923,-77.0368707',
	'brown': '41.8239891,-71.4128343',
	'cornell': '42.4439614,-76.5018807',
	'princeton': '40.3572976,-74.6672226',
	'howard': '38.9071923,-77.0368707',
	'gwu': '38.9071923,-77.0368707',
	'american': '38.9071923,-77.0368707',
	'yale': '41.308274,-72.9278835',
	'dartmouth': '43.7044406,-72.2886934'
	}

administrativeAreaDict = {
	"georgetown": "dc",
	"gwu": "dc",
	"howard" : "dc",
	"american" : "dc",
	"cornell" : "ny",
	"dartmouth" : "nh",
	"yale" : "ct",
	"princeton" : "nj",
	"brown" : "ri",
	"colgate" : "ny",
}

def get_coordinate_and_disance(address, community = []):
	global administrativeAreaDict
	addressUrl = address.replace(' ', '+')
	administrativeArea = ""
	if community != []:
		for item in community:
			if item.lower() in administrativeAreaDict:
				administrativeArea = administrativeAreaDict[item]
				break
	if community != [] and community != ["agnes"] and administrativeArea == "" and "usgbc" not in community:
		print address
		print community
		raw_input("community error")
	components = {'administrative_area':administrativeArea}
	coordinate = gmaps.geocode(address = address, components = components)
	
	if coordinate == []:
		latitude = ""
		longitude = ""
		distance = ""
	else:
		coordinate = coordinate[0] #choose the first reason
		latitude = coordinate["geometry"]["location"]["lat"]
		longitude = coordinate["geometry"]["location"]["lng"]
		if "bounds" in coordinate["geometry"]:
			northeast = coordinate["geometry"]["bounds"]["northeast"]
			southwest = coordinate["geometry"]["bounds"]["southwest"]
		elif "viewport" in coordinate["geometry"]:
			northeast = coordinate["geometry"]["viewport"]["northeast"]
			southwest = coordinate["geometry"]["viewport"]["southwest"]
		distance = haversine((northeast["lng"],northeast["lat"]), (southwest["lng"],southwest["lat"]), miles=True)
		if distance > 3:
			latitude = ""
			longitude = ""
			distance = ""
	return latitude, longitude, distance

def get_place(locationName, community):
	locationName = locationName.replace(" ", "+")
	query = locationName
	location = ""
	if community != []:
		for item in community:
			if item.lower() in cityCoordinateDict:
				location = cityCoordinateDict[item]
				cityLongitude = float(location.split(",")[1])
				cityAltitude = float(location.split(",")[0])
				break
	if community != [] and community != ["agnes"] and location == "" and "usgbc" not in community:
		print address
		print community
		raw_input("community error")

	radius = "50000"
	API_Key="AIzaSyCnXTXPt3cXDjVmP-PLcA3dvhlIC9KPs_E"
	if location != "":
		requrl = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&location="+location+"&radius="+radius+"&key="+API_Key
	else:
		requrl = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_Key
	req = urllib2.Request(requrl)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	dic = json.loads(res)
	latitude = ""
	longitude = ""
	distance = ""
	if dic["status"] == "OK":
		address = dic["results"][0]["formatted_address"]
		geometry = dic["results"][0]["geometry"]
		latitude = geometry["location"]["lat"]
		longitude = geometry["location"]["lng"]
		if "bounds" in geometry:
			northeast = geometry["bounds"]["northeast"]
			southwest = geometry["bounds"]["southwest"]
			distance = haversine((northeast["lng"],northeast["lat"]), (southwest["lng"],southwest["lat"]), miles=True)
		elif "viewport" in geometry:
			northeast = geometry["viewport"]["northeast"]
			southwest = geometry["viewport"]["southwest"]
			distance = haversine((northeast["lng"],northeast["lat"]), (southwest["lng"],southwest["lat"]), miles=True)
		else:
			distance = ""
		cityEventDistance = haversine((longitude, latitude),(cityLongitude, cityAltitude), miles=True)
		if cityEventDistance > 25:
			latitude = ""
			longitude = ""
			distance = ""
		elif distance != "" and distance > 3:
			latitude = ""
			longitude = ""
			distance = ""
	return latitude, longitude, distance

def getGeoInfo(location, community):
	latitude, longitude, distance = get_coordinate_and_disance(location, community)
	if latitude == "":
		latitude, longitude, distance = get_place(location, community)
	return latitude, longitude, distance

def getGeoInfoWithRawOffset(location, community):
	latitude, longitude, distance = get_coordinate_and_disance(location, community)
	if latitude == "":
		latitude, longitude, distance = get_place(location, community)
	rawOffset = getTimeZone(latitude, longitude, community)['rawOffset']
	return latitude, longitude, distance, rawOffset

if __name__ == '__main__':
	location = "Gelman Library"
	community = ["gwu"]
	print getGeoInfo(location, community)


