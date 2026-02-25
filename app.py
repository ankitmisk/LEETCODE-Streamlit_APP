import streamlit as st
import pandas as pd
import random
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
# SESSION STATE INIT
# --------------------------------
if "user" not in st.session_state:
    st.session_state.user = None

if "progress" not in st.session_state:
    st.session_state.progress = 0

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "rank" not in st.session_state:
    st.session_state.rank = random.choice(
        ["Bronze 🟤", "Silver ⚪", "Gold 🟡", "Platinum 🔵", "Diamond 💎"]
    )

if "avatar" not in st.session_state:
    st.session_state.avatar = random.choice(
        ["🧑‍💻", "👩‍💻", "🧠", "🚀", "🔥", "😎"]
    )

# --------------------------------
# DATABASE
# --------------------------------
setup_database()
conn = get_connection()

# --------------------------------
# LOGIN SCREEN
# --------------------------------
if st.session_state.user is None:
    st.title("🔐 Welcome to SQL Practice Lab")
    username = st.text_input("Enter your name to continue")

    if st.button("Login"):
    if username.strip():
        st.session_state.user = username.strip()
        st.rerun()
    else:
        st.warning("Please enter a valid name.")

    st.stop()

# --------------------------------
# THEME SETTINGS
# --------------------------------
is_dark = st.session_state.theme == "Dark"
editor_theme = "monokai" if is_dark else "chrome"

bg_color = "#0e1117" if is_dark else "#ffffff"
text_color = "#ffffff" if is_dark else "#000000"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------
# TOP BAR (AVATAR + PROGRESS)
# --------------------------------
col_a, col_b, col_c = st.columns([2, 4, 2])

with col_a:
    st.markdown(f"### {st.session_state.avatar} {st.session_state.user}")

with col_b:
    st.progress(st.session_state.progress)
    st.caption("Learning Progress")

with col_c:
    st.markdown(f"### 🏆 Rank: {st.session_state.rank}")

st.divider()

# --------------------------------
# SIDEBAR
# --------------------------------
st.sidebar.title("🧠 SQL Practice Lab")

st.sidebar.toggle(
    "🌗 Dark / Light Mode",
    value=is_dark,
    key="theme_toggle"
)

if st.session_state.theme_toggle:
    st.session_state.theme = "Dark"
else:
    st.session_state.theme = "Light"

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

st.sidebar.dataframe(
    pd.read_sql("SELECT * FROM employees LIMIT 5", conn),
    use_container_width=True
)

# --------------------------------
# EXPECTED OUTPUT
# --------------------------------
expected_df = pd.read_sql(question["expected_query"], conn)
st.sidebar.markdown("### ✅ Expected Output")
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
        st.info(question["hint"])

with col2:
    if st.button("🧩 Solution"):
        st.code(solutions[question["id"]])

# --------------------------------
# SQL EDITOR
# --------------------------------
user_query = st_ace(
    placeholder="-- Write your SQL query here",
    language="sql",
    theme=editor_theme,
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

            st.session_state.progress = min(
                st.session_state.progress + 10, 100
            )

        else:
            st.error("❌ Output does not match expected result.")

    except Exception as e:
        st.error(f"⚠ SQL Error: {e}")

# --------------------------------
# FOOTER
# --------------------------------
st.divider()
st.markdown(
    """
    <div style="text-align:center; opacity:0.8;">
        Made with ❤️ by <b>Ankit Mishra</b><br>
        <a href="https://www.linkedin.com/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/" target="_blank">GitHub</a> |
        <a href="https://instagram.com/" target="_blank">Instagram</a>
    </div>
    """,
    unsafe_allow_html=True
)
