import streamlit as st
import pandas as pd
from streamlit_ace import st_ace

from database import setup_database, get_connection
from questions import questions
from solutions import solutions
from validator import is_safe_query, validate

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="SQL Practice Lab", layout="wide")

# -----------------------------
# DATABASE SETUP
# -----------------------------
setup_database()
conn = get_connection()

# -----------------------------
# 🔊 GLOBAL SOUNDS (Typing + Click)
# -----------------------------
st.components.v1.html(
    """
<script>
/* Typing sound */
const typingSound = new Audio("https://www.soundjay.com/mechanical/sounds/keyboard-1.mp3");
typingSound.volume = 0.12;

document.addEventListener("keydown", function(e) {
    if (e.key.length === 1 || e.key === "Backspace" || e.key === "Enter") {
        typingSound.currentTime = 0;
        typingSound.play();
    }
});

/* Button click sound */
const clickSound = new Audio("https://www.soundjay.com/buttons/sounds/button-16.mp3");
clickSound.volume = 0.25;

document.addEventListener("click", function() {
    clickSound.currentTime = 0;
    clickSound.play();
});
</script>
""",
    height=0,
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🧠 SQL Practice Lab")

difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    ["Easy", "Intermediate", "Hard", "Very Hard"]
)

filtered_questions = [q for q in questions if q["difficulty"] == difficulty]
question_map = {q["question"]: q for q in filtered_questions}
selected_question = st.sidebar.selectbox("Select Question", question_map.keys())

question = question_map[selected_question]

# -----------------------------
# SAMPLE TABLE DATA
# -----------------------------
st.sidebar.markdown("### 📊 Sample Table Records")

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

# -----------------------------
# EXPECTED OUTPUT
# -----------------------------
st.sidebar.markdown("### ✅ Expected Output")
expected_df = pd.read_sql(question["expected_query"], conn)
st.sidebar.dataframe(expected_df, use_container_width=True)

# -----------------------------
# MAIN AREA
# -----------------------------
st.title("🧪 SQL Coding Playground")
st.subheader("📘 Question")
st.write(question["question"])

col1, col2 = st.columns(2)

with col1:
    if st.button("💡 Hint"):
        st.info(question["hint"])

with col2:
    if st.button("🧩 Solution"):
        st.code(solutions[question["id"]])

# -----------------------------
# SQL EDITOR (Ace)
# -----------------------------
user_query = st_ace(
    placeholder="Write your SQL query here...",
    language="sql",
    theme="sqlserver",
    keybinding="vscode",
    min_lines=12,
    font_size=14,
    wrap=True,
)

# -----------------------------
# RUN QUERY
# -----------------------------
if st.button("▶ Run Query"):
    if not user_query or not user_query.strip():
        st.warning("⚠ Please write a SQL query.")
        st.stop()

    if not is_safe_query(user_query):
        st.error("⛔ Only SELECT queries are allowed. DDL/DML is restricted.")
        st.stop()

    try:
        user_df = pd.read_sql(user_query, conn)

        st.subheader("📤 Your Output")
        st.dataframe(user_df, use_container_width=True)

        if validate(user_df, expected_df):
            st.success("🎉 HURRAY! Correct Answer 🥳🔥")
            st.balloons()

            # 🎊 WIN / CROWD CHEER SOUND
            st.components.v1.html(
                """
<script>
const winSound = new Audio("https://www.soundjay.com/human/sounds/applause-8.mp3");
winSound.volume = 0.6;
winSound.play();
</script>
""",
                height=0,
            )

        else:
            st.error("❌ Output does not match expected result. Try again!")

    except Exception as e:
        st.error(f"⚠ SQL Error: {e}")
