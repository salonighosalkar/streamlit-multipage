import streamlit as st

st.title("Plotting Demo")

st.write("Welcome to the plotting page!")

numbers = [1, 2, 3, 4, 5]
st.line_chart(numbers)
