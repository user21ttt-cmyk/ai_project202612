import streamlit as st
import cv2
import numpy as np
import os
import joblib

from PIL import Image
from sklearn.ensemble import RandomForestClassifier

MODEL_FILE = "makeup_model.pkl"

# -----------------------
# 특징 추출 함수
# -----------------------
def extract_features(img):

    img = cv2.resize(img, (64, 64))

    rgb_mean = img.mean(axis=(0, 1))

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    hsv_mean = hsv.mean(axis=(0, 1))

    features = np.concatenate([
        rgb_mean,
        hsv_mean
    ])

    return features


# -----------------------
# 데이터셋 읽기
# -----------------------
def load_dataset():

    X = []
    y = []

    base = "data/data"

    classes = {
        "no_makeup": 0,
        "makeup": 1
    }

    for cls, label in classes.items():

        folder = os.path.join(base, cls)

        for file in os.listdir(folder):

            path = os.path.join(folder, file)

            try:
                img = Image.open(path).convert("RGB")
                img = np.array(img)

                feat = extract_features(img)

                X.append(feat)
                y.append(label)

            except:
                pass

    return np.array(X), np.array(y)


# -----------------------
# 모델 학습
# -----------------------
@st.cache_resource
def get_model():

    if os.path.exists(MODEL_FILE):
        return joblib.load(MODEL_FILE)

    X, y = load_dataset()

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, MODEL_FILE)

    return model


model = get_model()

# -----------------------
# UI
# -----------------------
st.title("💄 화장 여부 판별 AI")

uploaded = st.file_uploader(
    "사진 업로드",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(image, width=300)

    img = np.array(image)

    feat = extract_features(img)

    prob = model.predict_proba([feat])[0][1]

    if prob >= 0.5:
        result = "화장한 사람"
        confidence = prob * 100
    else:
        result = "화장하지 않은 사람"
        confidence = (1 - prob) * 100

    st.success(result)

    st.metric(
        "신뢰도",
        f"{confidence:.1f}%"
    )

    st.markdown("---")

    st.subheader("분석")

    if prob >= 0.5:
        st.write("""
        ✔ 피부톤이 비교적 균일함

        ✔ 색조 표현이 강함

        ✔ 입술·눈 주변 색상이 뚜렷함
        """)
    else:
        st.write("""
        ✔ 자연스러운 피부 표현

        ✔ 색조 대비가 적음

        ✔ 원래 피부 특징이 잘 보임
        """)

    st.info(
        "이 결과는 AI의 추정이며 100% 정확하지 않을 수 있습니다."
    )
