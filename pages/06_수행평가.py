import streamlit as st

st.set_page_config(
    page_title="SBTI 추천 시스템",
    page_icon="📚",
    layout="wide"
)

# SBTI 27개 유형
sbti_types = [
    "CTRL", "ATM-er", "Dior-s", "BOSS", "THAN-K",
    "OH-NO", "GOGO", "CHARM", "LOVE-R", "MUM",
    "FAKE", "OJBK", "MALO", "JOKE-R", "WOC!",
    "THIN-K", "FURY", "ZZZZ", "POOR", "MONK",
    "IMSB", "SOLO", "WILD", "DRAIN", "IMFW",
    "HHHH", "CHEERS"
]

# 유형 그룹
groups = {
    "리더형": ["CTRL", "BOSS"],
    "분석형": ["THIN-K", "THAN-K"],
    "감성형": ["LOVE-R", "MUM"],
    "창의형": ["CHARM", "JOKE-R"],
    "자유형": ["GOGO", "WILD"],
    "독립형": ["SOLO", "MONK"],
}

recommendations = {
    "리더형": {
        "salary": "5,800만원",
        "jobs": ["경영자", "PM", "마케팅 팀장"],
        "books": [("원칙", "경영"), ("그릿", "자기계발")],
        "movies": [("소셜 네트워크", "드라마"), ("머니볼", "스포츠")],
        "desc": "목표 지향적이며 추진력이 강한 유형"
    },
    "분석형": {
        "salary": "5,600만원",
        "jobs": ["연구원", "개발자", "데이터 분석가"],
        "books": [("코스모스", "과학"), ("이기적 유전자", "과학")],
        "movies": [("인터스텔라", "SF"), ("컨택트", "SF")],
        "desc": "논리적 사고와 분석 능력이 뛰어난 유형"
    },
    "감성형": {
        "salary": "4,900만원",
        "jobs": ["교사", "상담사", "사회복지사"],
        "books": [("아몬드", "소설"), ("어린 왕자", "소설")],
        "movies": [("코코", "애니메이션"), ("원더", "드라마")],
        "desc": "공감 능력이 뛰어나고 배려심이 많은 유형"
    },
    "창의형": {
        "salary": "5,100만원",
        "jobs": ["디자이너", "작가", "광고기획자"],
        "books": [("생각의 탄생", "창의성"), ("갈매기의 꿈", "소설")],
        "movies": [("인셉션", "SF"), ("위대한 쇼맨", "뮤지컬")],
        "desc": "새로운 아이디어를 만들어내는 유형"
    },
    "자유형": {
        "salary": "5,000만원",
        "jobs": ["여행작가", "PD", "크리에이터"],
        "books": [("연금술사", "소설"), ("모모", "판타지")],
        "movies": [("업", "애니메이션"), ("탑건 매버릭", "액션")],
        "desc": "도전과 경험을 좋아하는 유형"
    },
    "독립형": {
        "salary": "5,300만원",
        "jobs": ["교수", "연구원", "프로그래머"],
        "books": [("데미안", "성장소설"), ("사피엔스", "인문")],
        "movies": [("마션", "SF"), ("이미테이션 게임", "드라마")],
        "desc": "스스로 탐구하고 성장하는 유형"
    }
}

def get_group(sbti):
    for group, types in groups.items():
        if sbti in types:
            return group
    return "분석형"  # 나머지 유형 기본값

st.title("📚🎬 SBTI 유형별 추천 시스템")

selected = st.selectbox(
    "SBTI 유형을 선택하세요",
    sbti_types
)

group = get_group(selected)
info = recommendations[group]

st.subheader(f"🧑 {selected} 유형")

st.info(info["desc"])

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 평균 연봉", info["salary"])

    st.subheader("💼 추천 직업")
    for job in info["jobs"]:
        st.write("•", job)

with col2:
    st.subheader("📖 추천 도서")
    for title, genre in info["books"]:
        st.write(f"• {title} ({genre})")

    st.subheader("🎬 추천 영화")
    for title, genre in info["movies"]:
        st.write(f"• {title} ({genre})")

st.success("수행평가용 예시 데이터입니다.")
