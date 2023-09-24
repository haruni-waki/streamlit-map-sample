import pandas as pd
from fuzzywuzzy import process

# ファイルを読み込む
cultural_properties = pd.read_csv('file.csv')
location_coordinates = pd.read_csv('coordinates.csv')

# 結果を保存するための空の列を作る
cultural_properties['Latitude'] = pd.Series(dtype='float64')
cultural_properties['Longitude'] = pd.Series(dtype='float64')

# 文化財の各所在地について、最も一致する地名を見つけて緯度と経度を追加する
for idx, row in cultural_properties.iterrows():
    location = row['所在地等']
    
    # fuzzywuzzyのprocess.extractOneを使って最も一致する地名を見つける
    best_match = process.extractOne(location, location_coordinates['Location'].tolist())
    
    # 最も一致する地名の緯度と経度を見つける
    coordinates = location_coordinates[location_coordinates['Location'] == best_match[0]][['Latitude', 'Longitude']].values[0]
    
    # 緯度と経度を文化財の情報に追加する
    cultural_properties.at[idx, 'Latitude'] = coordinates[0]
    cultural_properties.at[idx, 'Longitude'] = coordinates[1]

# 新しいファイルを作成する
cultural_properties.to_csv('結合した文化財の情報.csv', index=False)
