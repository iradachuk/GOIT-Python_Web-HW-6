-- Список курсів, які певному студенту читає певний викладач.
SELECT t.fullname AS teacher, s.fullname AS student, d.name AS discipline
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE s.id = 5 AND t.id = 3
GROUP BY d.name