import tensorflow as tf
import numpy as np
import cv2
import streamlit as st

st.title('Standford_online_products classification')

### model ###

classes = [    "bicycle",
    "cabinet",
    "chair",
    "coffee_maker",
    "fan",
    "kettle",
    "lamp",
    "mug",
    "sofa",
    "stapler",
    "table",
    "toaster" ]

deep = tf.saved_model.load('model')
st.header(":blue[Using model]")
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if img_file_buffer is not None:
    file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_array = np.array(img)
    st.image(cv2.resize(img_array, (224, 224)))


if st.button('Predict'):
    img_array = cv2.resize(img_array, (224, 224)).astype(np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    val = deep(img_array)
    st.write(f'result : {np.argmax(val[0])}')
    st.write(f'class  : {classes[np.argmax(val[0])]}')
    st.bar_chart(val[0])