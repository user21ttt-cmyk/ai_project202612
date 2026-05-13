import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼")

# MBTI별 진로 데이터
career_data = {
    "INTJ": [
        {
            "job": "데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 전략적으로 생각하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        },
        {
            "job": "건축가",
            "major": "건축학과",
            "personality": "창의적이며 계획 세우기를 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "INTP": [
        {
            "job": "프로그래머",
            "major": "컴퓨터공학과",
            "personality": "분석적이고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "연구원",
            "major": "화학과, 물리학과",
            "personality": "호기심이 많고 탐구를 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ENTJ": [
        {
            "job": "기업 경영인",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표 지향적인 사람",
            "salary": "평균 연봉 약 7,000만원"
        },
        {
            "job": "변호사",
            "major": "법학과",
            "personality": "논리적이며 설득력이 있는 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],
    "ENTP": [
        {
            "job": "마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 도전을 즐기는 사람",
            "salary": "평균 연봉 약 4,800만원"
        },
        {
            "job": "창업가",
            "major": "경영학과",
            "personality": "새로운 시도를 좋아하고 활동적인 사람",
            "salary": "평균 연봉 다양함"
        }
    ],
    "INFJ": [
        {
            "job": "상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 배려심 있는 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "작가",
            "major": "문예창작학과",
            "personality": "상상력이 풍부하고 감수성이 높은 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "INFP": [
        {
            "job": "디자이너",
            "major": "시각디자인학과",
            "personality": "창의적이고 감성적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻하고 남을 돕는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "ENFJ": [
        {
            "job": "교사",
            "major": "교육학과",
            "personality": "사람들을 이끄는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "인사 담당자",
            "major": "경영학과",
            "personality": "소통 능력이 뛰어나고 친절한 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ENFP": [
        {
            "job": "유튜버",
            "major": "미디어커뮤니케이션학과",
            "personality": "활발하고 창의적인 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 풍부하고 사교적인 사람",
            "salary": "평균 연봉 약 4,700만원"
        }
    ],
    "ISTJ": [
        {
            "job": "공무원",
            "major": "행정학과",
            "personality": "책임감이 강하고 성실한 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 체계적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "배려심 있고 책임감 있는 사람",
            "salary": "평균 연봉 약 4,700만원"
        },
        {
            "job": "유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 인내심 있는 사람",
            "salary": "평균 연봉 약 3,900만원"
        }
    ],
    "ESTJ": [
        {
            "job": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "관리자",
            "major": "경영학과",
            "personality": "조직 관리에 능숙한 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사교적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 뛰어난 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ISTP": [
        {
            "job": "정비사",
            "major": "자동차공학과",
            "personality": "손재주가 좋고 실용적인 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 집중력이 높은 사람",
            "salary": "평균 연봉 약 8,000만원"
        }
    ],
    "ISFP": [
        {
            "job": "플로리스트",
            "major": "원예학과",
            "personality": "감각적이고 섬세한 사람",
            "salary": "평균 연봉 약 3,500만원"
        },
        {
            "job": "패션 디자이너",
            "major": "패션디자인학과",
            "personality": "예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,500만원"
        }
    ],
    "ESTP": [
        {
            "job": "영업 전문가",
            "major": "경영학과",
            "personality": "적극적이고 자신감 있는 사람",
            "salary": "평균 연봉 약 5,000만원"
        },
        {
            "job": "운동선수",
            "major": "체육학과",
            "personality": "활동적이고 경쟁을 좋아하는 사람",
            "salary": "평균 연봉 다양함"
        }
    ],
    "ESFP": [
        {
            "job": "배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 활발한 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "이벤트 기획자",
            "major": "관광경영학과",
            "personality": "사람들과 어울리기를 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ]
}

st.title("💼 MBTI 진로 추천 프로그램")
st.write("자신의 MBTI를 선택하면 추천 진로 2가지를 알려줍니다!")

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(career_data.keys())
)

if st.button("진로 추천 보기"):
    st.subheader(f"{mbti} 유형 추천 진로")

    careers = career_data[mbti]

    for idx, career in enumerate(careers, start=1):
        st.markdown(f"## {idx}. {career['job']}")
        st.write(f"📚 추천 학과 : {career['major']}")
        st.write(f"😊 어울리는 성격 : {career['personality']}")
        st.write(f"💰 {career['salary']}")
        st.divider()

st.caption("※ 연봉은 평균적인 예시이며 실제와 차이가 있을 수 있습니다.")
