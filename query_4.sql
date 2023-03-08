-- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT gr.name, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 2
GROUP BY gr.name;
