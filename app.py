import streamlit as st
from PIL import Image
import time

# Page config
st.set_page_config(page_title="Our Love Story ❤️", page_icon="❤️", layout="centered")

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #ffdde1, #ee9ca7);
}
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: black;
}
.subtitle {
    font-size: 20px;
    text-align: center;
    color: black;
}
.box {
    background-color: rgba(255,255,255,0.25);
    padding: 20px;
    border-radius: 15px;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💖 Our Love Story 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A journey of love beyond distance</div>', unsafe_allow_html=True)

# Load your images
image1 = Image.open("images/pic1.jpg")
image2 = Image.open("images/pic2.jpg")
image3 = Image.open("images/pic3.jpg")

# Section 1
st.markdown('<div class="box">', unsafe_allow_html=True)
st.image(image1, caption="Our First Memory ❤️", width=600)

st.subheader("🌸 The Beginning")
st.write("""
It all started with a simple conversation that turned into something unforgettable.

From strangers to best friends… and then to something much deeper,
you became the most important part of my life.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Section 2
st.markdown('<div class="box">', unsafe_allow_html=True)
st.image(image2, caption="Moments I Miss the Most 💞", width=600)

st.subheader("💞 Our Journey")
st.write("""
Even though we are miles apart, I feel you close to my heart every single day.

Every message, every call, every little effort—
made me realize how strong our love truly is.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Section 3
st.markdown('<div class="box">', unsafe_allow_html=True)
st.image(image3, caption="Together Forever 🌍❤️", width=600)

st.subheader("🌍 Our Long Distance Love")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Pros")
    st.write("""
    - Strong emotional bond  
    - Deep trust  
    - Meaningful conversations  
    - Personal growth  
    """)

with col2:
    st.markdown("### ❌ Cons")
    st.write("""
    - Missing you every day  
    - No physical presence  
    - Time differences  
    - Hard goodbyes  
    """)

st.markdown('</div>', unsafe_allow_html=True)

# Love Button
st.write("")
if st.button("💌 Click to Reveal My Heart"):
    with st.spinner("Loading my feelings... ❤️"):
        time.sleep(2)

    st.success("❤️ Message Loaded ❤️")

    st.markdown("""
    ## 💖 I LOVE YOU 💖

    No matter how far we are,
    my heart always belongs to you.

    You are my happiness, my peace, my forever.

    I may not always be there physically,
    but I promise I am always there emotionally.

    **I LOVE YOU SO MUCH ❤️**
    """)

# Footer
st.markdown("<center>Made with ❤️ just for you by Bikash Dahal (Sana)</center>", unsafe_allow_html=True)
