import folium


def create_map_with_marker(latitude, longitude, marker_label):
    # Создаем карту с заданными координатами
    map = folium.Map(location=[latitude, longitude], zoom_start=30)

    # Создаем маркер с меткой и добавляем его на карту
    folium.Marker(
        location=[latitude, longitude],
        popup=marker_label,
        icon=folium.Icon(color="red"),
    ).add_to(map)

    return map._repr_html_()
