import streamlit as st

st.set_page_config(page_title="Contact Us | Anjani Computer", page_icon="📞", layout="centered")

st.title("📞 Contact Us")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://i.imgur.com/4M34hi2.png", width=120)  # Replace with your logo if available

with col2:
    st.markdown("""
    <h3 style='margin-bottom:0;'>Anjani Computer</h3>
    <p style='margin-top:0; color:gray;'>Your trusted IT partner in Nanded</p>
    """, unsafe_allow_html=True)

st.markdown("""
**Address:**  
Latur Phata Chowk, Nanded

**Phone:**  
<a href="tel:+917588424343">7588424343</a> / 
<a href="tel:+917028344555">7028344555</a> / 
<a href="tel:+917666371355">7666371355</a>
""", unsafe_allow_html=True)

st.markdown("""
**Connect with us:**
- [📩 WhatsApp](https://whatsapp.com/channel/0029VbAjw12BA1ewKtqB7t2z)
- [📸 Instagram](https://instagram.com/anjanicomputer_nanded)
""")

st.markdown("---")
st.subheader("📍 Find Us on the Map")
st.markdown("""
<iframe
    src="https://www.google.com/maps?q=19.1232735,77.312532&z=18&output=embed"
    width="100%" height="300" style="border:0; border-radius:8px;"
    allowfullscreen="" loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"></iframe>
""", unsafe_allow_html=True)

