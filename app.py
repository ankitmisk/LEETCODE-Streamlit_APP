import streamlit as st
import pandas as pd
from streamlit_ace import st_ace

from database import setup_database, get_connection
from questions import questions
from solutions import solutions
from validator import is_safe_query, validate

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="SQL Practice Lab", layout="wide")

# -------------------------------
# DATABASE
# -------------------------------
setup_database()
conn = get_connection()

# -------------------------------
# SESSION STATE FOR AUDIO
# -------------------------------
if "play_win" not in st.session_state:
    st.session_state.play_win = False

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("🧠 SQL Practice Lab")

difficulty = st.sidebar.selectbox(
    "Difficulty", ["Easy", "Intermediate", "Hard", "Very Hard"]
)

filtered = [q for q in questions if q["difficulty"] == difficulty]
question_map = {q["question"]: q for q in filtered}
selected = st.sidebar.selectbox("Question", question_map.keys())
question = question_map[selected]

# -------------------------------
# SAMPLE DATA
# -------------------------------
st.sidebar.markdown("### 📊 Sample Records")

st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM employees LIMIT 5", conn),
    use_container_width=True
)

# -------------------------------
# EXPECTED OUTPUT
# -------------------------------
expected_df = pd.read_sql(question["expected_query"], conn)
st.sidebar.markdown("### ✅ Expected Output")
st.sidebar.dataframe(expected_df, use_container_width=True)

# -------------------------------
# MAIN UI
# -------------------------------
st.title("🧪 SQL Coding Playground")
st.subheader("📘 Question")
st.write(question["question"])

# -------------------------------
# DARK MODE SQL EDITOR
# -------------------------------
user_query = st_ace(
    placeholder="-- Write your SQL query here",
    language="sql",
    theme="monokai",
    keybinding="vscode",
    min_lines=14,
    font_size=15
)

# -------------------------------
# RUN QUERY
# -------------------------------
if st.button("▶ Run Query"):

    if not user_query or not user_query.strip():
        st.warning("Please write a SQL query.")
        st.stop()

    if not is_safe_query(user_query):
        st.error("⛔ Only SELECT queries allowed.")
        st.stop()

    try:
        user_df = pd.read_sql(user_query, conn)
        st.dataframe(user_df, use_container_width=True)

        if validate(user_df, expected_df):
            st.success("🎉 HURRAY! Correct Answer 🥳🔥")
            st.balloons()
            st.session_state.play_win = True
        else:
            st.error("❌ Incorrect output. Try again.")

    except Exception as e:
        st.error(f"SQL Error: {e}")

# -------------------------------
# 🎊 PLAY WIN SOUND (WORKS)
# -------------------------------
if st.session_state.play_win:
    with open("mixkit-animated-small-group-applause-523.wav", "rb") as f:
        st.audio(f.read(), format="audio/wav")
    st.session_state.play_win = False
