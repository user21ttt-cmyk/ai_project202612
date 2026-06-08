sbti_data = {
    "BOSS": {
        "desc": "리더십이 강한 유형",
        "detail": "목표 지향적이며 추진력이 뛰어남",
        "salary": "5,800만원",
        "jobs": ["경영자", "PM", "마케팅 팀장"],
        "tip": "조직을 이끄는 경험을 많이 해보세요.",
        "books": [
            {
                "title": "원칙",
                "genre": "경영",
                "reason": "의사결정 능력 향상"
            },
            {
                "title": "그릿",
                "genre": "자기계발",
                "reason": "끈기와 실행력 강화"
            }
        ],
        "movies": [
            {
                "title": "소셜 네트워크",
                "genre": "드라마",
                "reason": "창업과 리더십"
            },
            {
                "title": "머니볼",
                "genre": "스포츠 드라마",
                "reason": "전략적 사고"
            }
        ]
    }
}
import streamlit as st
from data import sbti_data

st.set_page_config(
    page_title="SBTI 책·영화 추천기",
    page_icon="📚",
    layout="wide"
)

st.title("📚🎬 SBTI 유형별 책·영화 추천")
st.markdown("SBTI 유형을 선택하면 추천 도서, 영화, 직업, 평균 연봉을 확인할 수 있습니다.")

selected_type = st.selectbox(
    "SBTI 유형 선택",
    list(sbti_data.keys())
)

info = sbti_data[selected_type]

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🧑 유형 정보")

    st.info(info["desc"])

    st.metric(
        label="💰 평균 연봉",
        value=info["salary"]
    )

    st.subheader("💼 추천 직업")

    for job in info["jobs"]:
        st.write(f"• {job}")

with col2:
    st.subheader("📖 유형 특징")

    st.write(info["detail"])

st.divider()

book_col, movie_col = st.columns(2)

with book_col:
    st.subheader("📚 추천 도서")

    for idx, book in enumerate(info["books"], start=1):
        st.markdown(
            f"""
### {idx}. {book['title']}

- 장르 : **{book['genre']}**
- 추천 이유 : {book['reason']}
"""
        )

with movie_col:
    st.subheader("🎬 추천 영화")

    for idx, movie in enumerate(info["movies"], start=1):
        st.markdown(
            f"""
### {idx}. {movie['title']}

- 장르 : **{movie['genre']}**
- 추천 이유 : {movie['reason']}
"""
        )

st.divider()

st.subheader("⭐ 학습 및 진로 조언")

st.success(info["tip"])

st.divider()

with st.expander("📌 수행평가 참고용 안내"):
    st.write(
        """
        본 프로그램은 SBTI 유형을 기반으로
        추천 도서, 영화, 직업 정보를 제공합니다.

        평균 연봉은 수행평가용 예시 데이터이며
        실제 통계와 차이가 있을 수 있습니다.
        """
    )

st.caption("Made with Streamlit")
