--- Day23_sql_window_functions.sql ---

-- Rank employees by salary within department
SELECT e.emp_id, e.name, e.dept_id, s.salary,
       RANK() OVER (PARTITION BY e.dept_id ORDER BY s.salary DESC) AS dept_rank
FROM employees e
JOIN salaries s ON e.emp_id = s.emp_id;

-- For each dept, show employee(s) with highest salary
WITH ranked AS (
  SELECT e.emp_id, e.name, e.dept_id, s.salary,
         RANK() OVER (PARTITION BY e.dept_id ORDER BY s.salary DESC) AS rnk
  FROM employees e
  JOIN salaries s ON e.emp_id = s.emp_id
)
SELECT emp_id, name, dept_id, salary FROM ranked WHERE rnk = 1;
