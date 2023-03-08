-- Знайти список курсів, які відвідує студент.
SELECT s.fullname, d.name
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
WHERE s.id = 5
GROUP BY d.name 