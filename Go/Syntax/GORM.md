## 🔹 How GORM Helps Prevent SQL Injection Attacks  

SQL injection occurs when an attacker manipulates a query by injecting malicious SQL code. ORM libraries like **GORM** help prevent this by using **prepared statements and parameterized queries**, which ensure that user inputs are treated as data rather than executable SQL code.

---

## Example of SQL Injection Prevention in GORM  

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

## tags
```go
type User struct {
	ID         int64  `gorm:"primaryKey"`
	Username   string `gorm:"column:user_name;unique"`
	Password   string
	History    string         `gorm:"type:text"`
	HistoryMap map[string]int `gorm:"-"`
}
```
* Gorm cannot work with private fields(start with not capitalized letters)
