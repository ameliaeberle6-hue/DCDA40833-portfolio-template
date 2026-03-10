# pip install folium pandas requests
import pandas as pd
import requests
import folium
from urllib.parse import quote_plus
import os

# ----------------------------
# CONFIG
# ----------------------------
# Mapbox token: you can keep it here or set MAPBOX_TOKEN in your environment
MAPBOX_TOKEN = os.getenv('MAPBOX_TOKEN', "pk.eyJ1IjoidGN1bWlhIiwiYSI6ImNtbWswMjMyczFrdmYycXBzY2s0cnF1aW4ifQ.uqEFIT3h0FfuzMZLNHKYKA")

# Customize these with your Mapbox username and style ID from Mapbox Studio.
# Example: MAPBOX_USERNAME = 'your_username', MAPBOX_STYLE_ID = 'ckxyzabc12345...'
# Set your Mapbox username and style ID here (provided):
MAPBOX_USERNAME = os.getenv('MAPBOX_USERNAME', 'tcumia')
# If you copied the style URL (mapbox://styles/tcumia/cmmk04hf4004901qua6oc75jc),
# the style id is the last part after the final '/'
MAPBOX_STYLE_ID = os.getenv('MAPBOX_STYLE_ID', 'cmmk04hf4004901qua6oc75jc')

if MAPBOX_USERNAME and MAPBOX_STYLE_ID:
    MAPBOX_TILES = f"https://api.mapbox.com/styles/v1/{MAPBOX_USERNAME}/{MAPBOX_STYLE_ID}/tiles/256/{{z}}/{{x}}/{{y}}@2x?access_token={MAPBOX_TOKEN}"
else:
    # fallback to Mapbox default streets style
    MAPBOX_TILES = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/256/{{z}}/{{x}}/{{y}}@2x?access_token={MAPBOX_TOKEN}"

print('Using Mapbox tiles:', MAPBOX_TILES.split('?')[0])

# ----------------------------
# READ CSV (custom parser for provided file format)
# ----------------------------
import re

csv_path = "hometown_locations - Sheet1.csv"
pattern = re.compile(r'^"(?P<name>.*?)\,""(?P<address>.*?)""\,?(?P<type>[^,]*?)\,""(?P<description>.*?)""\,?\s*(?P<image>https?://\S+)$', re.DOTALL)
rows = []
with open(csv_path, 'r') as fh:
    for raw in fh:
        s = raw.strip()
        if not s:
            continue
        m = pattern.match(s)
        if not m:
            # skip or log unparsable lines
            continue
        rows.append({
            'name': m.group('name').strip().strip('"'),
            'address': m.group('address').strip(),
            'type': m.group('type').strip(),
            'description': m.group('description').strip(),
            'image': m.group('image').strip().strip('"')
        })

df = pd.DataFrame(rows)

# ----------------------------
# GEOCODING FUNCTION
# ----------------------------
def geocode(address):
    query = quote_plus(str(address))
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json?access_token={MAPBOX_TOKEN}&limit=1"
    resp = requests.get(url)
    resp.raise_for_status()
    response = resp.json()
    if not response.get("features"):
        raise ValueError(f"No geocoding result for: {address}")
    coords = response["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]

# ----------------------------
# CREATE MAP
# ----------------------------
start_lat, start_lon = geocode(df.iloc[0]["address"])

m = folium.Map(
    location=[start_lat, start_lon],
    zoom_start=12,
    tiles=MAPBOX_TILES,
    attr="Mapbox"
)

# ----------------------------
# MARKERS
# ----------------------------
for _, row in df.iterrows():
    lat, lon = geocode(row["address"])

    popup_html = f"""
    <h4>{row['name']}</h4>
    <p>{row['description']}</p>
    <img src="{row['image']}" width="200">
    """

    # choose marker color by location type
    type_to_color = {
        'Restaurant': 'red',
        'Park': 'green',
        'Historical': 'purple',
        'Recreation': 'orange',
        'Cultural': 'cadetblue',
        'School': 'darkblue'
    }
    loc_type = row.get('type', '')
    color = type_to_color.get(loc_type.strip(), 'blue')

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(color=color, icon='info-sign')
    ).add_to(m)

# ----------------------------
# SAVE MAP
# ----------------------------
m.save("hometown-map.html")

print(os.listdir())