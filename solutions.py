solutions = {
    1: "SELECT * FROM employees;",
    2: "SELECT name, salary FROM employees;",
    3: "SELECT * FROM employees WHERE department='IT';",
    4: "SELECT department, AVG(salary) FROM employees GROUP BY department;",
    5: """
        SELECT department, MAX(salary)
        FROM employees
        GROUP BY department;
    """
}
