import streamlit as st
import pandas as pd
from streamlit import components


def slideshow(speed, images):
    slide_show = SlideShow()
    slide_show(speed=speed, images=images, key="slideshow")

def wine():
    st.title('Wine')
    
    image_list = ["https://images.unsplash.com/photo-1534187840746-2f2b80c15b50",
                  "https://images.unsplash.com/photo-1553830570-26dbec850d6a",
                  "https://images.unsplash.com/photo-1525966222135-5a810fda9664",
                  "https://images.unsplash.com/photo-1527616190088-21e4aab9c9fa",
                  "https://images.unsplash.com/photo-1529186406761-7b182cdbcdc8",]

    speed = st.slider("슬라이드 속도를 조절해주세요", 1, 10, 5)
    st.write("## 물건을 보여드릴게요!")
    slideshow(speed, image_list)


@st.cache(allow_output_mutation=True)
def SlideShow():
    component_func = components.declare_component(
    "SlideShow",
    url="http://localhost:3001",
)
    
    return component_func

