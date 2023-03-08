import sqlite3
from pprint import pprint


def execute_query(sql: str) -> list:
    with sqlite3.connect('hw6.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql_1 = '''
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM GRADES g
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.fullname
ORDER BY average_grade DESC 
LIMIT 5;
'''

# Знайти студента із найвищим середнім балом з певного предмета.
sql_2 = '''
SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE d.id = 2
GROUP BY s.fullname
ORDER BY average_grade DESC 
LIMIT 1;
'''

# Знайти середній бал у групах з певного предмета.
sql_3 = '''
SELECT gr.name AS group_name, d.name, s.fullname, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 1
GROUP BY gr.name;
'''

# Знайти середній бал на потоці(по всій таблиці оцінок).
sql_4 = '''
SELECT gr.name, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 2
GROUP BY gr.name;
'''

# Знайти які курси читає певний викладач.
sql_5 = '''
SELECT t.fullname, d.name
FROM teachers t 
JOIN disciplines d ON t.id = d.teacher_id 
WHERE t.id = 5;
'''

# Знайти список студентів у певній групі.
sql_6 = '''
SELECT gr.name, s.fullname
FROM students s 
JOIN [groups] gr ON gr.id = s.group_id
WHERE gr.id = 1
GROUP BY s.fullname;
'''

# Знайти оцінки студентів у окремій групі з певного предмета.
sql_7 = '''
SELECT d.name, gr.name, s.fullname, g.grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 3 AND d.id = 4;
'''

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
sql_8 = '''
SELECT t.fullname, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g 
JOIN teachers t ON t.id = g.discipline_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE t.id = 4
GROUP BY t.fullname
'''

# Знайти список курсів, які відвідує студент.
sql_9 = '''
SELECT s.fullname, d.name
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
WHERE s.id = 5
GROUP BY d.name
'''

# Список курсів, які певному студенту читає певний викладач.
sql_10 = '''
SELECT t.fullname AS teacher, s.fullname AS student, d.name AS discipline
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id 
JOIN students s ON s.id = g.student_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE s.id = 5 AND t.id = 3
GROUP BY d.name
'''

if __name__ == '__main__':
    print('\n1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.\n')
    pprint(execute_query(sql_1))
    print('\n2. Знайти студента із найвищим середнім балом з певного предмета.\n')
    pprint(execute_query(sql_2))
    print('\n3. Знайти середній бал у групах з певного предмета.\n')
    pprint(execute_query(sql_3))
    print('\n4. Знайти середній бал на потоці (по всій таблиці оцінок).\n')
    pprint(execute_query(sql_4))
    print('\n5. Знайти які курси читає певний викладач.\n')
    pprint(execute_query(sql_5))
    print('\n6. Знайти список студентів у певній групі.\n')
    pprint(execute_query(sql_6))
    print('\n7. Знайти оцінки студентів у окремій групі з певного предмета.\n')
    pprint(execute_query(sql_7))
    print('\n8. Знайти середній бал, який ставить певний викладач зі своїх предметів.\n')
    pprint(execute_query(sql_8))
    print('\n9. Знайти список курсів, які відвідує студент.\n')
    pprint(execute_query(sql_9))
    print('\n10. Список курсів, які певному студенту читає певний викладач.\n')
    pprint(execute_query(sql_10))
