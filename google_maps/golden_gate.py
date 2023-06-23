import gmplot
# import pandas as pd

from key import GOOGLE_API_KEY

# API KEY (ignorada)
apikey = GOOGLE_API_KEY

lat = 37.766956
lng = -122.448481
zoom = 14
gmap = gmplot.GoogleMapPlotter(lat, lng, zoom, apikey=apikey)

# marcador
mark_lat = 37.770776
mark_lng = -122.461689
color = 'cornflowerblue'
gmap.marker(mark_lat, mark_lng, color=color)

# coordenadas de atracciones
attractions_lats, attractions_lngs = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
])

# df = pd.read_excel('./puntos.xlsx', 'atracciones')
# attractions_lats = df['lat'].tolist()
# attractions_lngs = df['lng'].tolist()
gmap.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=False)

# coordenadas del parque
golden_gate_park = zip(*[
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (37.774797, -122.454538),
    (37.771988, -122.454018),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347)
])
gmap.polygon(*golden_gate_park, color='cornflowerblue', edge_width=10)

# df = pd.read_excel('./puntos.xlsx', 'golden_gate')
# golden_gate_lats = df['lat'].tolist()
# golden_gate_lngs = df['lng'].tolist()
# gmap.polygon(golden_gate_lats, golden_gate_lngs, color='cornflowerblue', edge_width=10)

# Draw the map to an HTML file:
gmap.draw('map.html')
