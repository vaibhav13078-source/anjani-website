try:
    sh = client.open_by_key("1eJsjTEBeibYszJFN-ij-4AUn0XI4GuHjWNf4U0YeqFs")
    st.success(f"Connected to spreadsheet: {sh.title}")
    st.write("Sheets:", [ws.title for ws in sh.worksheets()])
except Exception as e:
    st.error(f"Connection error: {e}")

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

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = st.secrets.get("google_service_account")
if not creds_dict:
    st.error("Google credentials not found in Streamlit secrets. Go to Settings → Secrets and add 'google_service_account'.")
    st.stop()

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1eJsjTEBeibYszJFN-ij-4AUn0XI4GuHjWNf4U0YeqFs").sheet1

# Enquiry Form
st.markdown("---")
st.subheader("📩 Enquiry Form")

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
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([now, name.strip(), phone.strip(), course], value_input_option="USER_ENTERED")
        st.success("✅ Enquiry submitted and saved to Google Sheets!")
    else:
        st.warning("⚠ Please fill all required fields (*)")

# Optional: Admin view
if st.checkbox("Show all enquiries (admin)"):
    try:
        data = sheet.get_all_records()
        st.dataframe(data)
    except Exception as e:
        st.error(f"Error reading sheet: {e}")

