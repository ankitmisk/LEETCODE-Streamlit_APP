questions = [
    {
        "id": 1,
        "difficulty": "Easy",
        "question": "Show all employees",
        "expected_query": "SELECT * FROM employees"
    },
    {
        "id": 2,
        "difficulty": "Easy",
        "question": "List employee names and salary",
        "expected_query": "SELECT name, salary FROM employees"
    },
    {
        "id": 3,
        "difficulty": "Easy",
        "question": "Find employees from IT department",
        "expected_query": "SELECT * FROM employees WHERE department='IT'"
    },
    {
        "id": 4,
        "difficulty": "Intermediate",
        "question": "Find average salary per department",
        "expected_query": "SELECT department, AVG(salary) FROM employees GROUP BY department"
    },
    {
        "id": 5,
        "difficulty": "Hard",
        "question": "Find highest paid employee in each department",
        "expected_query": """
        SELECT department, MAX(salary)
        FROM employees
        GROUP BY department
        """
    },
]

# 👉 You can extend this list to 50 easily
