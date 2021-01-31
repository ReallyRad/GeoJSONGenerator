import csv
import geojson

with open('world-110m.geojson') as f:
    gj = geojson.load(f)

features = gj['features']

with open('data.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         for feature in features:
             if row[0] == feature['properties']['name']:
                 feature['properties']['rating'] = row[2]


gj['features'] = features

with open('out.geojson', 'w') as outfile:
    geojson.dump(gj, outfile)