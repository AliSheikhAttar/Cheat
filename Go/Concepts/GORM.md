# ORM Library for Go: **GORM**  
One of the most popular ORM libraries for Go is **GORM**. It simplifies database interactions by providing an object-oriented approach to CRUD (Create, Read, Update, Delete) operations.

---

## 🔹 How GORM Helps Prevent SQL Injection Attacks  

SQL injection occurs when an attacker manipulates a query by injecting malicious SQL code. ORM libraries like **GORM** help prevent this by using **prepared statements and parameterized queries**, which ensure that user inputs are treated as data rather than executable SQL code.

---

## ✅ Example of SQL Injection Prevention in GORM  

### ❌ **Vulnerable Raw SQL Query (Unsafe)**
```go
db.Exec("SELECT * FROM users WHERE username = '" + userInput + "'")
```
⚠️ If `userInput` is `"admin' OR 1=1 --"`, it could return all users, leading to unauthorized access.

---

### ✅ **Safe Query Using GORM**
```go
var user User
db.Where("username = ?", userInput).First(&user)
```
🔹 **Why is this safe?**  
- The `?` **placeholder** ensures `userInput` is treated as a value, not SQL code.  
- GORM **automatically escapes** special characters, preventing malicious SQL execution.

---

## 🔹 Additional Security Features of GORM  
1. **Auto-Escaping Input Data** – Prevents direct SQL injection.  
2. **Preloading & Eager Loading** – Avoids manual query construction mistakes.  
3. **Logging & Debugging** – Helps detect suspicious query patterns.  

---

GORM makes database operations **safer, cleaner, and more efficient** in Go applications. 