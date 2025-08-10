import streamlit as st
import pandas as pd
import os

# Set page config
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
        st.button("Know More", key=course["name"])

import streamlit as st
import pandas as pd
from datetime import datetime

st.markdown("---")
st.subheader("📩 Enquiry Form")

# Form UI
with st.form("enquiry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name*")
    with col2:
        phone = st.text_input("Mobile Number*")

    course = st.selectbox(
        "Select Course*",
        ["MS-CIT", "Tally Prime with GST", "Typing with GCC TBC", "Other"]
    )

    submitted = st.form_submit_button("Submit Enquiry")

    if submitted:
        if name.strip() and phone.strip():
            new_data = pd.DataFrame([{
                "Name": name.strip(),
                "Phone": phone.strip(),
                "Course": course,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }])

            file_path = "enquiries.xlsx"

            try:
                # Append if file exists
                try:
                    old_data = pd.read_excel(file_path, engine="openpyxl")
                    df = pd.concat([old_data, new_data], ignore_index=True)
                except FileNotFoundError:
                    df = new_data

                df.to_excel(file_path, index=False, engine="openpyxl")
                st.success("✅ Your enquiry has been submitted successfully!")
            except Exception as e:
                st.error(f"❌ Error saving enquiry: {e}")
        else:
            st.warning("⚠ Please fill all required fields (*).")
import pandas as pd
df = pd.read_excel("anjani_website/enquiry.xlsx")
