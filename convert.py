import csv
import geojson

def centroid (vertexes):
  x_list = [vertex[0] for vertex in vertexes]
  y_list = [vertex[1] for vertex in vertexes]
  x = sum(x_list) / len(vertexes)
  y = sum(y_list) / len(vertexes)
  return(x,y)

with open('world-110m.geojson') as f:
    countries = geojson.load(f)

with open('chicago-parks.geojson') as f:
    markers = geojson.load(f)

features = countries['features']

points = geojson.FeatureCollection(features=[])

with open('data.csv') as csvfile:
     csv_reader = csv.reader(csvfile, delimiter=',')
     for row in csv_reader:
         for feature in features:
             if row[0] == feature['properties']['name']:
                 feature['properties']['rating'] = row[2]
                 if (feature['geometry']['type'] == 'MultiPolygon'):
                   my_point = geojson.Point(centroid(feature['geometry']['coordinates'][0][0]))
                 else:
                   my_point = geojson.Point(centroid(feature['geometry']['coordinates'][0]))

                 new_feature = geojson.Feature(geometry=my_point, properties={"description": row[1], "title": row[0]})
                 points['features'].append(new_feature)

countries['features'] = features

with open('out.geojson', 'w') as outfile:
    geojson.dump(countries, outfile)

#for each country with link
#calculate center of country
#add node with country name as title, url as description, country center as coordinates
