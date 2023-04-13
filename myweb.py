import streamlit as st
import pandas as pd
import folium
from home import home
from map import map
from wine import wine


# 사이드바 생성
st.sidebar.header("Welcome! 00!")

##### db 연동, 사용자별 id 띄워주기 #####

with st.sidebar:
    menu = ["HOME", "Map", "Wine"]
    choice = st.sidebar.selectbox("Select menu!", menu)

    st.text(" ")
    st.text(" ")

if choice == "HOME":
    home()
elif choice == "Map":
    map()
else:
    wine()
