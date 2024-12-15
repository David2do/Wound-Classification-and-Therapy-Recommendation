import streamlit as st
import sys
sys.path.append('./src/')
import home
import therapy_guidance

st.set_page_config(page_title="Wound Classifier and Therapy Recommendation", layout="centered")

st.title('AI Wound Therapy Pro')

# function to load the models to cache
page = st.sidebar.radio("Go to", ["Home", "Therapy Guidance"])

if page == "Home":
    home.app()
elif page == "Therapy Guidance":
    therapy_guidance.app()
