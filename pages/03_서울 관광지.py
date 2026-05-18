# Streamlit Cloud용 서울 관광지 Top10 지도 앱

아래 파일 2개를 같은 폴더에 저장한 뒤, Streamlit Cloud에 업로드하면 바로 실행됩니다.

---

## 1. app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 Top10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 관광지 Top10")
st.markdown("지도에서 관광지를 클릭하면 가까운 지하철역과 놀거리를 확인할 수 있습니다.")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역",
        "fun": "한복 체험, 궁궐 산책, 전통 사진 촬영"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "subway": "명동역",
        "fun": "쇼핑, 길거리 음식, 화장품 투어"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역",
        "fun": "야경 감상, 케이블카, 사랑의 자물쇠"
    },
    {
        "name": "홍대거리",
        "lat": 37.556337,
        "lon": 126.922652,
        "subway": "홍대입구역",
        "fun": "버스킹, 카페 탐방, 쇼핑"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "subway": "안국역",
        "fun": "한옥 구경, 전통 문화 체험, 사진 촬영"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102486,
        "subway": "잠실역",
        "fun": "전망대, 쇼핑몰, 아쿠아리움"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009223,
        "subway": "동대문역사문화공원역",
        "fun": "야경, 디자인 전시, 패션 쇼핑"
    },
    {
        "name": "인사동",
        "lat": 37.574018,
        "lon": 126.984900,
        "subway": "안국역",
        "fun": "전통 찻집, 기념품 쇼핑, 공예 체험"
    },
    {
        "name": "코엑스",
        "lat": 37.511684,
        "lon": 127.059151,
        "subway": "삼성역",
        "fun": "별마당도서관, 쇼핑, 전시회"
    },
    {
        "name": "한강공원",
        "lat": 37.528726,
        "lon": 126.932337,
        "subway": "여의나루역",
        "fun": "자전거, 피크닉, 야경 감상"
    }
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 선택된 장소 저장
if "selected_place" not in st.session_state:
    st.session_state.selected_place = None

# 마커 추가
for place in places:
    popup_html = f"""
    <b>{place['name']}</b><br>
    클릭 후 아래 설명 확인
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=1200, height=600)

# 클릭 이벤트 처리
if map_data["last_object_clicked_popup"]:
    clicked_name = map_data["last_object_clicked_popup"].split("<br>")[0].replace("<b>", "").replace("</b>", "")

    for place in places:
        if place["name"] == clicked_name:
            st.session_state.selected_place = place

# 하단 정보 출력
st.markdown("---")
st.subheader("📍 관광지 정보")

if st.session_state.selected_place:
    selected = st.session_state.selected_place

    st.success(
        f"{selected['name']} → 가까운 지하철역: {selected['subway']} | 놀거리: {selected['fun']}"
    )
else:
    st.info("지도에서 관광지를 클릭해보세요!")
```

---

## 2. requirements.txt

```txt
streamlit
folium
streamlit-folium
```

---

## 실행 방법

### 로컬 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit Cloud 배포

1. GitHub에 app.py 와 requirements.txt 업로드
2. Streamlit Cloud 접속
3. GitHub 저장소 연결
4. Main file path를 app.py로 설정
5. Deploy 클릭
