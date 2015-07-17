import collections
import glob
import gpxpy
import gpxpy.gpx
import datetime
from pint import UnitRegistry
ureg = UnitRegistry()
ureg.define("timedelta = 1 = dt")

best_paces = collections.OrderedDict()
best_paces[1] = datetime.timedelta(minutes=10) * ureg.timedelta / ureg.kilometer
best_paces[5] = datetime.timedelta(minutes=10) * ureg.timedelta / ureg.kilometer
best_paces[10] = datetime.timedelta(minutes=10) * ureg.timedelta / ureg.kilometer
best_paces[15] = datetime.timedelta(minutes=10) * ureg.timedelta / ureg.kilometer
best_paces[20] = datetime.timedelta(minutes=10) * ureg.timedelta / ureg.kilometer

for filename in glob.glob('*.gpx'):
	file = open(filename, 'r')
	gpx = gpxpy.parse(file)

	for track in gpx.tracks:
		if ('Running' in track.name):
			length_km = (track.length_3d() / 1000.0) * ureg.kilometer
			time = datetime.timedelta(seconds=track.get_duration())
			pace = time * ureg.timedelta / length_km
			
			print(pace, length_km)
			
			for distance, record in best_paces.items():
				if length_km > (distance * ureg.kilometer) and pace < record:
					best_paces[distance] = pace

for distance, record in best_paces.items():
	print(distance * ureg.km, "record:", record)