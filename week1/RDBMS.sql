--revise the class and create a database add 10 students in a table.

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
