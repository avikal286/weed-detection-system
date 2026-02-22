import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

@st.cache_resource
def load_model():
    return YOLO("run/best.pt")   # ✅ YOUR PATH

model = load_model()

st.set_page_config(page_title="YOLO Detection App", layout="wide")
st.title("YOLO-Based Weed Detection App")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

confidence = st.slider("Confidence Threshold", 0.01, 1.0, 0.25)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    results = model.predict(
        source=img_array,
        conf=confidence,
        imgsz=640,
        verbose=False
    )

    st.write("Number of detections:", len(results[0].boxes))

    if len(results[0].boxes) > 0:
        annotated_frame = results[0].plot()
        st.subheader("Detected Objects")
        st.image(annotated_frame, use_container_width=True)

        st.subheader("Detection Details")
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf_score = float(box.conf[0])
            st.write(f"**{label}** – Confidence: {conf_score:.2f}")
    else:

        st.warning("No objects detected. Try lowering confidence or different image.")

