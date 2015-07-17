#TODO: 
# Use units
# Convert from decimal to minutes:seconds (use datetime.timedelta)
import glob
import gpxpy
import gpxpy.gpx

best_1k_pace = 10.0
best_5k_pace = 10.0
best_10k_pace = 10.0
best_20k_pace = 10.0


for filename in glob.glob('*.gpx'):
	file = open(filename, 'r')
	gpx = gpxpy.parse(file)

	for track in gpx.tracks:
		if ('Running' in track.name):
			#print(track.length_3d(), ' m')
			#print(track.get_duration(), ' s')
			#print(track.length_3d() / track.get_duration(), ' m/s')
			
			length_km = track.length_3d() / 1000.0
			time_min = track.get_duration() / 60.0
			pace = time_min / length_km
			#print(length_km, 'km')
			#print(time_min, 'min')
			print("%.2f" % pace, ' min/km', "%.2f km" % length_km)
			
			if length_km > 1.0 and pace < best_1k_pace:
				best_1k_pace = pace
								
			if length_km > 5.0 and pace < best_5k_pace:
				best_5k_pace = pace
								
			if length_km > 10.0 and pace < best_10k_pace:
				best_10k_pace = pace
				
			if length_km > 20.0 and pace < best_20k_pace:
				best_20k_pace = pace
				
print("1k best pace: ", "%.2f" % best_1k_pace, " km/min")
print("5k best pace: ", "%.2f" % best_5k_pace, " km/min")
print("10k best pace: ", "%.2f" % best_10k_pace, " km/min")
print("20k best pace: ", "%.2f" % best_20k_pace, " km/min")