-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN teachers t ON t.id = g.discipline_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE t.id = 4
GROUP BY t.fullname