import glob
import csv
import gpxpy.gpx
from datetime import timedelta, datetime


class Run:
    def __init__(self, length:float, duration:timedelta, time:datetime):
        self.duration = duration
        self.length = length
        self.time = time

    def __str__(self):
        return str(self.pace()).split('.')[0] + " min/km" + " %.2f km" % self.length + " " + str(self.time)

    def pace(self) -> timedelta:
        return self.duration / self.length


class Runs(list):
    def record(self, length) -> Run:
        return min([x for x in runs if x.length > length], key=lambda item:item.pace())


runs = Runs()


for filename in glob.glob('*.gpx'):
    file = open(filename, 'r')
    gpx = gpxpy.parse(file)

    for track in gpx.tracks:
        if "Running" in track.name:
            runs.append(Run(track.length_3d() / 1000.0,
                            timedelta(seconds=track.get_duration()),
                            track.get_time_bounds()[0]))

with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Date', 'Average pace'])
    for run in runs:
        if 10.0 < run.length < 15.0:
            total_seconds = run.pace().total_seconds()
            h = total_seconds // 3600
            m = (total_seconds % 3600) // 60
            sec = (total_seconds % 3600) % 60
            writer.writerow([run.time.strftime("%Y-%m-%d"), '{:02d}:{:02d}:{:02d}'.format(int(h), int(m), int(sec))])

print(runs.record(1.0))
print(runs.record(5.0))
print(runs.record(10.0))
print(runs.record(15.0))
print(runs.record(20.0))
