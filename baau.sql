SELECT *
FROM birinci_cədvəl
JOIN ikinci_cədvəl
ON əlaqə_şərti;








SELECT s.name, d.department_name
FROM students
JOIN departments
ON s.department_id = d.id;







SELECT students.name, departments.department_name
FROM students
LEFT JOIN departments
ON students.department_id = departments.id;





SELECT students.id, students.name
FROM students
LEFT JOIN departments
ON students.department_id = departments.id
WHERE departments.id IS NULL;





SELECT 
    s.name AS telebe_adi,
    d.department_name AS ixtisas
FROM students s
LEFT JOIN departments d
ON s.department_id = d.id;





SELECT colors.color, sizes.size
FROM colors
CROSS JOIN sizes;



