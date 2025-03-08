# postgres

- date diff
w1.recordDate = w2.recordDate+1
```sql
DATEDIFF(w1.recordDate , w2.recordDate) = 1
```

- drop if exists
```sql
DROP TABLE IF EXISTS album;
```

- create, primary, composite, foreign key
```sql
CREATE TABLE Student (
    ID INT PRIMARY KEY,
    name VARCHAR(255),
    dept_name VARCHAR(255),
    tot_cred INT,
    FOREIGN KEY (dept_name) REFERENCES Department(dept_name)
);

CREATE TABLE Takes (
    ID INT,
    course_id VARCHAR(255),
    sec_id VARCHAR(255),
    semester VARCHAR(255),
    year INT,
    grade DECIMAL(3,2),
    PRIMARY KEY (ID, course_id, sec_id, semester, year),
    FOREIGN KEY (ID) REFERENCES Student(ID),
    FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES Section(course_id, sec_id, semester, year)
);
```