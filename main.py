import streamlit as st
import requests
import streamlit.components.v1 as components
import json

# --- 1. ПАРАМЕТРЛЕР (Өзгертпеңіз) ---
URL = "https://bjqoazdkiyhrdrfkkgaz.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJqcW9hemRraXlocmRyZmtrZ2F6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3NTM4NjIsImV4cCI6MjA4NTMyOTg2Mn0.0t4S6fa9CmYa6WBdDvkVr4V4H91wLx9xLYtcEdriX4I"
TABLE_NAME = "sor_8_rus" # Кесте аты сол күйі қалды

st.set_page_config(page_title="ФИЗИКА: ҚЫСЫМ ТАҚЫРЫБЫНА СОР", layout="wide", page_icon="⚖️")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- 2. СТИЛЬ (Дизайн) ---
st.markdown("""
    <style>
    * { -webkit-user-select: none; user-select: none; } 
    .stApp { background-color: #f0f2f6; }
    .main-title { color: #2c3e50; text-align: center; font-weight: 800; padding: 20px; border-bottom: 3px solid #3498db; }
    .question-box { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #3498db; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

def send_data(payload):
    headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
    return requests.post(f"{URL}/rest/v1/{TABLE_NAME}", json=payload, headers=headers)

# --- 3. НЕГІЗГІ БЕТ ---
st.markdown("<h1 class='main-title'>⚖️ ФИЗИКА: «ҚЫСЫМ» ТАҚЫРЫБЫНА СОР</h1>", unsafe_allow_html=True)

if st.session_state.submitted:
    st.balloons()
    st.success("🎉 Жауаптарың сәтті қабылданды! Төмендегі іздеу бөлімінен нәтижені біле аласың.")
    if st.button("Қайта бастау 🔄"):
        st.session_state.submitted = False
        st.rerun()
else:
    st.warning("⚠️ **Нұсқаулық:** Жауаптарды мұқият жазыңыз. Есептердің шығарылу жолын көрсету баллды арттырады. Басқа терезеге өтпеңіз!")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Оқушының аты-жөні:", placeholder="Мысалы: Асқаров Нұрлан")
    with col2:
        s_class = st.selectbox("🏫 Сыныбыңыз:", ["8 А", "8 Б", "8 В", "8 Г"])

    if name:
        # ANTI-CHEAT JS
        components.html(f"""
            <script>
            let isSubmitting = false;
            document.addEventListener("visibilitychange", function() {{
                if (document.hidden && !isSubmitting) {{
                    const payload = {{
                        student_name: "{name}",
                        student_class: "{s_class}",
                        status: "cheated",
                        answers: {{ "lang": "kz" }},
                        ai_feedback: "🚫 ЖҰМЫС ЖОЙЫЛДЫ: Анти-чит жүйесі басқа бетке өткеніңізді анықтады."
                    }};
                    fetch('{URL}/rest/v1/{TABLE_NAME}', {{
                        method: 'POST',
                        headers: {{ 'apikey': '{KEY}', 'Authorization': 'Bearer {KEY}', 'Content-Type': 'application/json' }},
                        body: JSON.stringify(payload)
                    }}).then(() => {{ 
                        isSubmitting = true;
                        window.parent.location.reload(); 
                    }});
                }}
            }});
            </script>
        """, height=0)

        with st.form("physics_exam_kz"):
            
            st.markdown("### 📝 ТАПСЫРМАЛАР:")

            # 1-есеп
            st.markdown("<div class='question-box'><b>1. Массасы 50 кг баланың еденге түсіретін қысымын табыңыз.</b> Оның екі бәтеңкесінің табанының ауданы 250 см². (Ескерту: см²-ты м²-қа айналдыру: 250 / 10 000).</div>", unsafe_allow_html=True)
            q1 = st.text_area("Шешуі мен жауабы (Паскальмен):", key="q1")

            # 2-есеп
            st.markdown("<div class='question-box'><b>2. Неліктен шаңғымен қардың үстінде жүргенде адам батып кетпейді, ал жай аяқ киіммен батып кетеді?</b> Физикалық тұрғыдан түсіндіріңіз.</div>", unsafe_allow_html=True)
            q2 = st.text_area("Түсіндірмеңіз:", key="q2")

            # 3-есеп
            st.markdown("<div class='question-box'><b>3. Тік бұрышты параллелепипед пішінді кірпіштің қырлары 5 см, 10 см және 20 см.</b> Кірпіш қай жағымен жатқанда ең аз қысым түсіреді? Ең көп қысым ше?</div>", unsafe_allow_html=True)
            q3 = st.text_area("Жауабыңыз бен себебі:", key="q3")

            # 4-есеп
            st.markdown("<div class='question-box'><b>4. Тереңдігі 5 метр болатын бассейннің түбіндегі судың қысымын есептеңіз.</b> (Судың тығыздығы ρ = 1000 кг/м³; g ≈ 10 Н/кг).</div>", unsafe_allow_html=True)
            q4 = st.text_area("Шешуі мен жауабы:", key="q4")

            # 5-есеп
            st.markdown("<div class='question-box'><b>5. Гидравликалық престің кіші поршенінің ауданы 2 см², үлкенінікі 100 см².</b> Кіші поршеньге 50 Н күш түсірілсе, үлкен поршень қандай күшпен көтеріледі?</div>", unsafe_allow_html=True)
            q5 = st.text_area("Есептелу жолы мен жауабы (Ньютонмен):", key="q5")

            submit_btn = st.form_submit_button("ЖҰМЫСТЫ ТАПСЫРУ ✅")

            if submit_btn:
                if not name or len(name) < 3:
                    st.error("❌ Аты-жөніңізді жазыңыз!")
                else:
                    all_answers = {
                        "lang": "kz",
                        "questions": {
                            "1": q1, "2": q2, "3": q3, "4": q4, "5": q5
                        }
                    }
                    payload = {
                        "student_name": name, 
                        "student_class": s_class,
                        "answers": all_answers,
                        "status": "pending"
                    }
                    resp = send_data(payload)
                    if resp.status_code in [200, 201, 204]:
                        st.session_state.submitted = True
                        st.rerun()
                    else:
                        st.error(f"⚠️ Қате: {resp.text}")

# --- 4. НӘТИЖЕНІ ІЗДЕУ ---
st.markdown("---")
st.markdown("### 🔎 Нәтижеңді тексер")
search_query = st.text_input("Есіміңді жаз (Мысалы: Асқаров):", key="search_input")

if search_query:
    s_headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}"}
    res = requests.get(f"{URL}/rest/v1/{TABLE_NAME}?student_name=ilike.*{search_query}*&select=*&order=id.desc", headers=s_headers)
    
    if res.status_code == 200:
        results = res.json()
        if len(results) > 0:
            for data in results:
                with st.container():
                    st.markdown(f"#### 👤 {data['student_name']} ({data['student_class']})")
                    if data['status'] == 'cheated':
                        st.error("🚫 Жұмыс жойылды: Анти-чит жүйесі іске қосылған.")
                    elif data['status'] == 'pending':
                        st.warning("⏳ Мұғалім әлі тексерген жоқ. Күте тұрыңыз...")
                    else:
                        col_score, col_fb = st.columns([1, 3])
                        with col_score:
                            st.metric("Жиналған балл", f"{data.get('score', 0)} / 20")
                        with col_fb:
                            with st.expander("📝 Мұғалімнің пікірі мен талдауы (AI)", expanded=True):
                                st.write(data.get('ai_feedback', 'Талдау жасалуда...'))
                    st.markdown("<br>", unsafe_allow_html=True)