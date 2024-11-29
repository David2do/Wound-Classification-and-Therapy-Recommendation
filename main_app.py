import streamlit as st
import tensorflow as tf
import numpy as np
from therapy_script import therapy

st.set_page_config(page_title="Wound Classifier and Therapy Recommendation", layout="centered")
st.title('Wound Classifier and Therapy Recommendation')

# function to load the models to cache
@st.cache_resource()
def load_model():
    classifier_model = tf.keras.models.load_model("./models/wound_classifier_model.keras")
    status_model = tf.keras.models.load_model("./models/wound_status_model.keras")
    return classifier_model, status_model

# load the models
classifier_model, status_model = load_model()


# class names for the models and input params
main_class_name = ['Abrasion', 'Bruises', 'Burns', 'Incision', 'Laceration', 'Puncture', 'Ulcer']
status_class_name = ['Fresh', 'Healing']
img_height, img_width = 224, 224

# image uploader
st.write('')
uploaded_file = st.file_uploader('Upload a clear and correct image:', type=['png','jpg','jpeg', 'jfif'])

if uploaded_file is not None:
    st.image(uploaded_file)

    # perform image pre-processing
    img = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)  # Create a batch

    # Normalize the image
    img_array = img_array / 255.0

    # perform both predictions
    prediction_class = classifier_model.predict(img_array)
    prediction_status = status_model.predict(img_array)
    score_class = tf.nn.softmax(prediction_class[0])
    score_status = tf.nn.softmax(prediction_status[0])

    wound_class = main_class_name[np.argmax(score_class)]
    wound_status = status_class_name[np.argmax(score_status)]

    # output the predictions
    st.write(f'Wound Class: {wound_class}')
    st.write(f'Wound Status: {wound_status}')
    therapy(wound_class=wound_class, wound_status=wound_status)
