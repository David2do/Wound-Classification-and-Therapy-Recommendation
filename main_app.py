import streamlit as st
from src import home
from src import therapy_guidance

st.set_page_config(page_title="Wound Classifier and Therapy Recommendation", layout="centered")

st.title('AI Wound Therapy Pro')

# function to load the models to cache
page = st.sidebar.radio("Go to", ["Home", "Therapy Guidance"])

if page == "Home":
    home.app()
elif page == "Therapy Guidance":
    therapy_guidance.app()
