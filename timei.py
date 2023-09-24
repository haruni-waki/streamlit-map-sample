import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    header = next(reader)

    # LatitudeおよびLongitudeが"Not Found"の所在地を抽出
    locations = set()  # 重複を避けるためsetを使用
    for row in reader:
        if row[6] == "Not Found" or row[7] == "Not Found":
            locations.add(row[4])

with open('notfound.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for location in locations:
        writer.writerow([location])
