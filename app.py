import streamlit as st
from password_generator import generate_password

st.title("🔑 Secure Password Generator")

length = st.slider("Select Password Length:", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits", value=True)
use_special_chars = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.text_area("Your Secure Password:", password, height=68)
