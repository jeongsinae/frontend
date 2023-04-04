import streamlit as st
import pandas as pd
import folium
import googlemaps
import map
from streamlit_folium import st_folium, folium_static

def map():
    st.title('Map')

    col_map, col_des = st.columns([4,1])

    with col_map:
        m = folium.Map(location=[35.228956, 126.843181], zoom_start=16)
        folium.Marker(
            [35.228956, 126.843181],
            popup='GIST',
            tooltip='Dasan'
        ).add_to(m)

        st_data = st_folium(m, width=725)
    with col_des:
        df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
        )
        edited_df = st.experimental_data_editor(df, num_rows="dynamic")

        favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        st.markdown(f"Your choices are **{favorite_command}** 🍷")