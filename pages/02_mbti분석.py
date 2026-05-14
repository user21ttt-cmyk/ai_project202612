import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI Country Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Countries MBTI Dashboard")
st.markdown("국가별 MBTI 분포를 인터랙티브하게 확인하세요.")

# -----------------------------
# CSV 불러오기
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

try:
    df = load_data()
except:
    st.error("countriesMBTI_16types.csv 파일을 app.py와 같은 폴더에 넣어주세요.")
    st.stop()

# -----------------------------
# 데이터 확인
# -----------------------------
mbti_cols = [col for col in df.columns if col != "Country"]

with st.expander("📄 데이터 미리보기"):
    st.dataframe(df)

# -----------------------------
# 국가 선택
# -----------------------------
country = st.selectbox(
    "국가를 선택하세요",
    sorted(df["Country"].unique())
)

selected = df[df["Country"] == country].iloc[0]

values = selected[mbti_cols].astype(float)

# -----------------------------
# 정렬 옵션
# -----------------------------
sort_option = st.radio(
    "정렬 방식",
    ["높은 순", "원래 순서"],
    horizontal=True
)

if sort_option == "높은 순":
    values = values.sort_values(ascending=False)

# -----------------------------
# 색상 만들기
# 1등 = 빨강
# 나머지 = 파란 그라데이션
# -----------------------------
top_mbti = values.idxmax()

blue_gradient = [
    f"rgba(30, 144, 255, {alpha})"
    for alpha in np.linspace(0.4, 1.0, len(values))
]

colors = []
blue_idx = 0

for mbti in values.index:
    if mbti == top_mbti:
        colors.append("crimson")
    else:
        colors.append(blue_gradient[blue_idx])
        blue_idx += 1

# -----------------------------
# Plotly 그래프
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=values.index,
        y=values.values,
        marker_color=colors,
        text=[f"{v:.2%}" for v in values.values],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}" +
        "<extra></extra>"
    )
)

fig.update_layout(
    title=f"{country} MBTI Distribution",
    xaxis_title="MBTI Type",
    yaxis_title="Ratio",
    height=600,
    template="plotly_white",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# TOP 3 표시
# -----------------------------
st.subheader("🏆 TOP 3 MBTI")

top3 = values.sort_values(ascending=False).head(3)

col1, col2, col3 = st.columns(3)

for col, (mbti, val) in zip([col1, col2, col3], top3.items()):
    col.metric(
        label=mbti,
        value=f"{val:.2%}"
    )

# -----------------------------
# 전체 평균 보기
# -----------------------------
with st.expander("🌎 전체 국가 평균 MBTI"):
    avg = df[mbti_cols].mean().sort_values(ascending=False)
    st.dataframe(avg)
