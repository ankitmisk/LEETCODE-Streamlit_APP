import streamlit as st
import pandas as pd
from streamlit_ace import st_ace

from database import setup_database, get_connection
from questions import questions
from solutions import solutions
from validator import is_safe_query, validate

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="SQL Practice Lab",
    layout="wide"
)

# --------------------------------
# DATABASE
# --------------------------------
setup_database()
conn = get_connection()

# --------------------------------
# SOUND HELPERS (LOCAL FILES)
# --------------------------------
def play_click_sound():
    st.components.v1.html(
        """
        <script>
        const clickSound = new Audio("mixkit-single-key-type-2533.wav");
        clickSound.volume = 0.4;
        clickSound.play();
        </script>
        """,
        height=0
    )

def play_win_sound():
    st.components.v1.html(
        """
        <script>
        const winSound = new Audio("mixkit-animated-small-group-applause-523.wav");
        winSound.volume = 0.7;
        winSound.play();
        </script>
        """,
        height=0
    )

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("🧠 SQL Practice Lab")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Intermediate", "Hard", "Very Hard"]
)

filtered_questions = [q for q in questions if q["difficulty"] == difficulty]
question_map = {q["question"]: q for q in filtered_questions}
selected_question = st.sidebar.selectbox("Select Question", question_map.keys())
question = question_map[selected_question]

# --------------------------------
# SAMPLE DATA
# --------------------------------
st.sidebar.markdown("### 📊 Sample Records")

st.sidebar.write("Employees")
st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM employees LIMIT 5", conn),
    use_container_width=True
)

st.sidebar.write("Departments")
st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM departments LIMIT 5", conn),
    use_container_width=True
)

# --------------------------------
# EXPECTED OUTPUT
# --------------------------------
st.sidebar.markdown("### ✅ Expected Output")
expected_df = pd.read_sql(question["expected_query"], conn)
st.sidebar.dataframe(expected_df, use_container_width=True)

# --------------------------------
# MAIN UI
# --------------------------------
st.title("🧪 SQL Coding Playground")
st.subheader("📘 Question")
st.write(question["question"])

col1, col2 = st.columns(2)

with col1:
    if st.button("💡 Hint"):
        play_click_sound()
        st.info(question["hint"])

with col2:
    if st.button("🧩 Solution"):
        play_click_sound()
        st.code(solutions[question["id"]])

# --------------------------------
# DARK MODE SQL EDITOR
# --------------------------------
user_query = st_ace(
    placeholder="-- Write your SQL query here",
    language="sql",
    theme="monokai",      # 🌙 DARK MODE
    keybinding="vscode",
    font_size=15,
    min_lines=14,
    wrap=True,
    show_gutter=True
)

# --------------------------------
# RUN QUERY
# --------------------------------
if st.button("▶ Run Query"):
    play_click_sound()

    if not user_query or not user_query.strip():
        st.warning("Please write a SQL query first.")
        st.stop()

    if not is_safe_query(user_query):
        st.error("⛔ Only SELECT queries are allowed.")
        st.stop()

    try:
        user_df = pd.read_sql(user_query, conn)

        st.subheader("📤 Your Output")
        st.dataframe(user_df, use_container_width=True)

        if validate(user_df, expected_df):
            st.success("🎉 HURRAY! Correct Answer 🥳🔥")
            st.balloons()
            play_win_sound()   # 🎊 CROWD APPLAUSE

        else:
            st.error("❌ Output does not match expected result.")

    except Exception as e:
        st.error(f"⚠ SQL Error: {e}")
