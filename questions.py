questions = [

# =========================
# EASY (1–15)
# =========================

{
"id": 1,
"difficulty": "Easy",
"question": "Show all employees",
"hint": "Use SELECT *",
"expected_query": "SELECT * FROM employees"
},
{
"id": 2,
"difficulty": "Easy",
"question": "Show employee names and salary",
"hint": "Select specific columns",
"expected_query": "SELECT name, salary FROM employees"
},
{
"id": 3,
"difficulty": "Easy",
"question": "Find employees working in IT department",
"hint": "Use WHERE clause",
"expected_query": "SELECT * FROM employees WHERE department = 'IT'"
},
{
"id": 4,
"difficulty": "Easy",
"question": "Show employees with salary greater than 60000",
"hint": "Use comparison operator",
"expected_query": "SELECT * FROM employees WHERE salary > 60000"
},
{
"id": 5,
"difficulty": "Easy",
"question": "List employees ordered by salary",
"hint": "Use ORDER BY",
"expected_query": "SELECT * FROM employees ORDER BY salary"
},
{
"id": 6,
"difficulty": "Easy",
"question": "Show unique departments",
"hint": "Use DISTINCT",
"expected_query": "SELECT DISTINCT department FROM employees"
},
{
"id": 7,
"difficulty": "Easy",
"question": "Count total employees",
"hint": "Use COUNT",
"expected_query": "SELECT COUNT(*) FROM employees"
},
{
"id": 8,
"difficulty": "Easy",
"question": "Find minimum salary",
"hint": "Use MIN function",
"expected_query": "SELECT MIN(salary) FROM employees"
},
{
"id": 9,
"difficulty": "Easy",
"question": "Find maximum salary",
"hint": "Use MAX function",
"expected_query": "SELECT MAX(salary) FROM employees"
},
{
"id": 10,
"difficulty": "Easy",
"question": "Show employees joined after 2020",
"hint": "Compare dates",
"expected_query": "SELECT * FROM employees WHERE join_date > '2020-01-01'"
},
{
"id": 11,
"difficulty": "Easy",
"question": "Show employees from HR department",
"hint": "Filter using WHERE",
"expected_query": "SELECT * FROM employees WHERE department = 'HR'"
},
{
"id": 12,
"difficulty": "Easy",
"question": "Display employee names in alphabetical order",
"hint": "ORDER BY name",
"expected_query": "SELECT name FROM employees ORDER BY name"
},
{
"id": 13,
"difficulty": "Easy",
"question": "Show top 3 highest paid employees",
"hint": "Use ORDER BY DESC and LIMIT",
"expected_query": "SELECT * FROM employees ORDER BY salary DESC LIMIT 3"
},
{
"id": 14,
"difficulty": "Easy",
"question": "Find employees with salary between 50000 and 80000",
"hint": "Use BETWEEN",
"expected_query": "SELECT * FROM employees WHERE salary BETWEEN 50000 AND 80000"
},
{
"id": 15,
"difficulty": "Easy",
"question": "Show employees whose name starts with 'A'",
"hint": "Use LIKE",
"expected_query": "SELECT * FROM employees WHERE name LIKE 'A%'"
},

# =========================
# INTERMEDIATE (16–30)
# =========================

{
"id": 16,
"difficulty": "Intermediate",
"question": "Find average salary of all employees",
"hint": "Use AVG",
"expected_query": "SELECT AVG(salary) FROM employees"
},
{
"id": 17,
"difficulty": "Intermediate",
"question": "Find department-wise employee count",
"hint": "GROUP BY department",
"expected_query": "SELECT department, COUNT(*) FROM employees GROUP BY department"
},
{
"id": 18,
"difficulty": "Intermediate",
"question": "Find department-wise average salary",
"hint": "Aggregate + GROUP BY",
"expected_query": "SELECT department, AVG(salary) FROM employees GROUP BY department"
},
{
"id": 19,
"difficulty": "Intermediate",
"question": "Show departments having more than 2 employees",
"hint": "Use HAVING",
"expected_query": "SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 2"
},
{
"id": 20,
"difficulty": "Intermediate",
"question": "Join employees with departments table",
"hint": "Use INNER JOIN",
"expected_query": """
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.department = d.dept_name
"""
},
{
"id": 21,
"difficulty": "Intermediate",
"question": "Find total salary per department",
"hint": "SUM + GROUP BY",
"expected_query": "SELECT department, SUM(salary) FROM employees GROUP BY department"
},
{
"id": 22,
"difficulty": "Intermediate",
"question": "Find employees earning above average salary",
"hint": "Use subquery",
"expected_query": "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)"
},
{
"id": 23,
"difficulty": "Intermediate",
"question": "Find latest joined employee",
"hint": "ORDER BY date DESC",
"expected_query": "SELECT * FROM employees ORDER BY join_date DESC LIMIT 1"
},
{
"id": 24,
"difficulty": "Intermediate",
"question": "Find employees not in Finance department",
"hint": "Use NOT operator",
"expected_query": "SELECT * FROM employees WHERE department != 'Finance'"
},
{
"id": 25,
"difficulty": "Intermediate",
"question": "Count employees joined each year",
"hint": "Use substr on date",
"expected_query": "SELECT substr(join_date,1,4), COUNT(*) FROM employees GROUP BY substr(join_date,1,4)"
},
{
"id": 26,
"difficulty": "Intermediate",
"question": "Find second highest salary",
"hint": "Use subquery with MAX",
"expected_query": "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees)"
},
{
"id": 27,
"difficulty": "Intermediate",
"question": "Show employees whose salary is above department average",
"hint": "Correlated subquery",
"expected_query": """
SELECT *
FROM employees e
WHERE salary >
(
SELECT AVG(salary)
FROM employees
WHERE department = e.department
)
"""
},
{
"id": 28,
"difficulty": "Intermediate",
"question": "Find department with highest average salary",
"hint": "ORDER BY AVG DESC",
"expected_query": """
SELECT department
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
LIMIT 1
"""
},
{
"id": 29,
"difficulty": "Intermediate",
"question": "Find total employees in IT department",
"hint": "COUNT with WHERE",
"expected_query": "SELECT COUNT(*) FROM employees WHERE department = 'IT'"
},
{
"id": 30,
"difficulty": "Intermediate",
"question": "Find employees joined in same year",
"hint": "GROUP BY year",
"expected_query": "SELECT substr(join_date,1,4), COUNT(*) FROM employees GROUP BY substr(join_date,1,4)"
},

# =========================
# HARD (31–40)
# =========================

{
"id": 31,
"difficulty": "Hard",
"question": "Find highest paid employee in each department",
"hint": "GROUP BY + MAX",
"expected_query": """
SELECT department, MAX(salary)
FROM employees
GROUP BY department
"""
},
{
"id": 32,
"difficulty": "Hard",
"question": "Find employees earning exactly department maximum salary",
"hint": "Correlated subquery",
"expected_query": """
SELECT *
FROM employees e
WHERE salary =
(
SELECT MAX(salary)
FROM employees
WHERE department = e.department
)
"""
},
{
"id": 33,
"difficulty": "Hard",
"question": "Find departments with average salary greater than 65000",
"hint": "HAVING AVG",
"expected_query": """
SELECT department
FROM employees
GROUP BY department
HAVING AVG(salary) > 65000
"""
},
{
"id": 34,
"difficulty": "Hard",
"question": "Find employees who earn more than their manager (assume manager has higher emp_id)",
"hint": "Self join logic",
"expected_query": "SELECT * FROM employees"
},
{
"id": 35,
"difficulty": "Hard",
"question": "Find top 2 salaries per department",
"hint": "Use subquery and COUNT",
"expected_query": """
SELECT *
FROM employees e1
WHERE (
SELECT COUNT(DISTINCT salary)
FROM employees e2
WHERE e2.department = e1.department
AND e2.salary > e1.salary
) < 2
"""
},
{
"id": 36,
"difficulty": "Hard",
"question": "Find employees with duplicate salaries",
"hint": "GROUP BY salary",
"expected_query": """
SELECT *
FROM employees
WHERE salary IN (
SELECT salary
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1
)
"""
},
{
"id": 37,
"difficulty": "Hard",
"question": "Find departments having at least one employee earning more than 80000",
"hint": "Use EXISTS",
"expected_query": """
SELECT DISTINCT department
FROM employees e
WHERE EXISTS (
SELECT 1
FROM employees
WHERE department = e.department
AND salary > 80000
)
"""
},
{
"id": 38,
"difficulty": "Hard",
"question": "Find employees who joined earliest in each department",
"hint": "MIN date",
"expected_query": """
SELECT *
FROM employees e
WHERE join_date =
(
SELECT MIN(join_date)
FROM employees
WHERE department = e.department
)
"""
},
{
"id": 39,
"difficulty": "Hard",
"question": "Find employees earning between department min and max",
"hint": "Use subqueries",
"expected_query": """
SELECT *
FROM employees e
WHERE salary BETWEEN
(
SELECT MIN(salary) FROM employees WHERE department = e.department
)
AND
(
SELECT MAX(salary) FROM employees WHERE department = e.department
)
"""
},
{
"id": 40,
"difficulty": "Hard",
"question": "Find total salary contribution percentage per employee",
"hint": "Use subquery",
"expected_query": """
SELECT name,
(salary * 100.0 / (SELECT SUM(salary) FROM employees)) AS percentage
FROM employees
"""
},

# =========================
# VERY HARD (41–50)
# =========================

{
"id": 41,
"difficulty": "Very Hard",
"question": "Find second highest salary in each department",
"hint": "Correlated subquery",
"expected_query": """
SELECT *
FROM employees e1
WHERE 1 =
(
SELECT COUNT(DISTINCT salary)
FROM employees e2
WHERE e2.department = e1.department
AND e2.salary > e1.salary
)
"""
},
{
"id": 42,
"difficulty": "Very Hard",
"question": "Find employees who are top earners company-wide",
"hint": "MAX salary",
"expected_query": "SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees)"
},
{
"id": 43,
"difficulty": "Very Hard",
"question": "Find departments with highest total salary",
"hint": "ORDER BY SUM DESC",
"expected_query": """
SELECT department
FROM employees
GROUP BY department
ORDER BY SUM(salary) DESC
LIMIT 1
"""
},
{
"id": 44,
"difficulty": "Very Hard",
"question": "Find employees whose salary rank is 3rd highest",
"hint": "COUNT DISTINCT salaries",
"expected_query": """
SELECT *
FROM employees e1
WHERE 2 =
(
SELECT COUNT(DISTINCT salary)
FROM employees e2
WHERE e2.salary > e1.salary
)
"""
},
{
"id": 45,
"difficulty": "Very Hard",
"question": "Find employees earning more than 90 percent of employees",
"hint": "Percentile logic",
"expected_query": """
SELECT *
FROM employees
WHERE salary >
(
SELECT AVG(salary)
FROM employees
)
"""
},
{
"id": 46,
"difficulty": "Very Hard",
"question": "Find department with maximum employee count",
"hint": "COUNT + ORDER",
"expected_query": """
SELECT department
FROM employees
GROUP BY department
ORDER BY COUNT(*) DESC
LIMIT 1
"""
},
{
"id": 47,
"difficulty": "Very Hard",
"question": "Find employees whose salary is closest to average",
"hint": "ABS difference",
"expected_query": """
SELECT *
FROM employees
ORDER BY ABS(salary - (SELECT AVG(salary) FROM employees))
LIMIT 1
"""
},
{
"id": 48,
"difficulty": "Very Hard",
"question": "Find employees earning above company median salary",
"hint": "Median logic using subquery",
"expected_query": """
SELECT *
FROM employees
WHERE salary >
(SELECT AVG(salary) FROM employees)
"""
},
{
"id": 49,
"difficulty": "Very Hard",
"question": "Find employees who joined in same month across years",
"hint": "Extract month",
"expected_query": "SELECT substr(join_date,6,2), COUNT(*) FROM employees GROUP BY substr(join_date,6,2)"
},
{
"id": 50,
"difficulty": "Very Hard",
"question": "Find employees who earn more than all HR employees",
"hint": "Use ALL operator logic",
"expected_query": """
SELECT *
FROM employees
WHERE salary >
(SELECT MAX(salary) FROM employees WHERE department = 'HR')
"""
}

]
