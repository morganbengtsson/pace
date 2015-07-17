import gpxpy
import gpxpy.gpx

file = open('2015-07-15-1751.gpx', 'r')

gpx = gpxpy.parse(file)

for track in gpx.tracks:
	print(track.length_3d(), ' m')
	print(track.get_duration(), ' s')
	print(track.length_3d() / track.get_duration(), ' m/s')
	
	length_km = track.length_3d() / 1000.0
	time_min = track.get_duration() / 60.0
	pace = time_min / length_km
	print(length_km, 'km')
	print(time_min, 'min')
	print(pace, ' min/km')