CREATE DATABASE School;
USE School;

CREATE TABLE Students(
	id INT,
	name VARCHAR(50),
	age INT
    );
    
INSERT INTO Students(name, age) VALUES
('Ravi',20),
('Anita',21),
('Kiran',19),
('Meena',22),
('Rahul',20),
('Sita',23),
('Arjun',18),
('Priya',21),
('Vikram',22),
('Divya',19);

SELECT*FROM Students;
--AND
SELECT*FROM students
WHERE age > 20 AND name = 'Ravi';
--OR
SELECT*FROM students
WHERE age = 20 OR age = 21;
--NOT
SELECT*FROM students
WHERE NOT age = 20;
--LIMIT return only 5 records
SELECT*FROM students
LIMIT 5;
--OFFSET skips first three and return next 5
SELECT*FROM students
LIMIT 5 OFFSET 3;
--LIKE
SELECT*FROM students
WHERE name LIKE 'R%';
--LIKE for name endswith
SELECT*FROM students
WHERE name LIKE '%a';
--REGEXP can helps to find names at a time
SELECT*FROM students
WHERE name REGEXP '^[RS]';
