import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("Aplicacion de reconocimiento de abejas y mariposas")
st.balloons()

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  st.write(label)
  

  if label==0:
    st.subheader("Es una mariposa")
  else:
    st.subheader("Es una abeja")
  #st.snow()
  #st.st.slidebar.image(uploaded_file)
  st.image(uploaded_file)
