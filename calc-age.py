import streamlit as st
import time

st.image('https://collegevidya.com/tool/images/age.png', use_column_width=True)

year = st.slider("Enter your birth year", 2000, 2023, 2000)
# current = st.slider("Enter the current year", 2024, 2050, 2024)
current = time.localtime().tm_year
age = current - year

if st.button("Calculate"):
    st.write(f"## Your age is {age}")
    st.balloons()
