import streamlit as st
import pandas as pd
from streamlit_ace import st_ace

from database import setup_database, get_connection
from questions import questions
from solutions import solutions
from validator import is_safe_query, validate

st.set_page_config(page_title="SQL Practice Lab", layout="wide")

setup_database()
conn = get_connection()

# 🎧 Typing + Click Sound
st.components.v1.html("""
<script>
const keySound = new Audio("https://www.soundjay.com/mechanical/keyboard-1.mp3");
document.addEventListener("keydown", () => {
  keySound.volume = 0.15;
  keySound.currentTime = 0;
  keySound.play();
});
</script>
""", height=0)

# Sidebar
st.sidebar.title("🧠 SQL Practice")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Intermediate", "Hard", "Very Hard"]
)

filtered = [q for q in questions if q["difficulty"] == difficulty]
question_map = {q["question"]: q for q in filtered}
selected_q = st.sidebar.selectbox("Questions", question_map.keys())

question = question_map[selected_q]

# Sample Tables
st.sidebar.markdown("### 📊 Sample Records")

st.sidebar.write("**Employees**")
st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM employees LIMIT 5", conn),
    use_container_width=True
)

st.sidebar.write("**Departments**")
st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM departments LIMIT 5", conn),
    use_container_width=True
)

# Expected Output
st.sidebar.markdown("### ✅ Expected Output")
expected_df = pd.read_sql(question["expected_query"], conn)
st.sidebar.dataframe(expected_df, use_container_width=True)

# Main Area
st.title("🧪 SQL Coding Playground")
st.subheader("📘 Question")
st.write(question["question"])

if st.button("💡 Hint"):
    st.info(question["hint"])

if st.button("🧩 Solution"):
    st.code(solutions[question["id"]])

# SQL Editor
user_query = st_ace(
    placeholder="Write your SQL query here...",
    language="sql",
    theme="sqlserver",
    keybinding="vscode",
    min_lines=10,
    font_size=14
)

# Run Query
if st.button("▶ Run Query"):
    if not user_query:
        st.warning("Write a query first.")
        st.stop()

    if not is_safe_query(user_query):
        st.error("⛔ Only SELECT queries allowed.")
        st.stop()

    try:
        user_df = pd.read_sql(user_query, conn)
        st.subheader("📤 Your Output")
        st.dataframe(user_df, use_container_width=True)

        if validate(user_df, expected_df):
            st.success("🎉 Hurray! Correct Answer 🥳🔥")
            st.balloons()
        else:
            st.error("❌ Output does not match. Try again!")

    except Exception as e:
        st.error(f"⚠ SQL Error: {e}")
