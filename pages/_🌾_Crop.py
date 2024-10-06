import streamlit as st
from algorithms.crop_analyzer import CropAnalyzer
import cv2
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
        page_title="Crop Connect",
        page_icon="🪴",
)

st.title('Crops analysis')

st.divider()

# File upload section
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image_pil = Image.open(uploaded_file)
image_np = np.array(image_pil)
image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

# Display the file details after uploading
if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")
    image, data = CropAnalyzer.analyze_image(image_cv, 1, 2)
    #Handle data - funcion Rossi
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image_rgb, caption="Results", use_column_width=True)
    st.write("Analysis complete")

# Display the image