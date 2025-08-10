# app.py
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Page Config
st.set_page_config(page_title="Anjani Computer", page_icon=":computer:", layout="centered")

# Header Section
st.image(
    "https://raw.githubusercontent.com/vaibhav13078-source/anjani-website/main/anjani_website/logo.png",
    width=120,
)
st.markdown(
    "<h1 style='color:#2c3e50; font-weight:700;'>Anjani Computer Institute</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='font-size:1.1rem; color:#34495e;'>Empowering Your Future with Quality IT & Typing Education</p>",
    unsafe_allow_html=True,
)

# Courses Section
st.markdown("---")
st.subheader("Our Popular Courses")

courses = [
    {
        "name": "MS-CIT",
        "img": "https://raw.githubusercontent.com/vaibhav13078-source/anjani-website/main/anjani_website/mscIT.jpg",
    },
    {
        "name": "Tally Prime with GST",
        "img": "https://raw.githubusercontent.com/vaibhav13078-source/anjani-website/main/anjani_website/Tallygst.jpg",
    },
    {
        "name": "Typing with GCC TBC",
        "img": "https://raw.githubusercontent.com/vaibhav13078-source/anjani-website/main/anjani_website/Typing.jpg",
    },
]

cols = st.columns(3)
for idx, course in enumerate(courses):
    with cols[idx]:
        st.image(course["img"], use_container_width=True)
        st.markdown(
            f"<div style='text-align:center; font-weight:600; color:#2980b9;'>{course['name']}</div>",
            unsafe_allow_html=True,
        )

