import streamlit as st
import pandas as pd
from database import setup_database, get_connection
from questions import questions
from solutions import solutions
from validator import validate

st.set_page_config(page_title="SQL Practice App", layout="wide")

setup_database()
conn = get_connection()

st.sidebar.title("🧠 SQL Practice")

difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Intermediate", "Hard"])

filtered_questions = [q for q in questions if q["difficulty"] == difficulty]

question_texts = {q["question"]: q for q in filtered_questions}
selected_question = st.sidebar.selectbox("Choose Question", question_texts.keys())

question = question_texts[selected_question]

st.sidebar.markdown("### 📋 Tables")
st.sidebar.code("""
employees(emp_id, name, department, salary, join_date)
departments(dept_id, dept_name)
""")

show_hint = st.sidebar.button("💡 Show Hint")
show_solution = st.sidebar.button("🧩 Show Solution")

st.title("🧪 SQL Coding Playground")

st.subheader("📘 Question")
st.write(question["question"])

if show_hint:
    st.info("Think about SELECT, WHERE, GROUP BY, JOIN based on question")

if show_solution:
    st.code(solutions[question["id"]])

user_query = st.text_area("✍️ Write your SQL query here", height=200)

if st.button("▶ Run Query"):
    try:
        user_df = pd.read_sql(user_query, conn)
        expected_df = pd.read_sql(question["expected_query"], conn)

        st.subheader("📤 Output")
        st.dataframe(user_df)

        if validate(user_df, expected_df):
            st.success("🎉 Hurray! Correct Answer 🥳🔥")
            st.balloons()
        else:
            st.error("❌ Incorrect output. Try again!")

    except Exception as e:
        st.error(f"⚠ SQL Error: {e}")
