import json
import requests
from urllib.request import urlretrieve

airports_json_url = "https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588" \
                    "/airports.json "
airports_data_save_path = "airports_data.txt"

def get_image(lat, lng, width, height, zoom, scale, name):
    f = open(name, 'wb')
    url = 'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&scale={scale}&center={lat},{lng}&zoom={' \
          'zoom}&size={width}x{height}&sensor=false'.format(
        lat=lat, lng=lng, width=width, height=height, scale=scale, zoom=zoom)
    f.write(requests.get(url).content)
    f.close()

print('Download airport information')
urlretrieve(airports_json_url, airports_data_save_path)

f = open(airports_data_save_path, 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)

print('Download airport images')
for (inx, d) in enumerate( data ):
    if inx >=90:    # start inx
        get_image(d['lat'], d['lon'], 640, 640, 14, 2, 'images/{0}.png'.format(d['name']))
    if inx >= 100:  # stop inx
        break

