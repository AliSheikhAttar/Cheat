In Go, the choice between **pointer receivers** (`*BankAccount`) and **value receivers** (`Person`) depends on two key factors:  
1. **Whether you need to modify the struct’s state**.  
2. **Performance considerations** (avoid copying large structs).  

Here’s a breakdown of why the examples use each approach:

---

### **1. Pointer Receivers (`*BankAccount`)**  
Used when:  
- You need to **modify the struct’s fields** (mutate state).  
- The struct is **large**, and copying it would be inefficient.  

**Example**:  
```go
func (b *BankAccount) Deposit(amount float64) {
    b.balance += amount // Modify the original struct’s balance
}
```  
- **Why a pointer?**  
  - Without `*BankAccount`, `b` would be a **copy** of the struct, and changes to `balance` would only affect the copy.  
  - The pointer ensures changes persist outside the method.  

---

### **2. Value Receivers (`Person`)**  
Used when:  
- The method **doesn’t modify the struct’s state** (read-only).  
- The struct is **small**, and copying is trivial.  

**Example**:  
```go
func (p Person) Greet() string {
    return fmt.Sprintf("Hi, I'm %s!", p.Name) // Read-only, no mutation
}
```  
- **Why a value?**  
  - Safe for concurrency (no risk of accidental mutation).  
  - Simpler and avoids unnecessary indirection.  

---

### **Key Differences**  
| **Aspect**            | **Pointer Receiver (`*T`)**              | **Value Receiver (`T`)**               |  
|------------------------|------------------------------------------|-----------------------------------------|  
| **Mutation**           | Modifies the original struct.            | Works on a copy; changes are local.     |  
| **Performance**        | Better for large structs (no copying).   | Safe for small structs.                 |  
| **Concurrency**        | Risk of race conditions if not guarded.  | Thread-safe (immutable copy).           |  
| **Interface Matching** | Methods with `*T` receivers work with `T` and `*T`. | Methods with `T` receivers work with `T` and `*T`. |  

---

### **When to Use Each**  
1. **Use Pointer Receivers** (`*T`) when:  
   - You need to modify the struct’s data.  
   - The struct is large (e.g., contains arrays, nested structs).  
   - You want consistency across all methods of a type (even if some don’t mutate).  

2. **Use Value Receivers** (`T`) when:  
   - The method is read-only.  
   - The struct is small (e.g., `Person` with a few fields).  
   - You want to avoid side effects (functional-style programming).  

---

### **Example Explained**  
```go
// Pointer receiver: modifies state
func (b *BankAccount) Deposit(amount float64) {
    b.balance += amount // ✅ Changes the original struct
}

// Value receiver: read-only
func (p Person) Greet() string {
    return fmt.Sprintf("Hi, I'm %s!", p.Name) // ✅ Safe for immutability
}
```

---

### **Special Case: Mixing Receivers**  
Go allows mixing pointer and value receivers for the same struct, but this is generally discouraged for consistency.  

```go
type Counter struct {
    count int
}

// Pointer receiver: modifies state
func (c *Counter) Increment() {
    c.count++
}

// Value receiver: read-only
func (c Counter) Get() int {
    return c.count
}
```

---

### **Summary**  
- **Pointer Receivers**: For mutation and large structs.  
- **Value Receivers**: For immutability and small structs.  
- **Rule of Thumb**: Use pointers unless you have a specific reason to use values.  

This design choice is fundamental to Go’s simplicity and performance. Let me know if you’d like more examples! 🚀