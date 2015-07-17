#TODO: 
# Use units
# Convert from decimal to minutes:seconds (use datetime.timedelta)
import glob
import gpxpy
import gpxpy.gpx
import datetime
from pint import UnitRegistry
ureg = UnitRegistry()

best_paces = {1 * ureg.kilometer : datetime.timedelta(minutes=10) / ureg.kilometer,
			  5 * ureg.kilometer : datetime.timedelta(minutes=10) / ureg.kilometer,
			  10 * ureg.kilometer : datetime.timedelta(minutes=10) / ureg.kilometer,
			  15 * ureg.kilometer : datetime.timedelta(minutes=10) / ureg.kilometer,
			  20 * ureg.kilometer : datetime.timedelta(minutes=10) / ureg.kilometer}

#best_1k_pace = datetime.timedelta(minutes=10) / ureg.kilometer
#best_5k_pace = datetime.timedelta(minutes=10) / ureg.kilometer
#best_10k_pace = datetime.timedelta(minutes=10) / ureg.kilometer
#best_15k_pace = datetime.timedelta(minutes=10) / ureg.kilometer
#best_20k_pace = datetime.timedelta(minutes=10) / ureg.kilometer

for filename in glob.glob('*.gpx'):
	file = open(filename, 'r')
	gpx = gpxpy.parse(file)

	for track in gpx.tracks:
		if ('Running' in track.name):
			length_km = (track.length_3d() / 1000.0) * ureg.kilometer
			time = datetime.timedelta(seconds=track.get_duration())
			pace = time / length_km
			
			print(pace, length_km)
			
			if length_km > 1 * ureg.kilometer and pace < best_1k_pace:
				best_1k_pace = pace
								
			if length_km > 5 * ureg.kilometer and pace < best_5k_pace:
				best_5k_pace = pace
								
			if length_km > 10 * ureg.kilometer and pace < best_10k_pace:
				best_10k_pace = pace
			
			if length_km > 15 * ureg.kilometer and pace < best_15k_pace:
				best_15k_pace = pace
				
			if length_km > 20 * ureg.kilometer and pace < best_20k_pace:
				best_20k_pace = pace
				
print("1k best pace: ", best_1k_pace)
print("5k best pace: ", best_5k_pace)
print("10k best pace: ", best_10k_pace)
print("15k best pace: ", best_15k_pace)
print("20k best pace: ", best_20k_pace)