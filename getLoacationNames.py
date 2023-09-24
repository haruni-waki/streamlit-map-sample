import pandas as pd

# CSVファイルを読み込み、所在地等の列のみを取得する
df = pd.read_csv('file.csv', usecols=['所在地等'])

# 重複を除いた上でファイルに書き出す
df.drop_duplicates().to_csv('output.csv', index=False, encoding='utf-8-sig')