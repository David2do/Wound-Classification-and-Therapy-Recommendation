import streamlit as st


def app():
    st.write('This demo app is a study that develops an AI-guided model for injury rehabilitation, focusing on seven core wound types.'
             ' Using a MobileNetV2 as a base model, the system provides precise therapy recommendations.'
             ' The custom machine ensures tailored hot or cold treatments, improving recovery outcomes and highlighting AI\'s role in'
             ' advancing personalized, data-driven wound care.'
             )

    st.write('Navigate to the "Therapy Guidance" section on the sidebar to use the app. To ensure accurate results, upload a '
            'clear and correct wound image.')

    st.write('Essentially, the model outputs seven classes of the core wound types (Abrasion, Bruises, Burns, Incision,'
             ' Laceration, Puncture, and Ulcer), and provides therapeutic recommendations based on it\'s inference. ')