def distance_in_m(lat,long):	
	
	import math
	ref_lat = 37.7749295
	ref_long = -122.4194155

	radius_earth_in_m = 6371000
	degrees_to_radians = math.pi/180.0

	phi1 = (90.0 - ref_lat) * degrees_to_radians
	phi2 = (90.0 - lat) * degrees_to_radians

	theta1 = ref_long*degrees_to_radians
	theta2 = long*degrees_to_radians

	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
	arc = math.acos( cos )

	return arc * radius_earth_in_m
