import streamlit as st
from main import crew

st.title("AI Use Case Generator 🚀")
if st.button("Run Multi-Agent"):
    result = crew.run()
    st.markdown(result, unsafe_allow_html=True)
