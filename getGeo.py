import csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myGeocoder")

# CSVファイルから地名を読み込む
with open('locations.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    locations = list(reader)

# 結果を保存するためのCSVファイルを開く
with open('coordinates.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # ヘッダーを書き込む
    writer.writerow(["Location", "Latitude", "Longitude"])
    for location in locations:
        location_name = f"鹿児島市 {location[0]}"
        try:
            geo_location = geolocator.geocode(location_name)
            if geo_location is not None:
                writer.writerow([location_name, geo_location.latitude, geo_location.longitude])
            else:
                writer.writerow([location_name, 'Not Found', 'Not Found'])
        except Exception as e:
            print(f"Error: {e}")
