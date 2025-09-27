--- day24_sql_basic_queries.sql ---

-- Q1: Employees with salary > 60000
SELECT e.emp_id, e.name, s.salary
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
WHERE s.salary > 60000
ORDER BY s.salary DESC;

-- Q2: Employee name, dept name, salary
SELECT e.emp_id, e.name, d.dept_name, s.salary
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
JOIN departments d ON e.dept_id = d.dept_id;

-- Q3: Avg salary per department
SELECT d.dept_id, d.dept_name, AVG(s.salary) AS avg_salary
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name;
