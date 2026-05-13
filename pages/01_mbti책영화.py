import streamlit as st

st.set_page_config(page_title="MBTI 책 & 영화 추천", page_icon="📚")

# MBTI별 추천 데이터
recommend_data = {
    "INTJ": {
        "books": [
            {"title": "데미안", "genre": "철학·성장", "desc": "깊은 사고와 자기 성찰을 좋아하는 사람에게 적합"},
            {"title": "사피엔스", "genre": "인문·역사", "desc": "논리적 분석과 지적 호기심이 강한 사람에게 추천"}
        ],
        "movies": [
            {"title": "인터스텔라", "genre": "SF·과학", "desc": "미래와 우주, 과학적 사고를 좋아하는 사람에게 적합"},
            {"title": "인셉션", "genre": "SF·스릴러", "desc": "복잡한 전개와 추리를 좋아하는 사람에게 추천"}
        ]
    },

    "INTP": {
        "books": [
            {"title": "코스모스", "genre": "과학", "desc": "우주와 과학 탐구를 좋아하는 사람에게 추천"},
            {"title": "1984", "genre": "디스토피아", "desc": "사회 구조를 분석하는 것을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "매트릭스", "genre": "SF·액션", "desc": "현실과 철학적 질문을 좋아하는 사람에게 추천"},
            {"title": "테넷", "genre": "SF·추리", "desc": "복잡한 시간 구조를 이해하는 것을 즐기는 사람에게 적합"}
        ]
    },

    "ENTJ": {
        "books": [
            {"title": "군주론", "genre": "정치·철학", "desc": "리더십과 전략에 관심 있는 사람에게 추천"},
            {"title": "넛지", "genre": "경제·심리", "desc": "사람의 행동과 전략을 분석하는 데 흥미 있는 사람에게 적합"}
        ],
        "movies": [
            {"title": "아이언맨", "genre": "액션·SF", "desc": "카리스마 있는 리더형 인물에 끌리는 사람에게 추천"},
            {"title": "소셜 네트워크", "genre": "드라마", "desc": "성공과 도전을 좋아하는 사람에게 적합"}
        ]
    },

    "ENTP": {
        "books": [
            {"title": "아몬드", "genre": "성장소설", "desc": "새로운 시각과 감정을 탐구하는 사람에게 추천"},
            {"title": "팩트풀니스", "genre": "인문", "desc": "세상을 다양한 관점으로 바라보는 사람에게 적합"}
        ],
        "movies": [
            {"title": "주토피아", "genre": "애니메이션", "desc": "창의적이고 유쾌한 이야기를 좋아하는 사람에게 추천"},
            {"title": "레디 플레이어 원", "genre": "SF·모험", "desc": "새로운 세계관과 상상력을 좋아하는 사람에게 적합"}
        ]
    },

    "INFJ": {
        "books": [
            {"title": "어린 왕자", "genre": "동화·철학", "desc": "감수성과 깊은 의미를 좋아하는 사람에게 추천"},
            {"title": "나미야 잡화점의 기적", "genre": "힐링소설", "desc": "따뜻한 감동과 공감을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "코코", "genre": "애니메이션·감동", "desc": "가족과 감정을 중요하게 생각하는 사람에게 추천"},
            {"title": "월-E", "genre": "애니메이션·SF", "desc": "조용하지만 깊은 감성을 좋아하는 사람에게 적합"}
        ]
    },

    "INFP": {
        "books": [
            {"title": "미드나잇 라이브러리", "genre": "판타지·힐링", "desc": "상상력과 감성을 중요하게 생각하는 사람에게 추천"},
            {"title": "연금술사", "genre": "성장·철학", "desc": "꿈과 의미를 찾고 싶은 사람에게 적합"}
        ],
        "movies": [
            {"title": "라라랜드", "genre": "뮤지컬·로맨스", "desc": "감성적이고 예술적인 분위기를 좋아하는 사람에게 추천"},
            {"title": "업", "genre": "애니메이션·감동", "desc": "따뜻한 이야기와 감동을 좋아하는 사람에게 적합"}
        ]
    },

    "ENFJ": {
        "books": [
            {"title": "죽은 시인의 사회", "genre": "성장·교육", "desc": "사람들에게 영감을 주는 이야기를 좋아하는 사람에게 추천"},
            {"title": "모모", "genre": "판타지", "desc": "따뜻한 교훈과 인간관계를 중요하게 생각하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "굿 윌 헌팅", "genre": "드라마", "desc": "성장과 인간관계 중심 이야기를 좋아하는 사람에게 추천"},
            {"title": "인사이드 아웃", "genre": "애니메이션", "desc": "감정과 공감을 중요하게 생각하는 사람에게 적합"}
        ]
    },

    "ENFP": {
        "books": [
            {"title": "해리 포터", "genre": "판타지", "desc": "모험과 상상력을 좋아하는 사람에게 추천"},
            {"title": "완득이", "genre": "성장소설", "desc": "유쾌하면서도 감동적인 이야기를 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "겨울왕국", "genre": "애니메이션·뮤지컬", "desc": "밝고 자유로운 분위기를 좋아하는 사람에게 추천"},
            {"title": "스파이더맨: 뉴 유니버스", "genre": "애니메이션·액션", "desc": "개성 넘치는 전개를 좋아하는 사람에게 적합"}
        ]
    },

    "ISTJ": {
        "books": [
            {"title": "총, 균, 쇠", "genre": "역사", "desc": "체계적이고 사실 중심의 내용을 좋아하는 사람에게 추천"},
            {"title": "이기적 유전자", "genre": "과학", "desc": "논리적 설명을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "셜록 홈즈", "genre": "추리", "desc": "분석과 추리를 좋아하는 사람에게 추천"},
            {"title": "포레스트 검프", "genre": "드라마", "desc": "성실함과 책임감을 중요하게 생각하는 사람에게 적합"}
        ]
    },

    "ISFJ": {
        "books": [
            {"title": "아몬드", "genre": "성장소설", "desc": "따뜻한 공감 이야기를 좋아하는 사람에게 추천"},
            {"title": "Little Women", "genre": "가족·드라마", "desc": "가족과 관계 중심 이야기를 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "토이 스토리", "genre": "애니메이션", "desc": "우정과 따뜻한 감동을 좋아하는 사람에게 추천"},
            {"title": "미 비포 유", "genre": "로맨스", "desc": "감성적인 이야기를 좋아하는 사람에게 적합"}
        ]
    },

    "ESTJ": {
        "books": [
            {"title": "세이노의 가르침", "genre": "자기계발", "desc": "목표 지향적이고 현실적인 사람에게 추천"},
            {"title": "부자 아빠 가난한 아빠", "genre": "경제", "desc": "실용적인 지식을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "탑건", "genre": "액션", "desc": "도전과 리더십을 좋아하는 사람에게 추천"},
            {"title": "머니볼", "genre": "스포츠·드라마", "desc": "전략적 사고를 좋아하는 사람에게 적합"}
        ]
    },

    "ESFJ": {
        "books": [
            {"title": "기적", "genre": "감동", "desc": "따뜻한 인간관계를 좋아하는 사람에게 추천"},
            {"title": "나의 라임 오렌지 나무", "genre": "성장", "desc": "감정이 풍부한 이야기를 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "겨울왕국 2", "genre": "애니메이션", "desc": "가족과 우정을 중요하게 생각하는 사람에게 추천"},
            {"title": "싱", "genre": "뮤지컬", "desc": "밝고 활기찬 분위기를 좋아하는 사람에게 적합"}
        ]
    },

    "ISTP": {
        "books": [
            {"title": "삼체", "genre": "SF", "desc": "과학적 상상력과 문제 해결을 좋아하는 사람에게 추천"},
            {"title": "노인과 바다", "genre": "문학", "desc": "조용하지만 강한 이야기를 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "존 윅", "genre": "액션", "desc": "몰입감 있는 액션을 좋아하는 사람에게 추천"},
            {"title": "포드 V 페라리", "genre": "실화·드라마", "desc": "기계와 도전을 좋아하는 사람에게 적합"}
        ]
    },

    "ISFP": {
        "books": [
            {"title": "채식주의자", "genre": "문학", "desc": "감성적이고 예술적인 분위기를 좋아하는 사람에게 추천"},
            {"title": "노르웨이의 숲", "genre": "감성소설", "desc": "조용한 감정을 표현하는 이야기를 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "너의 이름은", "genre": "애니메이션·로맨스", "desc": "감성적이고 아름다운 연출을 좋아하는 사람에게 추천"},
            {"title": "리틀 포레스트", "genre": "힐링", "desc": "잔잔한 분위기를 좋아하는 사람에게 적합"}
        ]
    },

    "ESTP": {
        "books": [
            {"title": "트렌드 코리아", "genre": "트렌드", "desc": "새로운 유행과 활동적인 삶을 좋아하는 사람에게 추천"},
            {"title": "돈의 심리학", "genre": "경제", "desc": "현실적이고 빠른 판단을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "분노의 질주", "genre": "액션", "desc": "속도감과 스릴을 좋아하는 사람에게 추천"},
            {"title": "베이비 드라이버", "genre": "액션·음악", "desc": "감각적인 스타일을 좋아하는 사람에게 적합"}
        ]
    },

    "ESFP": {
        "books": [
            {"title": "불편한 편의점", "genre": "힐링소설", "desc": "사람 냄새 나는 이야기를 좋아하는 사람에게 추천"},
            {"title": "에세이 모음집", "genre": "에세이", "desc": "가볍고 공감되는 글을 좋아하는 사람에게 적합"}
        ],
        "movies": [
            {"title": "알라딘", "genre": "뮤지컬·판타지", "desc": "화려하고 신나는 분위기를 좋아하는 사람에게 추천"},
            {"title": "주먹왕 랄프", "genre": "애니메이션", "desc": "유쾌하고 밝은 이야기를 좋아하는 사람에게 적합"}
        ]
    }
}

st.title("📚🎬 MBTI 책 & 영화 추천 프로그램")
st.write("MBTI를 선택하면 어울리는 책과 영화를 추천해드립니다!")

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(recommend_data.keys())
)

if st.button("추천 보기"):
    data = recommend_data[mbti]

    st.header(f"{mbti} 추천 책")

    for book in data["books"]:
        st.subheader(f"📖 {book['title']}")
        st.write(f"🎨 장르 : {book['genre']}")
        st.write(f"✨ 추천 이유 : {book['desc']}")
        st.divider()

    st.header(f"{mbti} 추천 영화")

    for movie in data["movies"]:
        st.subheader(f"🎬 {movie['title']}")
        st.write(f"🎭 장르 : {movie['genre']}")
        st.write(f"✨ 추천 이유 : {movie['desc']}")
        st.divider()

st.caption("※ Streamlit Cloud에서 별도 라이브러리 설치 없이 실행 가능합니다.")
