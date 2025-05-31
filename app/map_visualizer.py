import folium
from folium.plugins import MarkerCluster

def generate_map(df, warehouse, route1, route2):
    m = folium.Map(location=[warehouse['lat'], warehouse['lon']], zoom_start=12)

    # Add warehouse marker
    folium.Marker(
        [warehouse['lat'], warehouse['lon']],
        popup="Warehouse",
        icon=folium.Icon(color='black', icon='home')
    ).add_to(m)

    # Add customers
    cluster = MarkerCluster().add_to(m)
    for _, row in df.iterrows():
        truck_color = 'blue' if row['Truck'] == 0 else 'green'
        folium.Marker(
            [row['Latitude'], row['Longitude']],
            popup=row['BusinessName'],
            icon=folium.Icon(color=truck_color)
        ).add_to(cluster)

    # Draw truck 1 route
    folium.PolyLine(
        [(point['lat'], point['lon']) for point in route1],
        color='blue', weight=4, opacity=0.7, tooltip="Truck 1 Route"
    ).add_to(m)

    # Draw truck 2 route
    folium.PolyLine(
        [(point['lat'], point['lon']) for point in route2],
        color='green', weight=4, opacity=0.7, tooltip="Truck 2 Route"
    ).add_to(m)

    return m._repr_html_()
