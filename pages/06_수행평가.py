import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.set_page_config(page_title="화장 판별기", layout="wide")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("makeup_model.keras")

model = load_model()

st.title("💄 화장 여부 판별 AI")

uploaded_file = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, width=350)

    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)[0][0]

    if pred >= 0.5:
        result = "화장한 사람"
        confidence = pred * 100
    else:
        result = "화장하지 않은 사람"
        confidence = (1 - pred) * 100

    st.subheader(f"결과 : {result}")
    st.metric("신뢰도", f"{confidence:.1f}%")

    st.markdown("---")

    if pred >= 0.5:
        st.write("### 화장 특징")
        st.write("""
        - 피부톤이 균일하게 보일 수 있음
        - 입술 색상이 선명함
        - 눈매가 강조될 수 있음
        - 사진 촬영에 유리한 경우가 많음
        """)
    else:
        st.write("### 민낯 특징")
        st.write("""
        - 자연스러운 피부 표현
        - 본래 얼굴 특징 확인 가능
        - 피부결과 주근깨 등이 보일 수 있음
        - 꾸미지 않은 자연스러운 느낌
        """)

    st.info(
        "어느 쪽이 더 좋다고 판단하지 않으며, "
        "상황과 개인 취향에 따라 적합성이 달라집니다."
    )
