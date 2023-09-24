import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Photon
from streamlit_js_eval import get_geolocation

def main():
    st.set_page_config(layout="wide") #←

    # CSVファイルを読み込む
    df = pd.read_csv('file.csv')

    # サイドバーで表示を切り替える
    page = st.sidebar.selectbox("Choose a page", ["Database View", "Map View"])

    if page == "Database View":
        # データベース表示
        st.header("Database View")
        col1, col2, col3 = st.columns(3)
        with col1:
            sort_option = st.selectbox('Sort by:', df.columns)
            df = df.sort_values(sort_option)
        with col2:
            filter_column = st.selectbox('Filter column:', df.columns)
            unique_values_in_column = df[filter_column].unique()
        with col3:
            selected_value = st.selectbox('Filter by:', unique_values_in_column)
            df = df[df[filter_column] == selected_value]
        st.write(df,width="100%")
    elif page == "Map View":
        # マップ表示
        st.header("Map View")
        # Geolocatorを作成
        geolocator = Photon(user_agent="geoapiExercises")
        # 現在地の取得
        loc = get_geolocation()
        if loc is not None:
            loc = loc['coords']
            # 取得した座標を地図の中心に設定
            m = folium.Map(location=[loc["latitude"], loc["longitude"]], zoom_start=15,width="100%")
        else:
            # 現在地取得がうまくいかない場合はデフォルトの座標（ここでは東京）を使う
            m = folium.Map(
                location=[31.583683448060494, 130.54209207000648],
                zoom_start=10,width="100%")
        df = pd.read_csv('data.csv')
        # 各行に対して、位置情報を取得し、マップにピンを立てる
        for idx, row in df.iterrows():
            if row["Latitude"] != "Not Found":
                folium.Marker([row["Latitude"], row["Longitude"]], popup=row['名称']).add_to(m)
        # 現在地のピンを立てる
        if loc is not None:
            # print(loc)
            folium.Marker([loc["latitude"], loc["longitude"]],
                          popup="You are here!",
                          icon=folium.Icon(color='red')).add_to(m)
        # Streamlitにマップを表示
        # folium_static(m)
        st.components.v1.html(folium.Figure().add_child(m).render(), height=500)

if __name__ == "__main__":
    main()
