import streamlit as st
import pandas as pd
import folium
import map
from streamlit_folium import st_folium, folium_static


def map():
    with st.container():
        st.title("Which wine are you looking for?🍷")

        code = st.text_input(
            "Search anything!", value="", placeholder="Wine"
        )  ##### 여기서 입력값 받아와야함!!! 입력값 -> code

        st.text(" ")
        st.text(" ")

        # with col_map:
        userspot = folium.Map(
            location=[35.228956, 126.843181], zoom_start=16
        )  ### user에 따라 바꿔야함
        folium.Marker([35.228956, 126.843181], popup="GIST", tooltip="Dasan").add_to(
            userspot
        )

        store1 = folium.Map(location=[35.2196, 126.8443], zoom_start=16)
        folium.Marker([35.2196, 126.8443], popup="A wine", tooltip="").add_to(store1)

        st_data = st_folium(userspot, width=700, height=500)  # 지도 크기 조절

        txt = st.text_area(
            "Details",
            """
            db에서 받아온 정보를 여기에 넣어줄 수 있지 않을까
            """,
        )
        # st.write('Sentiment:',txt)
