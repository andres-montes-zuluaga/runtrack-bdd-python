# RUNTRACK DATABASES & PYTHON
_A SQL query goes into a bar, walks up to two tables and asks, "Can I join you?"_

## Table of Contents

1. [Introduction](#introduction)
2. [Day 01](#day-01)
   - [SQL Queries](#sql-queries)
     - [Advanced Filters](#advanced-filters)
     - [Sorting Results](#sorting-results)
   - [Data Management](#data-management)
   - [Statistics and Analysis](#statistics-and-analysis)
   - [Exporting Results](#exporting-results)
3. [Day 02](#day-02)
   - [Enhanced Python & SQL Integration](#enhanced-python--sql-integration)
   - [Practical Applications](#practical-applications)
   - [Database Design and Implementation](#database-design-and-implementation)
     - [Animal Table](#animal-table)
     - [Cage Table](#cage-table)
   - [Python Integration](#python-integration)
   - [Practical Implementation](#practical-implementation)

## INTRODUCTION

Welcome to the **Runtrack Databases & Python** project, where SQL mastery meets Python ingenuity! This repository documents a journey of exploring database management and integration with Python through practical, real-world scenarios.

Over two intensive sessions, a variety of database-related skills were developed—from crafting advanced SQL queries to designing a functional database system for a zoo. With a blend of structured data management and Python-driven operations, this project demonstrates the seamless union of these two technologies to tackle complex, dynamic problems efficiently.

Dive into the details below to discover how SQL and Python come together to build versatile, scalable, and efficient database management solutions.


## DAY 01

During the session, several topics related to database management in MySQL were covered, including queries to filter, modify, delete and analyze data in the etudiant table of the laplateforme database. Here is an optimized summary of the work done:

### SQL queries

- Running advanced filters using WHERE, AND and LIKE, including specific searches such as students with names starting with a specific letter.

- Sorting results using ORDER BY in ascending (ASC) or descending (DESC) format.

### Data management

- Updating data using UPDATE commands, such as changing the age of a specific student.

- Controlled deletion of records with DELETE, using unique identifiers to avoid mass affectations.

### Statistics and analysis

- Calculation of the average age of students with AVG.

- Computation of the total number of students and specific groupings using COUNT.

- Retrieval of information about the youngest student using a combination of ORDER BY and LIMIT.

### Exporting results

- Use of SELECT INTO OUTFILE and output redirection to save data to external files.

## DAY 2

The session underscored the importance of blending SQL skills with Python programming to create efficient, user-friendly database management systems. These practices reflect the adaptability and versatility required for scalable database solutions.
During this session, we focused on the creation of a database system to manage a zoo, as well as advanced database interactions using Python and MySQL. Here is an optimized summary of the work done:

### Enhanced Python & SQL Integration

Designed a Python class to manage employees, showcasing CRUD operations with methods for adding, updating, reading, and deleting records from a MySQL table.

### Practical Applications

Applied SQL joins to combine data from multiple tables efficiently (e.g., linking employees to services).

Calculated statistics like the total number of employees or total cage surface area dynamically, demonstrating real-world data analysis capabilities.

### Database Design and Implementation

- **Created a new database named zoo and defined two relational tables:**

**animal**: Includes unique identifiers, names, species, cage IDs, birth dates, and countries of origin for each animal.

**cage**: Contains unique identifiers, surface areas, and maximum capacities for cages.

### Python Integration

Developed a comprehensive Python class Zoo to manage database operations, allowing the director to perform CRUD (Create, Read, Update, Delete) operations on the animal and cage tables.

- **Key functionalities of the class include:**

Adding and deleting animals or cages.

Modifying details for existing animals.

Displaying all animals in the zoo and animals in specific cages.

Calculating the total surface area of all cages combined.

### Practical Implementation

Used Python’s mysql-connector-python library to execute SQL queries efficiently, enabling seamless interaction between the program and the MySQL database.

Tested all methods to ensure proper functionality and reliability in real-world applications.

This session demonstrated the integration of database management and programming to create a real-life solution for managing a zoo’s operations, showcasing the power of SQL and Python when combined effectively.
