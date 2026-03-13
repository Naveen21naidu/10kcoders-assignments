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
--DQL
SELECT*FROM Students;
--DDL
--MODIFY
ALTER TABLE Students
ADD grade VARCHAR(10);
--DELETE
DROP TABLE students;
--REMOVE ALL LEFT TABLE
TRUNCATE TABLE Students;
--DML
INSERT INTO Students(name,age)
VALUES ('Ravi',20);
--UPDATE DATA
UPDATE Students
SET age = 21
WHERE name = 'Ravi';
--DELETE DATA
DELETE FROM Students
WHERE name = 'Ravi';
