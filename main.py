import streamlit as st
import requests
import streamlit.components.v1 as components
import json

# --- 1. НАСТРОЙКИ БАЗЫ ---
URL = "https://bjqoazdkiyhrdrfkkgaz.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJqcW9hemRraXlocmRyZmtrZ2F6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3NTM4NjIsImV4cCI6MjA4NTMyOTg2Mn0.0t4S6fa9CmYa6WBdDvkVr4V4H91wLx9xLYtcEdriX4I"
TABLE_NAME = "sor_8_rus"

st.set_page_config(page_title="СОР ПО ФИЗИКЕ - 8 КЛАСС", layout="wide", page_icon="⚡")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- 2. СТИЛЬ ---
st.markdown("""
    <style>
    * { -webkit-user-select: none; user-select: none; } 
    .stApp { background-color: #f8f9fa; }
    .stRadio > div { background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #dee2e6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 10px; }
    .stTextArea textarea { font-size: 16px; border-radius: 10px; }
    .main-title { color: #1e3a8a; text-align: center; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

def send_data(payload):
    headers = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
    return requests.post(f"{URL}/rest/v1/{TABLE_NAME}", json=payload, headers=headers)

# --- 3. ГЛАВНАЯ СТРАНИЦА ---
st.markdown("<h1 class='main-title'>⚡ ФИЗИКА 8 КЛАСС: СОР (Суммативное оценивание)</h1>", unsafe_allow_html=True)

if st.session_state.submitted:
    st.balloons()
    st.success("🎉 Твоя работа успешно принята! Дождись проверки учителем или найди результат ниже.")
    if st.button("Начать заново 🔄"):
        st.session_state.submitted = False
        st.rerun()
else:
    st.info("ℹ️ **Инструкция:** Внимательно прочитайте вопросы и дайте ответ. Все поля обязательны к заполнению. Максимальный балл: 20.")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Имя и фамилия ученика:", placeholder="Например: Иванов Иван")
    with col2:
        s_class = st.selectbox("🏫 Ваш класс:", ["8 А", "8 Б", "8 В", "8 Г"])

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
                        answers: {{ "lang": "ru" }}, // Метка языка внутри JSON
                        ai_feedback: "🚫 РАБОТА АННУЛИРОВАНА: Сработал анти-чит (переход в другое окно)."
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

        with st.form("exam_8_physics_ru"):
            st.subheader("📍 РАЗДЕЛ А: Тестовые задания (10 баллов)")
            q1 = st.radio("1. В каких единицах измеряется внутренняя энергия?", ["A) Ватт", "B) Джоуль", "C) Ньютон", "D) Паскаль"], index=None)
            q2 = st.radio("2. Какой вид теплопередачи возможен в вакууме?", ["A) Конвекция", "B) Теплопроводность", "C) Излучение", "D) Диффузия"], index=None)
            q3 = st.radio("3. Какова температура кипения воды при нормальных условиях?", ["A) 0°C", "B) 80°C", "C) 100°C", "D) 273°C"], index=None)
            q4 = st.radio("4. Формула первого закона термодинамики:", ["A) Q = ΔU + A", "B) Q = cmΔt", "C) η = A/Q", "D) pV = nRT"], index=None)
            q5 = st.radio("5. Как меняется температура жидкости при испарении?", ["A) Повышается", "B) Понижается", "C) Не меняется", "D) Сначала растет"], index=None)
            q6 = st.radio("6. Чему равен элементарный электрический заряд?", ["A) 1.6 * 10^-19 Кл", "B) 9 * 10^9 Кл", "C) 1.6 * 10^-31 Кл", "D) 1 Кл"], index=None)
            q7 = st.radio("7. Как взаимодействуют одноименные заряды (+ и +)?", ["A) Притягиваются", "B) Отталкиваются", "C) Не взаимодействуют", "D) Нейтрализуются"], index=None)
            q8 = st.radio("8. Прибор для обнаружения электрического заряда:", ["A) Термометр", "B) Барометр", "C) Электроскоп", "D) Спидометр"], index=None)
            q9 = st.radio("9. Формула закона Кулона:", ["A) F = ma", "B) F = k*q1*q2/r^2", "C) F = mg", "D) E = F/q"], index=None)
            q10 = st.radio("10. Какой заряд получает стеклянная палочка при трении о шелк?", ["A) Отрицательный (-)", "B) Положительный (+)", "C) Нейтральный (0)", "D) Сначала положительный"], index=None)

            st.subheader("📍 РАЗДЕЛ В: Краткие ответы (6 баллов)")
            q11 = st.text_area("11. Почему металлическая ложка кажется холоднее деревянной?", height=70)
            q12 = st.text_area("12. Как изменится сила Кулона, если расстояние между двумя зарядами увеличить в 3 раза?", height=70)

            st.subheader("📍 РАЗДЕЛ С: Решение задачи (4 балла)")
            q13 = st.text_area("13. Задача: r = 10 см, q1 = 2*10^-7 Кл, q2 = 5*10^-7 Кл. Найдите силу взаимодействия (F):", height=100)

            submit_btn = st.form_submit_button("ЗАВЕРШИТЬ РАБОТУ ✅")

            if submit_btn:
                if not name or len(name) < 3:
                    st.error("❌ Пожалуйста, введите имя и фамилию!")
                else:
                    all_answers = {
                        "lang": "ru", # Тілді осында жасырдық (баған қосудың қажеті жоқ)
                        "section_a": [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10],
                        "section_b": {"q11": q11, "q12": q12},
                        "section_c": {"q13": q13}
                    }
                    payload = {
                        "student_name": name, 
                        "student_class": s_class,
                        "answers": all_answers,
                        "status": "pending"  # ОРЫСША СТАТУС (Воркер үшін маңызды)
                    }
                    resp = send_data(payload)
                    if resp.status_code in [200, 201, 204]:
                        st.session_state.submitted = True
                        st.rerun()
                    else:
                        st.error(f"⚠️ Ошибка базы данных: {resp.text}")

# --- 4. ПОИСК РЕЗУЛЬТАТА ---
st.markdown("---")
st.markdown("### 🔎 Проверить результат")
search_query = st.text_input("Введите имя:", key="search_input")

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
                        st.error("🚫 Работа аннулирована: Сработал анти-чит.")
                    elif data['status'] == 'pending': # Осы жерін өзгерттік
                        st.warning("⏳ Твоя работа еще проверяется...")
                    else:
                        col_score, col_fb = st.columns([1, 3])
                        with col_score:
                            st.metric("Общий балл", f"{data.get('score', 0)} / 20")
                        with col_fb:
                            with st.expander("📝 Отзыв учителя (AI)", expanded=True):
                                st.write(data.get('ai_feedback', 'Отзыв готовится...'))
                    st.markdown("<br>", unsafe_allow_html=True)