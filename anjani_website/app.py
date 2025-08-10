import streamlit as st
import pandas as pd
import os

# Set page config for a professional look
st.set_page_config(page_title="Anjani Computer", page_icon=":computer:", layout="centered")

# Header Section
st.image("logo.png", width=120)
st.markdown("<h1 style='color:#2c3e50; font-weight:700;'>Anjani Computer Institute</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.1rem; color:#34495e;'>Empowering Your Future with Quality IT & Typing Education</p>", unsafe_allow_html=True)

# Courses Section
st.markdown("---")
st.subheader("Our Popular Courses")

courses = [
    {"name": "MS-CIT", "img": "mscIT.jpg"},
    {"name": "Tally Prime with GST", "img": "Tallygst.jpg"},
    {"name": "Typing with GCC TBC", "img": "typing.jpg"},
]

cols = st.columns(3)
for idx, course in enumerate(courses):
    with cols[idx]:
        st.image(course["img"], use_container_width=True)
        st.markdown(f"<div style='text-align:center; font-weight:600; color:#2980b9;'>{course['name']}</div>", unsafe_allow_html=True)
        st.button(f"Know More", key=course["name"])

# Enquiry Form Section
st.markdown("---")
st.subheader("Enquiry Form")

with st.form("enquiry_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    mobile = st.text_input("Mobile Number")
    city = st.text_input("City")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit Enquiry")

    if submitted:
        data = {
            "Name": [name],
            "Mobile Number": [mobile],
            "City": [city],
            "Message": [message]
        }
        df = pd.DataFrame(data)

        file_dir = "anjani_website"
        file_path = os.path.join(file_dir, "enquiry.xlsx")
        os.makedirs(file_dir, exist_ok=True)

        if os.path.exists(file_path):
            old_df = pd.read_excel(file_path)
            df = pd.concat([old_df, df], ignore_index=True)
        df.to_excel(file_path, index=False, engine="openpyxl")

        st.success("Thank you for your enquiry! We will get back to you soon.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#7f8c8d; font-size:0.9rem;'>© 2024 Anjani Computer Institute. All rights reserved.</div>",
    unsafe_allow_html=True
)
