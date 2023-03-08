-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE d.id = 2
GROUP BY s.fullname
ORDER BY average_grade DESC 
LIMIT 1;

