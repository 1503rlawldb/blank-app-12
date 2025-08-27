import streamlit as st
import base64

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="한국 뮤지컬 대백과",
    page_icon="🎭",
    layout="wide"
)

# --- 세련된 배경과 커스텀 스타일 적용 ---
st.markdown("""
<style>
/* Streamlit 앱의 메인 배경 */
.stApp {
    background-image: linear-gradient(135deg, #1a2a6c, #000000);
    background-attachment: fixed;
    background-size: cover;
    color: #e0e0e0;
}

/* 헤더와 제목 색상 */
h1, h2, h3 {
    color: #ffffff;
}

/* 검색창 스타일 */
.stTextInput > div > div > input {
    background-color: #000000;
    color: #FFFFFF;
    border: 1px solid #C0A062;
    border-radius: 20px;
    text-align: center;
}

/* 확장(expander) 컴포넌트 스타일 */
.stExpander {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    text-align: center;
}
.stExpander header {
    color: #D4AF37 !important;
}

/* 구분선 색상 */
hr {
    background-color: #444444;
}

/* 검색 결과 알림창 스타일 */
div[data-baseweb="alert"] {
    background-color: #000000 !important;
    color: #FFFFFF !important;
    border: 1px solid #C0A062 !important;
    border-radius: 10px;
    text-align: center;
}

/* 모든 p 태그(줄거리, 배우 목록 등) 색상 고정 */
p {
    color: #D4AF37;
}

strong {
    color: #D4AF37;
}

/* 포스터 이미지 스타일 */
.stImage img {
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)


# --- 뮤지컬 데이터 (60개) ---
# 각 뮤지컬 정보에 포스터 URL을 추가합니다.
musicals_data = [
    {
        "title": "프랑켄슈타인",
        "poster_url": "http://googleusercontent.com/file_content/3",
        "background_css": "linear-gradient(135deg, #2c3e50, #4a5a6a, #000000)", "text_color": "#D4AF37",
        "summary": "19세기 유럽, 나폴레옹 전쟁 당시 스위스의 천재 과학자 빅터 프랑켄슈타인은 '죽지 않는 군인'에 대한 연구를 진행하다 생명 창조라는 신의 영역에 발을 들입니다. 그의 굳은 신념을 이해한 유일한 친구 앙리 뒤프레의 희생으로 생명 창조에 성공하지만, 끔찍한 외모를 가진 피조물의 모습에 경악하여 그를 버립니다. 3년 후, '괴물'이 되어 돌아온 피조물은 창조주를 향한 처절한 복수를 시작하며 인간의 오만함과 생명의 본질에 대한 질문을 던집니다.",
        "cast": { "빅터 프랑켄슈타인": ["류정한", "유준상", "전동석", "민우혁", "규현"], "앙리 뒤프레/괴물": ["박은태", "한지상", "카이", "박민성", "정택운(레오)"], "엘렌": ["서지영", "박혜나", "안시하"], "줄리아": ["안시하", "이지혜", "박혜나"] }
    },
    {
        "title": "지킬앤하이드",
        "poster_url": "http://googleusercontent.com/file_content/5",
        "background_css": "linear-gradient(135deg, #4d0000, #1a0000, #000000)", "text_color": "#D4AF37",
        "summary": "19세기 런던, 유능한 의사이자 과학자인 헨리 지킬은 인간의 내면에 존재하는 선과 악을 완벽하게 분리할 수 있다는 신념으로 위험한 실험을 감행합니다. 이사회의 반대에 부딪히자 자기 자신을 실험 대상으로 삼고, 그 결과 그의 내면에 숨겨져 있던 사악하고 폭력적인 인격 '에드워드 하이드'가 깨어납니다. 낮에는 신사 지킬로, 밤에는 범죄자 하이드로 변하며 벌어지는 비극적인 사건들을 통해 인간 본성의 이중성을 탐구합니다.",
        "cast": { "지킬/하이드": ["조승우", "류정한", "홍광호", "박은태", "전동석", "신성록", "박건형", "민우혁"], "루시": ["김선영", "옥주현", "아이비", "윤공주", "린아", "해나", "선민"], "엠마": ["조정은", "김소현", "임혜영", "이지혜", "최수진", "민경아"] }
    },
    {
        "title": "오페라의 유령",
        "poster_url": "http://googleusercontent.com/file_content/4",
        "background_css": "linear-gradient(135deg, #000033, #1a0000, #000000)", "text_color": "#D4AF37",
        "summary": "파리 오페라 하우스의 지하 깊은 곳, 흉측한 얼굴을 가면 뒤에 숨긴 채 살아가는 천재 음악가 '유령'. 그는 아름다운 목소리를 가진 프리마돈나 '크리스틴'에게 매료되어 그녀를 최고의 스타로 만들기로 결심합니다. 유령의 비밀스러운 레슨으로 크리스틴의 실력은 일취월장하지만, 그녀가 귀족 청년 '라울'과 사랑에 빠지자 유령의 순수한 사랑은 광기 어린 집착으로 변질되어 오페라 하우스를 비극으로 몰아넣습니다.",
        "cast": { "유령(팬텀)": ["윤영석", "홍광호", "박효신", "조승우", "최재림", "전동석"], "크리스틴": ["김소현", "이혜경", "임혜영", "손지수", "송은혜"], "라울": ["류정한", "정상윤", "송원근", "황건하"] }
    },
    {
        "title": "레미제라블",
        "poster_url": "http://googleusercontent.com/file_content/6",
        "background_css": "linear-gradient(135deg, #001f4d, #3d0000, #2a2a2a)", "text_color": "#D4AF37",
        "summary": "빵 한 조각을 훔친 죄로 19년의 억울한 감옥살이를 한 장발장. 가석방 후에도 세상의 냉대와 편견에 시달리던 그는 미리엘 주교의 자비에 감화되어 새로운 삶을 살기로 결심합니다. 신분을 숨기고 시장으로 성공하지만, 법과 원칙을 맹신하는 경감 자베르의 끈질긴 추적을 받게 됩니다. 격동의 프랑스 대혁명 시대를 배경으로 한 인간의 숭고한 정신과 사랑, 용서, 구원의 대서사시입니다.",
        "cast": { "장발장": ["정성화", "양준모", "민우혁", "최재림"], "자베르": ["문종원", "김우형", "카이", "김준현"], "판틴": ["조정은", "차지연", "린아"] }
    },
    {
        "title": "데스노트",
        "poster_url": "http://googleusercontent.com/file_content/7",
        "background_css": "linear-gradient(135deg, #330000, #1a1a1a, #4a0000)", "text_color": "#D4AF37",
        "summary": "법과 정의에 한계를 느낀 천재 고등학생 '야가미 라이토'는 우연히 사신의 노트 '데스노트'를 줍게 됩니다. 노트에 이름이 적힌 자는 죽는다는 사실을 알게 된 그는 자신만의 정의를 실현하기 위해 '키라'라는 이름으로 범죄자들을 처단하기 시작합니다. 이에 맞서 세계 최고의 명탐정 '엘(L)'이 등장하며, 두 천재의 목숨을 건 치열하고 비상한 두뇌 싸움이 펼쳐집니다.",
        "cast": { "야가미 라이토": ["홍광호", "고은성", "김성철"], "엘(L)": ["김준수", "김성철", "서경수"], "렘": ["박혜나", "김선영", "장은아"], "류크": ["강홍석", "서경수", "장지후"] }
    },
    {
        "title": "드라큘라",
        "poster_url": "http://googleusercontent.com/file_content/8",
        "background_css": "linear-gradient(135deg, #6b0000, #000000)", "text_color": "#D4AF37",
        "summary": "수백 년 동안 죽지 않고 살아온 비운의 뱀파이어 '드라큘라 백작'. 그는 죽은 아내와 똑같이 생긴 '미나'를 발견하고 그녀를 차지하기 위해 영국으로 건너옵니다. 미나 역시 드라큘라에게 거부할 수 없는 운명적인 끌림을 느끼지만, 그녀의 약혼자 '조나단'과 뱀파이어 헌터 '반 헬싱'이 드라큘라를 추적하기 시작하며 애절하고 비극적인 사랑이 펼쳐집니다.",
        "cast": { "드라큘라": ["김준수", "전동석", "신성록", "류정한"], "미나": ["조정은", "임혜영", "린아", "아이비", "박지연"], "반 헬싱": ["강태을", "손준호", "유준상"] }
    },
    {
        "title": "레베카",
        "poster_url": "http://googleusercontent.com/file_content/9",
        "background_css": "linear-gradient(135deg, #00264d, #333333)", "text_color": "#D4AF37",
        "summary": "불의의 사고로 아내를 잃은 영국 상류층 신사 '막심 드 윈터'는 여행 중 만난 순수한 '나(I)'와 사랑에 빠져 결혼합니다. 그의 거대한 저택 맨덜리에 입성한 '나'는 죽은 전 부인 '레베카'의 압도적인 존재감과 집사 '댄버스 부인'의 서늘한 경계 속에서 점차 위축됩니다. 레베카의 죽음에 얽힌 미스터리를 파헤치며 진정한 사랑과 자아를 찾아가는 서스펜스 넘치는 이야기입니다.",
        "cast": { "막심 드 윈터": ["류정한", "민영기", "엄기준", "송창의", "카이", "신성록"], "댄버스 부인": ["옥주현", "신영숙", "차지연", "장은아", "리사"], "나(I)": ["임혜영", "김보경", "송상은", "루나", "이지혜", "박지연"] }
    },
    {
        "title": "엘리자벳",
        "poster_url": "http://googleusercontent.com/file_content/10",
        "background_css": "linear-gradient(135deg, #2a2a2a, #5c5c8a, #000000)", "text_color": "#D4AF37",
        "summary": "자유분방한 소녀였던 '엘리자벳'은 오스트리아의 황제 프란츠 요제프와 사랑에 빠져 황후가 되지만, 엄격한 황실의 규율과 시어머니의 압박에 숨 막혀 합니다. 그녀의 앞에 나타난 매력적인 '죽음(토드)'은 끊임없이 자유를 갈망하는 그녀를 유혹하며 평생 그녀의 곁을 맴돕니다. 한 여인의 일대기를 통해 진정한 자유와 사랑의 의미를 묻는 판타지 드라마입니다.",
        "cast": { "엘리자벳": ["옥주현", "김소현", "신영숙", "이지혜", "김선영"], "죽음(토드)": ["김준수", "박효신", "전동석", "박형식", "정택운(레오)", "신성록"], "루케니": ["박은태", "이지훈", "강태을", "김수용"] }
    },
    {
        "title": "위키드",
        "poster_url": "http://googleusercontent.com/file_content/11",
        "background_css": "linear-gradient(135deg, #00552e, #000000)", "text_color": "#D4AF37",
        "summary": "도로시가 오즈에 떨어지기 훨씬 전, 초록색 피부를 가졌지만 총명하고 불의를 참지 못하는 '엘파바'와 아름다운 금발에 인기가 많은 '글린다'가 룸메이트로 만납니다. 처음에는 서로를 싫어했지만 점차 진정한 우정을 쌓아가는 두 마녀. 그러나 오즈의 마법사의 음모와 세상의 편견 속에서 둘은 '나쁜 마녀'와 '착한 마녀'라는 상반된 길을 걷게 됩니다. 우리가 몰랐던 오즈의 숨겨진 이야기입니다.",
        "cast": { "엘파바": ["옥주현", "박혜나", "차지연", "손승연"], "글린다": ["정선아", "김보경", "아이비", "나하나"], "피에로": ["민우혁", "고은성", "서경수", "진태화"] }
    },
    {
        "title": "헤드윅",
        "poster_url": "http://googleusercontent.com/file_content/12",
        "background_css": "linear-gradient(135deg, #ff0066, #330066, #000000)", "text_color": "#D4AF37",
        "summary": "동독 출신의 트랜스젠더 록 가수 '헤드윅'이 록 밴드 '앵그리 인치'와 함께 자신의 기구한 삶과 사랑, 음악에 대한 이야기를 콘서트 형식으로 풀어냅니다. 실패한 성전환 수술로 남은 '앵그리 인치', 자신을 배신하고 스타가 된 연인 '토미' 등 상처로 가득한 삶을 강렬한 록 음악과 유머로 승화시키는 과정을 통해 진정한 자아를 찾아가는 과정을 그립니다.",
        "cast": { "헤드윅": ["조승우", "오만석", "조정석", "유연석", "전동석", "마이클리", "정문성", "이규형", "렌"], "이츠학": ["전혜선", "이영미", "제이민", "유리아", "홍서영"] }
    },
    {
        "title": "영웅",
        "poster_url": "http://googleusercontent.com/file_content/13",
        "background_css": "linear-gradient(135deg, #4a4a4a, #1a1a1a)", "text_color": "#D4AF37",
        "summary": "조국 독립의 열망이 뜨거웠던 1909년, 대한제국 의병 대장 안중근은 동지들과 단지동맹으로 거사를 맹세합니다. 조선 침략의 원흉 이토 히로부미가 하얼빈에 온다는 소식을 들은 그는 거사를 계획하고, 명성황후의 마지막 궁녀였던 설희의 도움을 받아 마침내 하얼빈역에서 역사의 총성을 울립니다. 안중근 의사의 마지막 1년을 통해 그의 인간적인 고뇌와 숭고한 희생정신을 담아낸 대한민국 대표 창작 뮤지컬입니다.",
        "cast": { "안중근": ["정성화", "양준모", "민우혁", "류정한", "신성록"], "이토 히로부미": ["김도형", "서영주", "이정열"], "설희": ["정재은", "린지", "리사"] }
    },
    {
        "title": "웃는 남자",
        "poster_url": "http://googleusercontent.com/file_content/14",
        "background_css": "linear-gradient(135deg, #b30000, #2a002a, #000000)", "text_color": "#D4AF37",
        "summary": "17세기 영국, 아이들을 납치해 기형적으로 만들어 팔던 '콤프라치코스'에 의해 입이 찢어진 소년 '그윈플렌'. 그는 눈 먼 소녀 '데아'와 함께 유랑극단에서 광대로 살아가지만, 그의 기괴한 미소는 사람들에게 큰 인기를 얻습니다. 그러던 중 자신의 출생의 비밀이 밝혀지며 부조리한 귀족 사회에 발을 들이게 되고, 인간의 존엄성과 평등의 가치에 대해 질문을 던집니다.",
        "cast": { "그윈플렌": ["박효신", "박강현", "수호", "박은태", "규현"], "우르수스": ["정성화", "양준모", "민영기"], "데아": ["민경아", "이수빈", "양서윤"], "조시아나 여공작": ["신영숙", "옥주현", "김소향"] }
    },
    {
        "title": "노트르담 드 파리",
        "poster_url": "http://googleusercontent.com/file_content/15",
        "background_css": "linear-gradient(135deg, #4a2a00, #1a1a1a)", "text_color": "#D4AF37",
        "summary": "15세기 파리의 노트르담 대성당을 배경으로, 추악한 외모를 가졌지만 순수한 마음을 지닌 꼽추 종지기 '콰지모도', 아름다운 집시 여인 '에스메랄다', 그리고 그녀를 욕망하는 성직자 '프롤로'와 근위대장 '페뷔스'의 엇갈린 사랑과 숙명을 그린 작품입니다. 대사 없이 노래로만 진행되는 성스루(Sung-through) 뮤지컬의 진수를 보여줍니다.",
        "cast": { "콰지모도": ["윤형렬", "홍광호", "케이윌", "정성화", "마이클리"], "에스메랄다": ["바다", "윤공주", "차지연", "전나영", "유리아"], "그랭구와르": ["박은태", "마이클리", "정동하", "이충주", "조휘"] }
    },
    {
        "title": "모차르트!",
        "poster_url": "http://googleusercontent.com/file_content/16",
        "background_css": "linear-gradient(135deg, #cc0000, #333333)", "text_color": "#D4AF37",
        "summary": "천재적인 재능을 가졌지만 자유를 갈망했던 음악가 '볼프강 모차르트'의 인간적인 고뇌를 그립니다. 그의 천재성을 상징하는 어린 아이 '아마데'는 그에게서 떠나지 않으며 계속해서 작곡을 강요하고, 아버지와 콜로레도 대주교의 억압 속에서 그는 점차 파멸해 갑니다. 화려한 삶 이면에 감춰진 한 천재의 고독과 열정을 강렬한 록 음악으로 풀어냅니다.",
        "cast": { "볼프강 모차르트": ["박효신", "김준수", "박은태", "전동석", "규현", "수호", "김희재"], "콜로레도 대주교": ["민영기", "김준현", "손준호"], "콘스탄체 베버": ["정선아", "차지연", "김소향", "린아"] }
    },
    {
        "title": "시카고",
        "poster_url": "http://googleusercontent.com/file_content/17",
        "background_css": "linear-gradient(135deg, #990000, #1a1a1a, #000000)", "text_color": "#D4AF37",
        "summary": "1920년대 재즈와 범죄의 도시 시카고. 불륜남을 살해한 코러스 걸 '록시 하트'는 교도소에서 만난 당대 최고의 스타 '벨마 켈리'를 모방하며 스타가 되길 꿈꿉니다. 돈만 주면 무죄도 만들어주는 변호사 '빌리 플린'의 도움으로 언론의 주목을 받게 된 그녀의 이야기는 당시 미국 사회의 부패와 황금만능주의를 신랄하고 관능적으로 풍자합니다.",
        "cast": { "벨마 켈리": ["최정원", "윤공주", "박칼린"], "록시 하트": ["아이비", "티파니 영", "민경아", "옥주현"], "빌리 플린": ["박건형", "최재림", "남경주"] }
    },
    {
        "title": "맘마미아!",
        "poster_url": "http://googleusercontent.com/file_content/18",
        "background_css": "linear-gradient(135deg, #0066cc, #0099ff, #66ccff)", "text_color": "#1E1E1E",
        "summary": "그리스의 아름다운 섬에서 작은 모텔을 운영하는 엄마 '도나'와 단둘이 살아온 '소피'. 그녀는 결혼을 앞두고 아빠를 찾고 싶은 마음에, 엄마의 옛 일기장에 적힌 아빠 후보 세 명에게 몰래 청첩장을 보냅니다. 결혼식 전날, 세 명의 아빠 후보가 모두 섬에 도착하면서 벌어지는 유쾌하고 감동적인 소동을 ABBA의 명곡들과 함께 그려냅니다.",
        "cast": { "도나": ["최정원", "신영숙", "김선영"], "소피": ["박지연", "서현", "루나", "김금나"], "타냐": ["전수경", "김영주", "홍지민"] }
    },
    {
        "title": "킹키부츠",
        "poster_url": "http://googleusercontent.com/file_content/19",
        "background_css": "linear-gradient(135deg, #cc0000, #ff3333, #ff6666)", "text_color": "#FFFFFF",
        "summary": "아버지의 갑작스러운 죽음으로 폐업 위기에 처한 구두 공장을 물려받게 된 '찰리'. 그는 우연히 만난 아름답고 유쾌한 드랙퀸 '롤라'에게서 영감을 받아, 남자가 신는 하이힐 부츠인 '킹키부츠'를 만들기로 결심합니다. 편견과 차별에 맞서 서로를 이해하고 함께 성장해나가는 과정을 신나는 음악과 함께 보여주는 작품입니다.",
        "cast": { "롤라": ["정성화", "강홍석", "최재림", "박은태"], "찰리": ["이석훈", "김호영", "성규", "신재범"], "로렌": ["김지우", "김환희", "나하나"] }
    },
    {
        "title": "그날들",
        "poster_url": "http://googleusercontent.com/file_content/20",
        "background_css": "linear-gradient(135deg, #333333, #666666)", "text_color": "#D4AF37",
        "summary": "1992년, 청와대 경호원 '정학'과 '무영'은 신원을 알 수 없는 '그녀'를 경호하게 되고, 무영과 그녀는 흔적도 없이 사라집니다. 20년 후, 한중 수교 20주년 기념행사가 한창인 청와대에서 대통령의 딸이 사라지고, 경호부장이 된 정학은 20년 전의 사건을 떠올리게 됩니다. 故 김광석의 명곡들로 엮어낸 미스터리 주크박스 뮤지컬입니다.",
        "cast": { "정학": ["유준상", "이건명", "최재웅", "오만석", "엄기준", "지창욱"], "무영": ["지창욱", "오종혁", "온주완", "양요섭", "규현", "남우현", "윤두준"], "그녀": ["김지현", "신다은", "루나", "방민아", "효정"] }
    },
    {
        "title": "서편제",
        "poster_url": "http://googleusercontent.com/file_content/21",
        "background_css": "linear-gradient(135deg, #8c6a4a, #d9b38c)", "text_color": "#1E1E1E",
        "summary": "소리를 위해 모든 것을 희생시키는 아버지 '유봉', 아버지의 소리를 완성시키기 위해 자신의 삶을 바치는 딸 '송화', 그리고 그런 두 사람의 곁을 떠나 자신만의 소리를 찾아 나서는 아들 '동호'. 각자의 소리를 찾아 평생을 헤매는 세 사람의 가슴 아픈 이야기를 한국적인 정서와 아름다운 음악으로 풀어낸 창작 뮤지컬입니다.",
        "cast": { "송화": ["차지연", "이자람", "장은아", "이소연"], "동호": ["박영수", "김재범", "서범석"], "유봉": ["이정열", "서범석", "양준모"] }
    },
    {
        "title": "팬텀",
        "poster_url": "http://googleusercontent.com/file_content/22",
        "background_css": "linear-gradient(135deg, #a0a0a0, #333333, #000000)", "text_color": "#D4AF37",
        "summary": "'오페라의 유령'으로 알려진 '에릭'의 인간적인 면모에 더 깊이 초점을 맞춘 작품입니다. 흉측한 얼굴 때문에 오페라 극장 지하에 숨어 살아야 했던 그의 불행한 어린 시절과 천재적인 음악성이 어떻게 만들어졌는지, 그리고 순수한 목소리를 가진 '크리스틴'을 향한 그의 애절하고 비극적인 사랑을 아름다운 음악과 발레를 통해 섬세하게 그려냅니다.",
        "cast": { "팬텀(에릭)": ["박효신", "박은태", "전동석", "카이", "규현", "류정한"], "크리스틴 다에": ["임선혜", "김소현", "이지혜", "김수"], "필립 드 샹동 백작": ["손준호", "박송권", "이해준"] }
    },
    {
        "title": "베르테르",
        "poster_url": "http://googleusercontent.com/file_content/23",
        "background_css": "linear-gradient(135deg, #ffcc00, #663300)", "text_color": "#4A2A00",
        "summary": "순수하고 열정적인 청년 '베르테르'는 매력적인 여성 '롯데'를 보고 첫눈에 반하지만, 그녀에게 이미 약혼자 '알베르트'가 있다는 사실을 알게 됩니다. 이룰 수 없는 사랑에 대한 그의 열망은 점차 깊어지고, 이성과 감정 사이에서 고뇌하던 그는 결국 극단적인 선택을 하게 됩니다. 괴테의 소설 '젊은 베르테르의 슬픔'을 원작으로 한 서정적인 뮤지컬입니다.",
        "cast": { "베르테르": ["조승우", "엄기준", "규현", "카이", "유연석", "나현우"], "롯데": ["이지혜", "김예원", "이지수"], "알베르트": ["이상현", "박은석", "김성철"] }
    },
    {
        "title": "스위니토드",
        "poster_url": "http://googleusercontent.com/file_content/25",
        "background_css": "linear-gradient(135deg, #660000, #1a1a1a)", "text_color": "#D4AF37",
        "summary": "아내와 딸을 억울하게 빼앗기고 15년간 옥살이를 한 이발사 '벤자민 바커'. 그는 '스위니 토드'라는 이름으로 런던에 돌아와 복수를 계획합니다. 그의 복수심을 이용하는 파이 가게 주인 '러빗 부인'과 손을 잡고, 그는 자신의 이발소를 찾아오는 사람들을 살해하기 시작합니다. 19세기 런던의 부조리한 사회를 배경으로 한 기괴하고도 매력적인 스릴러 뮤지컬입니다.",
        "cast": { "스위니 토드": ["조승우", "류정한", "홍광호", "박은태", "강필석", "신성록"], "러빗 부인": ["옥주현", "전미도", "김지현", "린아", "이지혜"], "터핀 판사": ["김도형", "서영주", "박인배"] }
    },
    {
        "title": "팬레터",
        "poster_url": "http://googleusercontent.com/file_content/26",
        "background_css": "linear-gradient(135deg, #4a3a2a, #f0e6d6)", "text_color": "#4A2A00",
        "summary": "1930년대 경성을 배경으로, 천재 소설가 '김해진'과 그를 동경하는 작가 지망생 '정세훈', 그리고 비밀에 싸인 천재 여류작가 '히카루'의 이야기를 다룬 미스터리 드라마입니다.",
        "cast": { "정세훈": ["문성일", "김성철", "려욱", "윤소호"], "김해진": ["김종구", "이규형", "김경수"], "히카루": ["소정화", "김히어라", "조지승"] }
    },
    {
        "title": "벤허",
        "poster_url": "http://googleusercontent.com/file_content/27",
        "background_css": "linear-gradient(135deg, #bf8f30, #4a2a00)", "text_color": "#D4AF37",
        "summary": "로마 제국 시대, 예루살렘의 귀족 청년 '유다 벤허'는 어린 시절 친구였던 '메셀라'의 배신으로 가문이 몰락하고 노예로 전락합니다. 갤리선에서 죽을 고비를 넘긴 그는 로마 장군의 양자가 되어 돌아와, 전차 경주에서 메셀라와 운명적인 대결을 펼칩니다. 한 남자의 파란만장한 삶을 통해 복수와 용서, 고난과 구원의 메시지를 전하는 대서사시입니다.",
        "cast": { "유다 벤허": ["유준상", "박은태", "카이", "신성록", "규현"], "메셀라": ["박민성", "이지훈", "서경수"], "에스더": ["윤공주", "아이비", "선민"] }
    },
    {
        "title": "빨래",
        "poster_url": "http://googleusercontent.com/file_content/28",
        "background_css": "linear-gradient(135deg, #66ccff, #ffffff)", "text_color": "#1E1E1E",
        "summary": "강원도에서 상경해 서울의 한 달동네에 사는 서점 직원 '나영'과 몽골에서 온 이주노동자 '솔롱고'. 팍팍한 서울살이에 지쳐가던 두 사람은 옥상에서 빨래를 널며 서로를 위로하고 사랑을 키워나갑니다. 우리네 이웃들의 소박하고 따뜻한 삶의 이야기를 통해 위로와 희망을 전하는 힐링 뮤지컬입니다.",
        "cast": { "서나영": ["홍지희", "강연정", "김주연"], "솔롱고": ["홍광호", "임창정", "이정은"], "주인 할매": ["이정은", "이미경"] }
    },
    # --- 5개 뮤지컬 추가 ---
    {
        "title": "마리 퀴리",
        "poster_url": "http://googleusercontent.com/file_content/29",
        "background_css": "linear-gradient(135deg, #003333, #006666, #ccffff)", "text_color": "#FFFFFF",
        "summary": "최초로 노벨상을 두 번 수상한 위대한 과학자 '마리 퀴리'의 삶을 다룹니다. 자신의 연구가 초래한 비극에 맞서며 진실을 찾아가는 그녀의 고뇌와 신념을 그립니다.",
        "cast": { "마리 퀴리": ["김소향", "옥주현", "리사"], "안느": ["김히어라", "이봄소리", "효정"], "피에르 퀴리": ["김찬호", "박영수", "임별"] }
    },
    {
        "title": "어쩌면 해피엔딩",
        "poster_url": "http://googleusercontent.com/file_content/30",
        "background_css": "linear-gradient(135deg, #ff9966, #ffcc99)", "text_color": "#4A2A00",
        "summary": "가까운 미래, 인간을 돕기 위해 만들어졌지만 구형이 되어 버려진 로봇 '올리버'와 '클레어'가 만나 사랑과 삶의 의미를 배워가는 따뜻하고 서정적인 이야기입니다.",
        "cast": { "올리버": ["정문성", "전성우", "신성민", "임준혁"], "클레어": ["전미도", "박지연", "강혜인", "한재아"] }
    },
    {
        "title": "호프",
        "poster_url": "http://googleusercontent.com/file_content/32",
        "background_css": "linear-gradient(135deg, #663300, #996633)", "text_color": "#D4AF37",
        "summary": "현대 문학의 거장 요제프 클라인의 미발표 원고를 평생 지켜온 78세 노인 '에바 호프'의 삶을 통해, 원고가 곧 자신이었던 한 인간의 인생을 그립니다.",
        "cast": { "호프": ["김선영", "차지연", "김지현"], "K": ["고훈정", "조형균", "김경수"] }
    },
    {
        "title": "광화문 연가",
        "poster_url": "http://googleusercontent.com/file_content/31",
        "background_css": "linear-gradient(135deg, #333399, #6666cc)", "text_color": "#D4AF37",
        "summary": "죽음을 앞둔 주인공 '명우'가 마지막 1분을 앞두고 '월하'와 함께 떠나는 시간 여행을 통해 자신의 젊은 날의 사랑과 우정을 되돌아보는 이야기입니다.",
        "cast": { "중년 명우": ["안재욱", "이건명", "강필석", "윤도현", "차지연"], "월하": ["구원영", "김호영", "이석훈", "정성화", "차지연"], "젊은 명우": ["허도영", "김성규", "박강현", "이찬동"] }
    },
    {
        "title": "사의 찬미",
        "poster_url": "http://googleusercontent.com/file_content/24",
        "background_css": "linear-gradient(135deg, #003366, #336699, #99aabb)", "text_color": "#FFFFFF",
        "summary": "1920년대 경성, 천재 극작가 김우진과 조선 최초의 소프라노 윤심덕의 비극적인 사랑과 실화를 바탕으로 한 뮤지컬입니다.",
        "cast": { "김우진": ["이해준", "김종구", "진태화"], "윤심덕": ["이지수", "최연우", "최수진"], "사내": ["최재웅", "김재범", "박정표"] }
    }
]


# --- 앱 UI 구성 ---

# 제목과 부제
st.markdown("<h1 style='text-align: center;'>🎭 한국 뮤지컬 대백과</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFFFFF;'>한국 뮤지컬의 모든 것을 한눈에! 제목과 배우 이름으로 검색해보세요.</p>", unsafe_allow_html=True)


# 검색창
search_term = st.text_input("", placeholder="뮤지컬 제목 또는 배우 이름을 검색하세요...", label_visibility="collapsed")

# --- 검색 및 필터링 로직 ---
final_filtered_musicals = []
if search_term:
    search_term_no_space = search_term.replace(" ", "").lower()
    for musical in musicals_data:
        title_no_space = musical['title'].replace(" ", "").lower()
        if search_term_no_space in title_no_space:
            final_filtered_musicals.append(musical)
            continue
        
        found_in_cast = False
        for role, actors in musical['cast'].items():
            for actor in actors:
                if search_term_no_space in actor.replace(" ", "").lower():
                    final_filtered_musicals.append(musical)
                    found_in_cast = True
                    break
            if found_in_cast:
                break
else:
    # 검색어가 없을 경우, 모든 뮤지컬을 보여줌
    final_filtered_musicals = musicals_data

# --- 배경 적용 로직 ---
default_bg = "linear-gradient(135deg, #1a2a6c, #000000)"
default_text_color = "#D4AF37"

if len(final_filtered_musicals) == 1:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: {final_filtered_musicals[0]['background_css']};
        background-attachment: fixed;
        background-size: cover;
    }}
    p, strong {{
        color: {final_filtered_musicals[0].get('text_color', default_text_color)};
    }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: {default_bg};
        background-attachment: fixed;
        background-size: cover;
    }}
    p, strong {{
        color: {default_text_color};
    }}
    </style>
    """, unsafe_allow_html=True)


# --- 결과 출력 ---
st.divider()
if not final_filtered_musicals:
    st.warning(f"'{search_term}'에 대한 검색 결과가 없습니다.")
else:
    if search_term:
        st.info(f"총 {len(final_filtered_musicals)}개의 뮤지컬을 찾았습니다.")
    
    for musical in final_filtered_musicals:
        text_color = musical.get('text_color', default_text_color)
        
        # 포스터 표시 로직
        col1, col2 = st.columns([1, 3]) # 포스터와 정보 영역 비율 조정
        with col1:
            poster_url = musical.get("poster_url")
            if poster_url:
                st.image(poster_url, use_column_width=True)
            else:
                # 포스터 URL이 없는 경우 임시 이미지 표시
                st.image(f"https://placehold.co/600x848/1E1E1E/FFFFFF?text={musical['title'].replace(' ', '+')}", use_column_width=True)

        with col2:
            st.markdown(f"<h2 style='text-align: center; color: #C0A062;'>{musical['title']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; color: {text_color};'>{musical['summary']}</p>", unsafe_allow_html=True)

            with st.expander("역대 주요 출연진 보기"):
                for role, actors in musical['cast'].items():
                    st.markdown(f"<p style='text-align: center; color: {text_color};'><strong>{role}:</strong> {', '.join(actors)}</p>", unsafe_allow_html=True)
        
        st.divider()
