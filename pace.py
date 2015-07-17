import collections
import glob
import gpxpy
import gpxpy.gpx
import datetime

records = collections.OrderedDict()
records[1] = datetime.timedelta(minutes=10)
records[5] = datetime.timedelta(minutes=10)
records[10] = datetime.timedelta(minutes=10)
records[15] = datetime.timedelta(minutes=10)
records[20] = datetime.timedelta(minutes=10)

for filename in glob.glob('*.gpx'):
    file = open(filename, 'r')
    gpx = gpxpy.parse(file)

    for track in gpx.tracks:
        if "Running" in track.name:
            length = track.length_3d() / 1000.0
            duration = datetime.timedelta(seconds=track.get_duration())
            pace = duration / length

            print(str(pace).split('.')[0] + " min/km", "%.2f km" % length)

            for distance, record in records.items():
                if length > distance and pace < record:
                    records[distance] = pace

for distance, record in records.items():
    print("%.2f km" % distance, str(record).split('.')[0] + " min/km")