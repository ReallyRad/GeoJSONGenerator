import csv
import geojson

with open('data.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))


import geojson
with open('world-110m.geojson') as f:
    gj = geojson.load(f)

features = gj['features'][0]